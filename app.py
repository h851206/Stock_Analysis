# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd


def get_options(df):
    Codes = df['Code'].to_list()
    Names = df['Company'].to_list()
    options_list = [{"label":code, "value":name} for code, name in zip(Codes, Names)]
    return options_list

#Load Data
df = pd.read_csv('data/StockCode.csv', dtype={'Code': object})
options = get_options(df)
print(df.info())

# Initialize the app
app = dash.Dash(__name__)
# app.config.suppress_callback_exceptions = True
app.layout = html.Div([
    html.Div([
        "Multi dynamic Dropdown",
        dcc.Dropdown(id="my-multi-dynamic-dropdown", multi=True),
    ]),
])

@app.callback(
    Output("my-multi-dynamic-dropdown", "options"),
    Input("my-multi-dynamic-dropdown", "search_value"),
    State("my-multi-dynamic-dropdown", "value")

)
def update_multi_options(search_value, value):
    if not search_value:
        raise PreventUpdate
    # Make sure that the set values are in the option list, else they will disappear
    # from the shown select list, but still part of the `value`.
    return [
        o for o in options if search_value in o["label"] or o["value"] in (value or [])
    ]


if __name__ == "__main__":
    app.run_server(debug=True)