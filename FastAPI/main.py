from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def a():
    with open("C:\\Users\\User\\PycharmProjects\\Education\\FastAPI\\index.html", "r", encoding="utf-8") as a:
        b = a.read()
        return HTMLResponse(content=b)
