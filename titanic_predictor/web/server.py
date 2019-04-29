from flask import Flask, jsonify


def compute_prediction():
    return [0.16019]


class Server:

    def __init__(self):
        self.server = Flask(__name__)

    def bootstrap(self):
        app = self.server

        @app.route("/")
        def hello():
            return "Hello World"

        @app.route("/predict", methods=['POST'])
        def predict():
            y_preds = compute_prediction()
            return jsonify({
                "predictions": y_preds[0]
            })

        return app


