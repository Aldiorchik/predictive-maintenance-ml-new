from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

model = joblib.load("data/failure_model.pkl")

@app.post("/predict")
def predict(features: list):
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction[0]),
        "probability": float(probability)
    }

@app.get("/health")
def health():
    return {"status": "ok"}