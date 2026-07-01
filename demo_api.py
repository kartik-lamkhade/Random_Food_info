from fastapi import FastAPI
from  fastapi import HTTPException
from pydantic import BaseModel, Field, computed_field
import pickle
from pydantic import BaseModel,Field
from typing import Literal,Annotated
import random
from datasets import load_dataset

app = FastAPI()

dataset = load_dataset("json", data_files="foods.json")

@app.get("/")
def read_root():
    return {"message": "Welcome to the FPS Prediction API! Use the /predict endpoint to get FPS predictions based on your input data."}

@app.get("/predict")
def predict():
    # Randomly select a sample from the dataset
    sample = random.choice(dataset['train'])
    
    # Extract relevant fields from the sample
    result = {
        "name": sample.get("name", "Unknown"),
        "category": sample.get("category", "Unknown"),
        "per_g": sample.get("per_g", 0.0),
        "calories_kcal": sample.get("calories_kcal", 0.0),
        "protein_g": sample.get("protein_g", 0.0),
        "carbs_g": sample.get("carbs_g", 0.0),
        "fats_g": sample.get("fats_g", 0.0)
    }
    
    return result




