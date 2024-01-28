import pandas as pd
import dash
from dash import dcc, html, Input, Output, dash_table, State
import plotly.express as px
import re
import dash
import pandas as pd
import plotly.express as px
import numpy as np
import base64
# Sample data
df = pd.DataFrame({
    'Text': ['Lorem ipsum dolor sit amet ' + str(i) for i in range(10000)]
})

# Dash app
app = dash.Dash(__name__)

# App layout
app.layout = dash_table.DataTable(
    id='large-text-table',
    columns=[{'name': 'Text', 'id': 'Text'}],
    data=df.to_dict('records'),
    virtualization=True,  # Enable virtualization
    page_size=20,  # Number of rows per page
    style_table={'height': '500px', 'overflowY': 'auto'},  # Set height and enable vertical scroll
    style_cell={'textAlign': 'left'}
)

if __name__ == '__main__':
    app.run_server(debug=True)