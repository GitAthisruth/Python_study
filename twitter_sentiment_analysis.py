import pandas as pd
import dash
from dash import dcc, html, Input, Output, dash_table
import plotly.express as px

df = pd.read_csv(
    "D:\\ActivBytes_Internship\\Active_Bytes_Tasks\\df_chatgpt_sentiment_analysis.csv"
)
df = df.reset_index()
df = df[["index", "preprocessed_Tweet", "sentiment_score", "sentiment_label"]].copy()
# print(df.head())
df = df.dropna()
df = df.drop_duplicates()

df = df.iloc[:100]
# Create the Dash app
app = dash.Dash(__name__)

# Set up the app layout

app.layout = html.Div(
    children=[
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
    Input(component_id="chatgpt-dropdown1", component_property="value"),
)
def update_scatterplot_graph(value):
    if value == "sentiment_label":
        sentiment_val = df
        # print(sentiment_val)
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
            hover_data=["preprocessed_Tweet"],
        )

    else:
        sentiment_val = df[df["sentiment_label"] == value]
        print(sentiment_val)
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
            hover_data=["preprocessed_Tweet"],
        )
    return scatter_plot


@app.callback(
    Output(component_id="tbl", component_property="data"),
    Input(component_id="chatgpt-dropdown1", component_property="value"),
)
def update_(value):
    if value == "sentiment_label":
        return df.to_dict("records")
    else:
        return df[df["sentiment_label"] == value].to_dict("records")


# @app.callback(
#     Output('container-button-timestamp', 'children'),
#     Input('btn-nclicks-1', 'n_clicks'))

# def button_click():


# Run local server
if __name__ == "__main__":
    app.run_server(debug=True)
