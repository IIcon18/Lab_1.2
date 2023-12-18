#импортируем библиотеки
import wikipedia
from fastapi import *
from wikipedia import *
from pydantic import BaseModel

#активируем FastAPI
app = FastAPI()

#создаем класс для валидации данных
class SearchBody(BaseModel):
    section: str
    url: str


# запрос через query
@app.get("/wiki/search_query")
def search_query(section: str):
    try:
        return {"result": wikipedia.page(section).content}
    except PageError:
        raise HTTPException(status_code=404)


# запрос через path
@app.get("/wiki/search_path/{section}")
def search_path(section: str):
    try:
        return {"result": wikipedia.page(section).content}
    except PageError:
        raise HTTPException(status_code=404)


# параметр post
@app.post("/wiki/search_body")
def postBody(key: SearchBody):
    try:
        return{"result": wikipedia.page(key.section).html()}
    except PageError:
        raise HTTPException(status_code=404)