import pickle
from datetime import datetime
from sklearn.metrics import accuracy_score, mean_squared_error, f1_score
try: from titanic_predictor import conf
except: import conf
import csv

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

with open(conf.X_test, 'rb') as fd:
    X_test = pickle.load(fd)

with open(conf.y_test, 'rb') as fd:
    y_test = pickle.load(fd)

y_preds = model.predict(X_test)

datetime = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

auc = round(accuracy_score(y_test, y_preds.round()), 4)
mse = round(mean_squared_error(y_test, y_preds), 4)
f1 = round(f1_score(y_test, y_preds.round()), 4)
#%%
print(datetime)

metrics_type = ["AUC", "MSE", "F1"]
metrics_data = [auc, mse, f1]
#data = [[datetime], metrics_type, metrics_data]
data = [metrics_type, metrics_data]

print(data)
