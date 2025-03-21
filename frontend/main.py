from modules.layout import init_layout

from modules.callbacks import *

def main():
    app.layout = init_layout()
    app.run_server(host='127.0.0.1', port=8050, debug=True)

if __name__ == '__main__':
    main()