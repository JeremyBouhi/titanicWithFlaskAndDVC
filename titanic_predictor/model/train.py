from sklearn.ensemble import RandomForestRegressor
import pickle

import sys
sys.path.insert(0, '..')
from model import conf

output = conf.model

with open(conf.X_train, 'rb') as fd:
    X_train = pickle.load(fd)

with open(conf.y_train, 'rb') as fd:
    y_train = pickle.load(fd)

reg = RandomForestRegressor()
reg.fit(X_train, y_train)

print(reg)

with open(output, 'wb') as fd:
    pickle.dump(reg, fd)