import uvicorn

from api import book_router, file_router, hero_router, team_router, tutorial_router
from core import app

app.include_router(hero_router)
app.include_router(team_router)
app.include_router(tutorial_router)
app.include_router(file_router)
app.include_router(book_router)


@app.get("/")
def hello():
    return {"msg": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
