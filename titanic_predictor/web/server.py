from flask import Flask, jsonify, request
from titanic_predictor.model.conf import model
from titanic_predictor.model.prepare import preprocess_data
import pickle
import pandas as pd


def compute_prediction():
    with open(model, 'rb') as fd:
        model_matrix = pickle.load(fd)

    data_sent = request.json
    print("data_sent: ", data_sent)

    columns = data_sent.keys()
    df_sent = pd.DataFrame(data_sent, columns=columns, index=[1])
    print("df_sent: ", df_sent)

    X_sent = preprocess_data(df_sent)
    print("X_sent: ", X_sent)

    y_preds = model_matrix.predict(X_sent)
    return y_preds


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
            print(y_preds)
            return jsonify({
                "predictions": y_preds[0]
            })

        return app