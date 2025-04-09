from modules.layout import init_layout
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

from modules.callbacks import *
def main():
    app.title = 'Shop-Check'
    app.layout = init_layout(config)
    app.run_server(host='127.0.0.1', port=8050, debug=False)

if __name__ == '__main__':
    main()
