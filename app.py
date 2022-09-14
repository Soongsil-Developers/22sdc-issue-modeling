from typing import List

from fastapi import FastAPI
from model.LDA import lda_model
from pydantic import BaseModel
from utils.preprocessing import cleansing, tokenize


app = FastAPI()


class Item(BaseModel):
    articles: List[str]


with open("./stopwords-ko.txt", "r", encoding="utf-8") as f:
    stopwords = f.readlines()


@app.get("/")
async def hello():
    return {"message": "hello world"}


@app.post("/keyword")
async def keyword(item: Item):
    processed = []
    for num, art in enumerate(item.articles):
        cleaned = cleansing(art)
        tokens = tokenize(cleaned, stopwords)
        processed.append(" ".join(tokens))

    topic = lda_model(processed)
    return {"keywords": topic}
