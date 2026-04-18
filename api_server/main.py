from fastapi import FastAPI
from .schema import Operands
from .logging.logger import logger
from contextlib import asynccontextmanager
import boto3
import json
import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs exactly once when the server boots up
    logger.info("Calculator API Server started")
    yield
    # This runs exactly once when the server shuts down
    logger.info("Calculator API Server shutting down")


app = FastAPI(lifespan=lifespan)

endpoint_url = (
    "http://ministack:4566"
    if os.getenv("ENVIRONMENT") == "test"
    else "http://localhost:4566"
)

lambda_client = boto3.client(
    "lambda",
    endpoint_url=endpoint_url,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)


@app.post("/add")
def add(operands: Operands):
    logger.info("Add operation requested")
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "add", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())
    return {"result": result["body"]}


@app.post("/subtract")
def subtract(operands: Operands):
    logger.info("Subtract operation requested")
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "subtract", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())
    return {"result": result["body"]}


@app.post("/multiply")
def multiply(operands: Operands):
    logger.info("Multiply operation requested")
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "multiply", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())
    return {"result": result["body"]}


@app.post("/divide")
def divide(operands: Operands):
    logger.info("Divide operation requested")
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "divide", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())
    return {"result": result["body"]}
