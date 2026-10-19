from api.models import PredictRequest, PredictResponse
from fastapi import FastAPI
from joblib import load

app = FastAPI()
model = load("model.joblib")
classes = ["setosa", "versicolor", "virginica"]


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:  # LLM
    prediction_index = model.predict(
        [
            [
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )[0]
    return PredictResponse(prediction=classes[int(prediction_index)])
