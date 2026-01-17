from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load trained ML model
model = joblib.load("sentimentmodel.pkl")

app = FastAPI(title="Sentiment Analysis API (ML Based)")

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_sentiment(data: TextInput):
    prediction = model.predict([data.text])[0]
    confidence = max(model.predict_proba([data.text])[0])

    return {
        "sentiment": prediction,
        "confidence_score": round(float(confidence), 2)
    }
