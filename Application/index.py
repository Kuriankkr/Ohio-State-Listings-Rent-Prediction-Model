## Importing dependencies
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from app import app, server
from layout_assets.complete_layout import main_layout

app.layout = html.Div(
    [
        main_layout
    ], 
)

if __name__ == '__main__':
    app.run_server()