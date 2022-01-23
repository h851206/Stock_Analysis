# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import pandas as pd


def get_options(df):
    Codes = df['Local Symbol'].to_list()
    options_list = [{"label":code, "value":code} for code in Codes]
    return options_list

#Load Data
df = pd.read_csv('data/StockCode.csv', dtype={'Local Symbol': object})
options = get_options(df)

# Initialize the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets) 

app.layout = html.Div(
    [
        html.Div([
            'Please enter the stock code',
            dcc.Dropdown(id="my-multi-dynamic-dropdown", options=[], search_value="", value=[], multi=True),
            html.Button('Submit', id='submit-button', n_clicks=0),
        ], className="three columns", style={"background-color": "#FFF"}),
        html.Div([
            html.Div(id="container-button-basic",
                children=["No data uploaded"], 
                className="row"
            )
            ]
            , className="nine columns"),
    ],
)




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

@app.callback(
    Output("container-button-basic", "children"),
    Input("submit-button", 'n_clicks'),
    State("my-multi-dynamic-dropdown", "value")
)
def data_upload(n_clicks, value):
    return_text = ""
    for v in value:
        Name = df.loc[df["Local Symbol"]==v, "Description"].squeeze()
        return_text = return_text + " " + Name +'('+ v + ')' ",\n"
    return return_text[:-1] + " succesfully uploaded!"


if __name__ == "__main__":
    app.run_server(debug=True)