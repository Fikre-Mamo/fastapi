from fastapi import FastAPI, Body, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}