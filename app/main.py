from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="ML Prediction API")


class Customer(BaseModel):
    age: int
    monthly_income: float


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(customer: Customer):
    prediction = int(
        customer.age >= 25
        and customer.monthly_income >= 50000
    )

    return {"prediction": prediction}


@app.get("/version")
def version():
    return {"version": "4.0"}


import os

@app.get("/environment")
def environment():
    return {
        "environment": os.getenv("APP_ENV", "development")
    }
