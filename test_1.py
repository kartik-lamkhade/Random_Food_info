from fastapi import FastAPI, File, UploadFile
from fastapi import HTTPException, status
from pydantic import BaseModel, Field
import pickle
from pydantic import BaseModel, Field
from typing import Literal, Annotated
import random
from datasets import load_dataset

app = FastAPI()

dataset = load_dataset("json", data_files="foods.json")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Random Food Properties Prediction API. The /predict endpoint accepts an image input and returns randomized property predictions."}

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    if file is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="No file provided"
        )

    sample = random.choice(dataset['train']) 

    result = {
        "name": sample.get("name", "Unknown"),
        "category": sample.get("category", "Unknown"),
        "per_g": sample.get("per_g", 0.0),
        "calories_kcal": sample.get("calories_kcal", 0.0),
        "protein_g": sample.get("protein_g", 0.0),
        "carbs_g": sample.get("carbs_g", 0.0),
        "fats_g": sample.get("fats_g", 0.0)
    }
    if not all(result.values()):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Not in valid format"
        )

    return result