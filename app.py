from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from model.LDA import lda_model
from utils.preprocessing import cleansing, tokenize


app = FastAPI()


class Item(BaseModel):
    articles: List[str]


@app.get("/")
async def hello():
    return {"message": "hello world"}


@app.post("/keyword")
async def keyword(item: Item):
    processed = []
    for num, art in enumerate(item.articles):
        cleaned = cleansing(art)
        tokens = tokenize(cleaned)
        processed.append(" ".join(tokens))

    topic = lda_model(processed)
    return {"keywords": topic}
