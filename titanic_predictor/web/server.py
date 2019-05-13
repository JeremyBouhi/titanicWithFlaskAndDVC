from flask import Flask, jsonify, request
from titanic_predictor.model.conf import model
from titanic_predictor.model.prepare import preprocess_data
import pickle
import pandas as pd
import csv


def compute_prediction(df):
    with open(model, 'rb') as fd:
        model_matrix = pickle.load(fd)

    X_sent = preprocess_data(df)
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
            data_sent = request.json
            columns = data_sent.keys()
            df_sent = pd.DataFrame(data_sent, columns=columns, index=[1])
            print("df_sent: ", df_sent)

            y_preds = compute_prediction(df_sent)
            print(y_preds)
            return jsonify({
                "predictions": y_preds[0]
            })

        @app.route("/submit", methods=['GET'])
        def submit():
            df_test = pd.read_csv("data/test.csv")
            df_passengers = df_test['PassengerId']
            y_preds = compute_prediction(df_test)

            d = {'PassengerId': df_passengers, 'Survived': y_preds.round()}
            df_submit = pd.DataFrame(data=d)

            print(df_submit)
            df_submit.to_csv('outputs/submission.csv', index=False)

            return 'Ok'

        return app
