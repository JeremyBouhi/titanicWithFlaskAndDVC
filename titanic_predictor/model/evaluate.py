import pickle
from sklearn.metrics import accuracy_score
try: from titanic_predictor import conf
except: import conf

with open(conf.model, 'rb') as fd:
    model = pickle.load(fd)

with open(conf.X_test, 'rb') as fd:
    X_test = pickle.load(fd)

with open(conf.y_test, 'rb') as fd:
    y_test = pickle.load(fd)

#%%
y_test.shape
#%%
#auc = model.score(X_test, y_test)
y_preds = model.predict(X_test)
#%%
print(y_preds.round())
#%%
auc = round(accuracy_score(y_preds.round(),y_test)*100,2)
#%%
print(auc)

#%%

with open(conf.metrics, 'w') as fd:
    fd.write('AUC: {:4f}\n'.format(auc))