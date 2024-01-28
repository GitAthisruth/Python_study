import dash
from dash import dcc, html, Input, Output, State
import dash
import pandas as pd
import base64
import re
import datetime

app = dash.Dash(
    __name__,
)

# Define the layout
app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    "Log File Filtering",
                    style={"color": "Darkseagreen", "font-weight": "bold"},
                )
            ]
        ),
        dcc.Upload(
            id="upload-file",
            children=html.Button("Upload_log_file", style={"font-weight": "bold"}),
            multiple=False,
        ),
        dcc.Store(id="output-store", storage_type="memory"),
        html.H4(id="output-status", style={"color": "red", "font-weight": "bold"}),
        dcc.Dropdown(
            id="dropdown_log_levels",
            options=[
                {"label": "NOTSET", "value": "notset"},
                {"label": " DEBUG", "value": "debug"},
                {"label": "INFO", "value": "info"},
                {"label": "WARN", "value": "warn"},
                {"label": "ERROR", "value": "error"},
                {"label": "CRITICAL", "value": "critical"},
                {"label": "EXCEPTION", "value": "exception"},
                {"label": "ALL", "value": "all"},
            ],
            placeholder="Select an Option",
            style={"color": "violet", "width": "40%"},
            value="",
            clearable=False,
        ),
        html.H3("file name is : "),
        html.Div(
            id="output-file-name",
            style={
                "color": "orange",
            },
        ),
        html.Div(id="filtered-log-timestamp"),
        html.H3(
            "Filtered logs",
            style={
                "color": "blue",
            },
        ),
        html.Div(
            id="filtered-log-output",
            style={
                "width": "100%",
                "height": "400px",
                "overflow": "auto",
            },
        ),
    ]
)


# Define the callback function
@app.callback(
    [
        Output(component_id="output-store", component_property="data"),
        Output(component_id="output-file-name", component_property="children"),
        Output(component_id="output-status", component_property="children"),
    ],
    # Store the output in the 'data' property of the Store component
    [
        Input(component_id="upload-file", component_property="contents"),
    ],
    [Input(component_id="upload-file", component_property="filename")],
)
def filtering_logfile(contents, filename):
    if contents:
        content_type, content_string = contents.split(",")
        decoded = base64.b64decode(content_string).decode("utf-8")
        lines = decoded.split("\n")
        return lines, filename, "Data uploaded successfully"
    return [], filename, "Upload a file"


# @app.callback(
#     [
#         Output(component_id="filtered-log-output", component_property="children"),
#         # Output(component_id="filtered-log-timestamp", component_property="children"),
#     ],
#     [
#         State(component_id="output-store", component_property="data"),
#     ],
#     [Input(component_id="dropdown_log_levels", component_property="value")],
# )


# def filter_log(data, value):
#     filtered_text = []
#     if data:
#         for line in data:
#             if value == "all":
#                 filtered_text.append(line)
#             else:
#                 if value in line.lower():
#                     filtered_text.append(line)
#         if not filtered_text:
#             filtered_text.append("No matching lines found.")
#         return html.Pre("\n".join(filtered_text))
#     return []


@app.callback(
    [
        Output(component_id="filtered-log-output", component_property="children"),
        Output(component_id="filtered-log-timestamp", component_property="children"),
    ],
    [
        State(component_id="output-store", component_property="data"),
    ],
    Input(component_id="dropdown_log_levels", component_property="value"),
)
def filter_log(data, value):
    filtered_text = []
    # filtered_timestamp = []
    # pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    if data:
        for line in data:
            if value == "all":
                # time = re.findall(pattern, line)
                # times = datetime.datetime.strptime(time[0], "%Y-%m-%d %H:%M:%S")
                # print(times)
                # filtered_timestamp.append(times)
                filtered_text.append(line)
            else:
                # time = re.findall(pattern, line)
                # times = datetime.datetime.strptime(time[0], "%Y-%m-%d %H:%M:%S")
                # filtered_timestamp.append(times)
                # print(times)
                if value in line.lower():
                    filtered_text.append(line)

        if not filtered_text:
            # filtered_timestamp.append("no time found")
            filtered_text.append("No matching data found.")
        # print(len(filtered_timestamp))
        # return html.Pre("\n".join(filtered_text)), html.Pre(
        # "\n".join(filtered_timestamp)
        # )
        return html.Pre("\n".join(filtered_text))

    return []


# @app.callback(
#     Output(component_id="filtered-log-timestamp", component_property="children"),
#     Input(component_id="output-store", component_property="data"),

# )


# def filter_timestamp(data):
#     timestamps = []
#     for line in data:
#         time_matches = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line)
#         if time_matches:
#             timestamp = datetime.datetime.strptime(time_matches[0], "%Y-%m-%d %H:%M:%S")
#             timestamps.append(timestamp)
#         return timestamp
#     return "no timestamp found"


if __name__ == "__main__":
    app.run_server(debug=True)
