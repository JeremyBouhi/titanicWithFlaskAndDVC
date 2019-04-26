from flask import Flask


class Server:

    def __init__(self):
        self.server = Flask(__name__)

    def bootstrap(self):
        app = self.server

        @app.route("/")
        def hello():
            return "Hello World"

        return app
