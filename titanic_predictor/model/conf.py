import os
data_dir = 'outputs'

df_train = os.path.join(data_dir, 'preprocessed_df.p')
X_train = os.path.join(data_dir, 'X_train.p')
X_test = os.path.join(data_dir, 'X_test.p')
y_train = os.path.join(data_dir, 'y_train.p')
y_test = os.path.join(data_dir, 'y_test.p')
model = os.path.join(data_dir, 'model.p')
metrics = os.path.join(data_dir, 'eval.txt')