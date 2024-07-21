from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home_page():
    return "home page"


@app.get("/main/")
def main_page():
    return "main page"
