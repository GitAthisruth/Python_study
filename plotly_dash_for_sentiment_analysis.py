import pandas as pd
import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import re
import dash
import pandas as pd
import plotly.express as px
from dash import Input, Output, dash_table, dcc, html,State
from transformers import AutoModelForSequenceClassification
# from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer,AutoConfig
# from transformers import pipeline
import numpy as np
from scipy.special import softmax
import time
# import csv
# from nltk.corpus import stopwords
# from nltk.probability import FreqDist

#get the start time 


# df = df.reset_index()
# df["sentiment_label"].value_counts()

# # print(df.head())
# # print(df.isna().sum())


# # preprocessing tweets


# def preprocessing_tweets(tweet):
#     # Removing hashtags
#     tweet = re.sub(r"#\w+", "", tweet)
#     # Removing links
#     tweet = re.sub(r"http\S+|www\S+", "", tweet)
#     # Removing mentions
#     tweet = re.sub(r"@\w+", "", tweet)
#     # Filtering non-alphanumeric characters
#     tweet = re.sub(r"[^\w\s]", "", tweet)
#     # removing digits
#     tweet = re.sub(r"\d+", "", tweet)
#     # Removing emojis
#     tweet = tweet.encode("ascii", "ignore").decode("utf-8")
#     # replacing underscores with empty space
#     tweet = tweet.replace("_", "")
#     # convert the text to lowercase
#     tweet = tweet.lower()
#     # converting all white spaces more than one to one.
#     tweet = re.sub(r"\s+", " ", tweet)

#     return tweet.strip()

# def preprocessing_df(data):
#     data=data[["index", "ID", "Date", "Username", "Tweet"]]
#     data=data.dropna()
#     data=data.drop_duplicates()
#     data["Tweet"] = data["Tweet"].apply(preprocessing_tweets)
#     data=data.iloc[:100]
#     return data

# df=preprocessing_df(df)
# print(df.head())


# # Sentiment analysis
# # load model and tokenizer
# MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
# tokenizer = AutoTokenizer.from_pretrained(MODEL)
# config = AutoConfig.from_pretrained(MODEL)
# model = AutoModelForSequenceClassification.from_pretrained(MODEL)
# # Create empty lists to store the sentiment labels and scores
# sentiment_labels = []
# sentiment_scores = []

# # Iterate over the text data column
# for text in df["Tweet"]:
#     tweet = re.sub(r"#\w+", "", tweet)
#     # Removing links
#     tweet = re.sub(r"http\S+|www\S+", "", tweet)
#     # Removing mentions
#     tweet = re.sub(r"@\w+", "", tweet)
#     # Filtering non-alphanumeric characters
#     tweet = re.sub(r"[^\w\s]", "", tweet)
#     # removing digits
#     tweet = re.sub(r"\d+", "", tweet)
#     # Removing emojis
#     tweet = tweet.encode("ascii", "ignore").decode("utf-8")
#     # replacing underscores with empty space
#     tweet = tweet.replace("_", "")
#     # convert the text to lowercase
#     tweet = tweet.lower()
#     # converting all white spaces more than one to one.
#     tweet = re.sub(r"\s+", " ", tweet)
#     encoded_input = tokenizer(text, return_tensors="pt")
#     output = model(**encoded_input)
#     scores = output[0][0].detach().numpy()
#     scores = softmax(scores)
#     # print(scores)
#     ranking = np.argsort(scores)
#     # print(ranking)
#     ranking = ranking[::-1]
#     labels = config.id2label[ranking[0]]
#     # print(labels)
#     scores_ = scores[ranking[0]]

#     sentiment_labels.append(labels)
#     sentiment_scores.append(scores_)

# # Add the sentiment labels and scores to the dataframe
# df["sentiment_label"] = sentiment_labels
# df["sentiment_score"] = sentiment_scores

# # print(df["sentiment_label"])
# print(df.head())

st=time.time()

df = pd.read_csv("C:\\Users\\LENOVO\\Downloads\\chatgpt-tweets-data-20230310-20230322-processed.csv (1)\\chatgpt-tweets-data-20230310-20230322-processed.csv")
df=df.copy()
# # print(df.shape)
print(df.head())
df=df.iloc[:100]
df=df[['ID', 'Date', 'Username', 'Tweet']]
print(df[['ID', 'Date', 'Username', 'Tweet']])
print(df.columns)


app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.Div(html.Button('Result', id='submit-val', n_clicks=0,style={'border':"white",'font-size': '20px', 'width': '140px', 'display': 'inline-block', 'margin-bottom': '10px', 'margin-right': '5px', 'height':'37px', 'verticalAlign': 'top',"color":"cyan","background-color":"Orange",
                                                                                 })),
        html.H1(
            children="Sentiment_Analysis Dashboard",
            style={"text-align": "center"},
        ),
        html.P(
            "Here is the Scatter plot of tweets about chatGPT, X axis contain tweet index and y axis consist of sentiment_score.",
            style={"color": "skyblue"},
        ),
        dcc.Dropdown(
            id="chatgpt-dropdown1",
            options=[
                {"label": "Neutral", "value": "neutral"},
                {"label": "Positive", "value": "positive"},
                {"label": "Negative", "value": "negative"},
                {"label": "All", "value": "sentiment_label"},
            ],
            placeholder="Select an Option",
            style={"width": "40%"},
            value="",
        ),
        dcc.Graph(id="sentiment_analysis-graph1"),
        html.P("Result Dataframe", style={"color": "red"}),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": i, "id": i} for i in df.columns],
            id="tbl",
            style_data={"textAlign": "left"},  # Set the text alignment to center
        ),
    ],
)

# Set up the callback function


@app.callback(
    Output(component_id="sentiment_analysis-graph1", component_property="figure"),
    [Input(component_id="submit-val", component_property="n_clicks"),
    Input(component_id="chatgpt-dropdown1", component_property="value"),
    Input(component_id="tbl", component_property="data")] 
)
def update_scatterplot_graph(n_clicks,value,data):
    print(n_clicks)
    data=pd.DataFrame(data)
    data=data.copy()
    data = data.reset_index()
    # print(data)
    data=data.dropna()
    data=data.drop_duplicates()
    print(data)
    # Sentiment analysis
    # load model and tokenizer
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    # Create empty lists to store the sentiment labels and scores
    sentiment_labels = []
    sentiment_scores = []
    prepr_tweet=[]


    # Iterate over the text data column
    for text in data["Tweet"]:
        text = re.sub(r"#\w+", "", text)
        # Removing links
        text = re.sub(r"http\S+|www\S+", "", text)
        # Removing mentions
        text = re.sub(r"@\w+", "", text)
        # Filtering non-alphanumeric characters
        text = re.sub(r"[^\w\s]", "", text)
        # removing digits
        text = re.sub(r"\d+", "", text)
       # Removing emojis
        text = text.encode("ascii", "ignore").decode("utf-8")
       # replacing underscores with empty space
        text = text.replace("_", "")
       # convert the text to lowercase
        text = text.lower()
       # converting all white spaces more than one to one.
        text = re.sub(r"\s+", " ", text)
        encoded_input = tokenizer(text, return_tensors="pt")
        output = model(**encoded_input)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        # print(scores)
        ranking = np.argsort(scores)
    # print(ranking)
        ranking = ranking[::-1]
        labels = config.id2label[ranking[0]]
        # print(labels)
        scores_ = scores[ranking[0]]

        sentiment_labels.append(labels)
        sentiment_scores.append(scores_)
        prepr_tweet.append(text)

    # Add the sentiment labels and scores to the dataframe
    data["sentiment_label"] = sentiment_labels
    data["sentiment_score"] = sentiment_scores
    data["Tweet"]=prepr_tweet

    # print(df.head())


    if n_clicks > 0:
        if value == "sentiment_label":
           sentiment_val = data
        #    print(sentiment_val)
           scatter_plot = px.scatter(
            sentiment_val,
            x="index",
            y="sentiment_score",
            color="sentiment_label",
            title=f"sentiment label {value}",
            color_discrete_map={
                "negative": "red",
                "neutral": "blue",
                "positive": "green",
            },
            hover_data=["Tweet"],
        )

        else:
            sentiment_val = data[data["sentiment_label"] == value]
            # print(sentiment_val)
            scatter_plot = px.scatter(
            sentiment_val,
            x=sentiment_val.index,
            y="sentiment_score",
            color="sentiment_label",
            title=f"sentiment label {value}",
            color_discrete_map={
                "negative": "red",
                "neutral": "blue",
                "positive": "green",
            },
            hover_data=["Tweet"],
        )
        return scatter_plot
    else:
        return dash.no_update


@app.callback(
    Output(component_id="tbl", component_property="data"),
    [Input(component_id="submit-val", component_property="n_clicks"),
    Input(component_id="chatgpt-dropdown1", component_property="value"),
    Input(component_id="tbl", component_property="data")] 
)
def update_table_data(n_clicks,value,data):
    if n_clicks>0:

       data=pd.DataFrame(data)
       data=data.copy()
       # print(df)
       data = data.reset_index()
       # print(df)
       data=data[["index","ID","Date","Username","Tweet"]]
       # print(df)
       data=data.dropna()
       data=data.drop_duplicates()
       data=data.iloc[:100]
       # Sentiment analysis
       # load model and tokenizer
       MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
       tokenizer = AutoTokenizer.from_pretrained(MODEL)
       config = AutoConfig.from_pretrained(MODEL)
       model = AutoModelForSequenceClassification.from_pretrained(MODEL)
       # Create empty lists to store the sentiment labels and scores
       sentiment_labels_twi = []
       sentiment_scores_twi = []
       prepr_tweet=[]

       # Iterate over the text data column
       for text in data["Tweet"]:
           text = re.sub(r"#\w+", "", text)
           # Removing links
           text = re.sub(r"http\S+|www\S+", "", text)
           # Removing mentions
           text = re.sub(r"@\w+", "", text)
           # Filtering non-alphanumeric characters
           text = re.sub(r"[^\w\s]", "", text)
           # removing digits
           text = re.sub(r"\d+", "", text)
           # Removing emojis
           text = text.encode("ascii", "ignore").decode("utf-8")
           # replacing underscores with empty space
           text = text.replace("_", "")
           # convert the text to lowercase
           text = text.lower()
           # converting all white spaces more than one to one.
           text = re.sub(r"\s+", " ", text)
           encoded_input = tokenizer(text, return_tensors="pt")
           output = model(**encoded_input)
           scores = output[0][0].detach().numpy()
           scores = softmax(scores)
           # print(scores)
           ranking = np.argsort(scores)
           # print(ranking)
           ranking = ranking[::-1]
           labels = config.id2label[ranking[0]]
           # print(labels)
           scores_ = scores[ranking[0]]

           sentiment_labels_twi.append(labels)
           sentiment_scores_twi.append(scores_)
           prepr_tweet.append(text)


        # Add the sentiment labels and scores to the dataframe
       data["Tweet"]=prepr_tweet
       data["sentiment_label"] = sentiment_labels_twi
       data["sentiment_score"] = sentiment_scores_twi
       # print(df)
       if value == "sentiment_label":
            print(data)
            return data.to_dict("records")
       else:
            print(data)
            return data[data["sentiment_label"] == value].to_dict("records")
         
    else:
        return []
    

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')

if __name__ == "__main__":
    app.run_server(debug=True)


