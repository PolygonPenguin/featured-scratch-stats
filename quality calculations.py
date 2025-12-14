import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

from sklearn.metrics import r2_score

data = pd.read_json("data.json")

data["ratio"]=data["views"]/data["loves"]

X=data[['views']]
y=data['ratio']


regression = linear_model.LinearRegression()

regression.fit(X, y)
print("coefs:")
print(regression.coef_, regression.intercept_)

predicted = regression.predict(X)
data["predicted"] = predicted
print("r^2:")
print(r2_score(y, predicted))

data["quality"] =  ((predicted-y)+42)/66*100
