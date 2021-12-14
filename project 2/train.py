import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.feature_extraction import DictVectorizer

from sklearn.metrics import roc_auc_score



# Parameters
max_depth=15
min_samples_leaf=3 
n_estimators=200
output_file = 'model.bin'

# Data Preparation

df = pd.read_csv('data.csv')

print("Reading the file...")

print("Preparing the dataset... ")

df.columns = ['age', 'job', 'marital', 'education', 'default', 
                'balance', 'housing', 'loan', 'contact', 'day', 'month',
                'duration', 'campain', 'passed_days', 'previous', 
                'poutcome', 'success']

df['success'] = df['success'].map({1:0 , 2:1 })

# Train test split
df_train, df_test = train_test_split(df, test_size=0.2, random_state=42)
df_train = df_train.reset_index(drop = True)
df_test = df_test.reset_index(drop = True)

# Label
y_train = df_train['success'].values
y_test = df_test['success'].values
del df_train['success']
del df_test['success']


# Features
dv = DictVectorizer(sparse = False)

train_dict = df_train.to_dict(orient = 'record')
X_train = dv.fit_transform(train_dict)
test_dict = df_test.to_dict(orient = 'record')
X_test = dv.transform(test_dict)


# Training the model
print("Training the model...")

rf = RandomForestClassifier(max_depth = max_depth, 
                            min_samples_leaf= min_samples_leaf, 
                            n_estimators = n_estimators,
                            random_state=42)

rf.fit(X_train, y_train)

# validation
print("Validating the model...")
y_pred = rf.predict_proba(X_test)[:, 1]
score = roc_auc_score(y_test, y_pred)

print("ROC_AUC score for the model on the test set is: ", score)

# Exporting the model
with open(output_file, 'wb') as f_out:
    pickle.dump((dv, rf), f_out)

print("Model is exported to ", output_file)
