import pickle
from sklearn.linear_model import BayesianRidge

try: from titanic_predictor import conf
except: import conf

output = conf.model

with open(conf.X_train, 'rb') as fd:
    X_train = pickle.load(fd)

with open(conf.y_train, 'rb') as fd:
    y_train = pickle.load(fd)

reg = BayesianRidge()
reg.fit(X_train, y_train)
print(reg)

with open(output, 'wb') as fd:
    pickle.dump(reg, fd)