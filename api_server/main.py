from fastapi import FastAPI
from .schema import Operands
from .logging.logger import logger

app = FastAPI()

logger.info("Calculator API Server started")

@app.post("/add")
def add(operands: Operands):
    logger.info("Add operation requested")
    return {"result": operands.a + operands.b}

@app.post("/subtract")
def subtract(operands: Operands):
    logger.info("Subtract operation requested")
    return {"result": operands.a - operands.b}

@app.post("/multiply")
def multiply(operands: Operands):
    logger.info("Multiply operation requested")
    return {"result": operands.a * operands.b}

@app.post("/divide")
def divide(operands: Operands):
    logger.info("Divide operation requested")
    return {"result": operands.a / operands.b}
