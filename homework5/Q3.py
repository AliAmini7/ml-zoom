import pickle

model_file = 'model1.bin'
dv_file = 'dv.bin'

with open(model_file, 'rb') as model_in:
    model = pickle.load(model_in)

with open(dv_file, 'rb') as dv_in:
    dv = pickle.load(dv_in)

costumer = {"contract": "two_year",
            "tenure": 12, 
            "monthlycharges": 19.7}

X = dv.transform([costumer])

print(model.predict_proba(X)[0,1])
