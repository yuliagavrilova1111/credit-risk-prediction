from fastapi import FastAPI, HTTPException
from .schema import CreditRequest
from .predictor import Predictor

app = FastAPI(title='Credit Default Risk API')
predictor = Predictor()

@app.get('/health')
async def check_health():
    return {'status': 'ok'}

@app.post('/predict')
async def predict(request: CreditRequest):
    try:
        proba = predictor.predict(request.dict())
        return {'probability_default': proba}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))