#!/usr/bin/env python
from app import make_app
from config import config

app = make_app()


# That "if" cycle starting server with debugging
if __name__ == "__main__":
    app.run(host=config.HOST, port=config.PORT, debug=config.DEBUG)