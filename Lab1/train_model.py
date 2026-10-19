from joblib import dump
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


data = load_iris()
model = LogisticRegression(max_iter=200)
model.fit(data.data, data.target)

dump(model, "model.joblib")
