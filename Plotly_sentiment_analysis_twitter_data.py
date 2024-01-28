import re
import dash
import pandas as pd
import plotly.express as px
from dash import Input, Output, dash_table, dcc, html
from transformers import AutoModelForSequenceClassification
from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer,AutoConfig
from transformers import pipeline
import numpy as np
from scipy.special import softmax
import csv
from nltk.corpus import stopwords
from nltk.probability import FreqDist

df = pd.read_csv(
    "C:\\Users\\LENOVO\\Downloads\\chatgpt-tweets-data-20230310-20230322-processed.csv (1)\\chatgpt-tweets-data-20230310-20230322-processed.csv"
)
# print(df.shape)
# print(df.head())
df = df.reset_index()
df["sentiment_label"].value_counts()
df = df[["index", "ID", "Date", "Username", "Tweet"]]
df = df.dropna()
df = df.drop_duplicates()
df = df.iloc[:100]
# print(df.head())
# print(df.isna().sum())

# preprocessing tweets


def preprocessing_tweets(tweet):
    # Removing hashtags
    tweet = re.sub(r"#\w+", "", tweet)
    # Removing links
    tweet = re.sub(r"http\S+|www\S+", "", tweet)
    # Removing mentions
    tweet = re.sub(r"@\w+", "", tweet)
    # Filtering non-alphanumeric characters
    tweet = re.sub(r"[^\w\s]", "", tweet)
    # removing digits
    tweet = re.sub(r"\d+", "", tweet)
    # Removing emojis
    tweet = tweet.encode("ascii", "ignore").decode("utf-8")
    # replacing underscores with empty space
    tweet = tweet.replace("_", "")
    # convert the text to lowercase
    tweet = tweet.lower()
    # converting all white spaces more than one to one.
    tweet = re.sub(r"\s+", " ", tweet)

    return tweet.strip()


df["Tweet"] = df["Tweet"].apply(preprocessing_tweets)

# print(df.head())

# Sentiment analysis

# load model and tokenizer
MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

# Create empty lists to store the sentiment labels and scores
sentiment_labels = []
sentiment_scores = []

# Iterate over the text data column
for text in df["Tweet"]:
    encoded_input = tokenizer(text, return_tensors="pt")
    output = model(**encoded_input)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    print(scores)
    ranking = np.argsort(scores)
    print(ranking)
    ranking = ranking[::-1]
    labels = config.id2label[ranking[0]]
    print(labels)
    scores_ = scores[ranking[0]]

    sentiment_labels.append(labels)
    sentiment_scores.append(scores_)

# Add the sentiment labels and scores to the dataframe
df["sentiment_label"] = sentiment_labels
df["sentiment_score"] = sentiment_scores

print(df["sentiment_label"])

# # Create the Dash app
# app = dash.Dash(__name__)

# # Set up the app layout

# app.layout = html.Div(
#     children=[
#         html.Button("Submit", id="submit-button", n_clicks=0),
#         html.H1(
#             children="Sentiment_Analysis Dashboard",
#             style={"text-align": "center"},
#         ),
#         html.P(
#             "Here is the Scatter plot of tweets about chatGPT, X axis contain tweet index and y axis consist of sentiment_score.",
#             style={"color": "skyblue"},
#         ),
#         dcc.Dropdown(
#             id="chatgpt-dropdown1",
#             options=[
#                 {"label": "Neutral", "value": "neutral"},
#                 {"label": "Positive", "value": "positive"},
#                 {"label": "Negative", "value": "negative"},
#                 {"label": "All", "value": "sentiment_label"},
#             ],
#             placeholder="Select an Option",
#             style={"width": "40%"},
#             value="",
#         ),
#         dcc.Graph(id="sentiment_analysis-graph1"),
#         html.P("Result Dataframe", style={"color": "red"}),
#         dash_table.DataTable(
#             data=df.to_dict("records"),
#             columns=[{"name": i, "id": i} for i in df.columns],
#             id="tbl",
#             style_data={"textAlign": "left"},  # Set the text alignment to center
#         ),
#     ],
# )

# # Set up the callback function


# @app.callback(
#     Output(component_id="sentiment_analysis-graph1", component_property="figure"),
#     Input(component_id="submit-button", component_property="n_clicks"),
#     Input(component_id="chatgpt-dropdown1", component_property="value"),
# )
# def update_scatterplot_graph(n_clicks, value):
#     if n_clicks > 0:
#         print(n_clicks)
#         if value == "sentiment_label":
#             sentiment_val = df
#             # print(sentiment_val)
#             scatter_plot = px.scatter(
#                 sentiment_val,
#                 x="index",
#                 y="sentiment_score",
#                 color="sentiment_label",
#                 title=f"sentiment label {value}",
#                 color_discrete_map={
#                     "negative": "red",
#                     "neutral": "blue",
#                     "positive": "green",
#                 },
#                 hover_data=["preprocessed_Tweet"],
#             )

#         else:
#             sentiment_val = df[df["sentiment_label"] == value]
#             # print(sentiment_val)
#             scatter_plot = px.scatter(
#                 sentiment_val,
#                 x=sentiment_val.index,
#                 y="sentiment_score",
#                 color="sentiment_label",
#                 title=f"sentiment label {value}",
#                 color_discrete_map={
#                     "negative": "red",
#                     "neutral": "blue",
#                     "positive": "green",
#                 },
#                 hover_data=["preprocessed_Tweet"],
#             )
#     return scatter_plot


# @app.callback(
#     Output(component_id="tbl", component_property="data"),
#     Input(component_id="chatgpt-dropdown1", component_property="value"),
# )
# def update_(value):
#     if value == "sentiment_label":
#         return df.to_dict("records")
#     else:
#         return df[df["sentiment_label"] == value].to_dict("records")


# # @app.callback(
# #     Output('container-button-timestamp', 'children'),
# #     Input('btn-nclicks-1', 'n_clicks'))

# # def button_click():


# # Run local server
# if __name__ == "__main__":
#     app.run_server(debug=True)
