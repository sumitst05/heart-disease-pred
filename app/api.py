from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from app.model import make_prediction

router = APIRouter()

class HeartData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@router.post("/predict")
async def predict(data: HeartData):
    try:
        prediction = make_prediction(data.model_dump())
        return JSONResponse(
            status_code=200,
            content=prediction,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
