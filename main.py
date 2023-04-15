from typing import Optional
from io import StringIO
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from DataModel import DataModel
from joblib import load
import pandas as pd

from PredictionModel import Model

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_root(request: Request):
   return templates.TemplateResponse("index.html", {"request": request})

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
async def make_predictions(request: Request, file: UploadFile):
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode()))
    
    model = Model()
    predictions_dic = model.make_predictions(df)
    predictions = predictions_dic['prediction']
    return templates.TemplateResponse("index.html", {"request": request, "predictions": dict(predictions)})