from fastapi import FastAPI
from .schema import Operands
from .logging.logger import logger
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs exactly once when the server boots up 
    logger.info("Calculator API Server started")
    yield
    # This runs exactly once when the server shuts down
    logger.info("Calculator API Server shutting down")

app = FastAPI(lifespan=lifespan)

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
