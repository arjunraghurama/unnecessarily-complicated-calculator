from fastapi import FastAPI
from .schema import Operands

app = FastAPI()

@app.post("/add")
def add(operands: Operands):
    return {"result": operands.a + operands.b}

@app.post("/subtract")
def subtract(operands: Operands):
    return {"result": operands.a - operands.b}

@app.post("/multiply")
def multiply(operands: Operands):
    return {"result": operands.a * operands.b}

@app.post("/divide")
def divide(operands: Operands):
    return {"result": operands.a / operands.b}
