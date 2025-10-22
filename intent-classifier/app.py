import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from intent_classifier import IntentClassifier

# Load environment variables from .env file
load_dotenv()

# Read environment mode (defaults to prod for safety)
ENV = os.getenv("ENV", "prod").lower()

app = FastAPI(
    # title="Intent Classifier API",
    description="Intent Classifier API",
    version="1.0.0",
    docs_url="/docs",        # Swagger UI
    redoc_url="/redoc",      # ReDoc
)

# Carregando os modelos como variáveis globais
MODELOS = {
    "CONFUSION": IntentClassifier(load_model="models/confusion-v1.keras"),
    "CLAIR": IntentClassifier(load_model="models/clair-v1.keras"),
}

# Corpo do POST
class PredictRequest(BaseModel):
    text: str

"""
Routes
"""

# GET http://localhost:8000/intents/
@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": f"Intent Classifier API is running in {ENV} mode. Check /redoc for more info."
    }

# --- Endpoint Geral ---
@app.post("/predict", tags=["Prediction"])
async def predict_all(request: PredictRequest):
    predictions = {}

    for model_name, classifier in MODELOS.items():
        intent, probabilities = classifier.predict(request.text)

        predictions[model_name] = {
            "intent": intent,
            "probabilities": probabilities
        }
    return predictions

# --- Endpoint Individual (Confusion) ---
@app.post("/confusion", tags=["Prediction"])
async def predict_confusion(request: PredictRequest):
    classifier = MODELOS["CONFUSION"]

    intent, probabilities = classifier.predict(request.text)

    return {
        "intent": intent,
        "probabilities": probabilities
    }

# --- Endpoint Individual (Clair) ---
@app.post("/clair", tags=["Prediction"])
async def predict_clair(request: PredictRequest):
    classifier = MODELOS["CLAIR"]

    intent, probabilities = classifier.predict(request.text)

    return {
        "intent": intent,
        "probabilities": probabilities
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

    # How to run the app
    # python -m uvicorn app:app --host 0.0.0.0 --port 8000