import pandas as pd
import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px
import re
import dash
import pandas as pd
import plotly.express as px
from dash import Input, Output, dash_table, dcc, html, State
from transformers import AutoModelForSequenceClassification

# from transformers import TFAutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig

# from transformers import pipeline
import numpy as np
from scipy.special import softmax
import time


# st=time.time()

df = pd.read_csv(
    "C:\\Users\\LENOVO\\Downloads\\chatgpt-tweets-data-20230310-20230322-processed.csv (1)\\chatgpt-tweets-data-20230310-20230322-processed.csv"
)
df = df.copy()
# # print(df.shape)
print(df.head())
df = df.iloc[:100]
df = df.reset_index()
df = df[["index", "ID", "Date", "Username", "Tweet"]]
df = df.dropna()
new_columns = ["sentiment_label", "sentiment_score"]
new_df = pd.DataFrame(columns=new_columns)
df = pd.concat([df, new_df], axis=1)
print(df)


app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.Div(
            html.Button(
                "Result",
                id="submit-val",
                n_clicks=0,
                style={
                    "border": "white",
                    "font-size": "30px",
                    "width": "140px",
                    "display": "inline-block",
                    "margin-bottom": "10px",
                    "margin-right": "5px",
                    "height": "37px",
                    "verticalAlign": "top",
                    "color": "white",
                    "background-color": "Orange",
                },
            )
        ),
        html.H1(
            children="Sentiment_Analysis Dashboard",
            style={"text-align": "center"},
        ),
        html.P(
            "Here is the Scatter plot of tweets about chatGPT, X axis contain tweet index and y axis consist of sentiment_score.",
            style={"color": "skyblue"},
        ),
        dcc.Graph(id="sentiment_analysis-graph1"),
        html.P("Result Dataframe", style={"color": "red"}),
        html.Label("Filter:"),
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
        dcc.Store(id="output-store_dataframe", storage_type="memory"),
        dash_table.DataTable(
            data=df.to_dict("records"),
            columns=[{"name": i, "id": i} for i in df.columns],
            id="tbl1",
            style_data={"textAlign": "left"},  # Set the text alignment to center
        ),
    ],
)


@app.callback(
    Output(component_id="output-store_dataframe", component_property="data"),
    [
        Input(component_id="submit-val", component_property="n_clicks"),
        Input(
            component_id="tbl1",
            component_property="data",
        ),
    ],
)
# Input(component_id="chatgpt-dropdown1", component_property="value"),])


def update_data(n_clicks, data):
    print(n_clicks)
    data = pd.DataFrame(data)
    # print(data.columns)
    # load model and tokenizer
    MODEL = "cardiffnlp/twitter-roberta-base-sentiment-latest"
    tokenizer = AutoTokenizer.from_pretrained(MODEL)
    config = AutoConfig.from_pretrained(MODEL)
    model = AutoModelForSequenceClassification.from_pretrained(MODEL)
    # Create empty lists to store the sentiment labels and scores
    sentiment_labels = []
    sentiment_scores = []
    prepr_tweet = []

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
    data["Tweet"] = prepr_tweet
    print(data)

    if n_clicks > 0:
        return data.to_dict("records")
    else:
        return dash.no_update


@app.callback(
    [
        Output(component_id="sentiment_analysis-graph1", component_property="figure"),
        Output(component_id="tbl1", component_property="data", allow_duplicate=True),
    ],
    [
        Input(component_id="output-store_dataframe", component_property="data"),
        Input(component_id="chatgpt-dropdown1", component_property="value"),
    ],
    prevent_initial_call=True,
)
def update_plot_and_data(data, value):
    # triggered_input = dash.callback_context.triggered[0]['prop_id'].split('.')[0]
    # print(triggered_input)
    data = pd.DataFrame(data)
    print(data, "sentiment_val")
    if value == "sentiment_label":
        scatter_plot = px.scatter(
            data,
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
        data = data[data["sentiment_label"] == value]
        print(data, "value")
        scatter_plot = px.scatter(
            data,
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
    return scatter_plot, data.to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)
