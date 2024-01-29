from fastapi import FastAPI

from fastapi_and_babel.translator import FastAPIAndBabel

app = FastAPI()
translator = FastAPIAndBabel(app, "de", "messages")


@app.get("/")
def index():
    return {"text": translator.gettext("Hello World!")}
