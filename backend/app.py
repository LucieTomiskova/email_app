from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from backend.routes.user import router

templates = Jinja2Templates(directory=Path(__file__).parents[1] / 'templates')

app = FastAPI()

app.include_router(router, tags=["user"], prefix="/user/v1")


@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("form.html", {'request': request})
