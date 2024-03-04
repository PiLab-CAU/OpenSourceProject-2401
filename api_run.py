from fastapi import FastAPI
from pydantic import BaseModel
from prediction import openai_stock_prediction
from database import SentenceDatabase

app = FastAPI()

osp = openai_stock_prediction()
db = SentenceDatabase('sentences.db')
class Item(BaseModel):
    text: str

@app.post("/prediction/")
async def prediction_by_chatgpt(item: Item):
    queries = db.get_all_sentences()
    return {"text": osp.predict(osp.health_checker(item.text), queries)}