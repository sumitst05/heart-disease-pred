import joblib
import pandas as pd

model_path = "src/models/heart_model.pkl"

model = joblib.load(model_path)

def make_prediction(data: dict):
    input = pd.DataFrame([data])

    prediction = model.predict(input)
    probab = model.predict_proba(input)[0]

    return {
        "Prediction": int(prediction[0]),
        "Confidence": probab[prediction[0]] * 100,
    }
