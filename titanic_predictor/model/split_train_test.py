from sklearn.model_selection import train_test_split
import pickle

#sys.path.append(os.path.dirname('titanic_predictor'))
#print(sys.path)
import conf

with open(conf.df_train, 'rb') as fd:
    df = pickle.load(fd)

X = df.drop(['Survived'], axis=1).values
print(X)
#%%
y = df['Survived'].values
print(y)

#%%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

with open(conf.X_train, 'wb') as fd:
    pickle.dump(X_train, fd)

with open(conf.X_test, 'wb') as fd:
    pickle.dump(X_test, fd)

with open(conf.y_train, 'wb') as fd:
    pickle.dump(y_train, fd)

with open(conf.y_test, 'wb') as fd:
    pickle.dump(y_test, fd)