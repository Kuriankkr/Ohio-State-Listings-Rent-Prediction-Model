import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
## Instantiating the dashboard application
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
#if __name__ == '__main__':
#    app.run_server()
server = app.server
app.config['suppress_callback_exceptions'] = True