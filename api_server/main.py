from fastapi import FastAPI
from .schema import Operands
from .log.logger import logger
from contextlib import asynccontextmanager
import boto3
import json
import os
import valkey

@asynccontextmanager
async def lifespan(app: FastAPI):
    # This runs exactly once when the server boots up
    logger.info("Calculator API Server started")
    yield
    # This runs exactly once when the server shuts down
    logger.info("Calculator API Server shutting down")


app = FastAPI(lifespan=lifespan)

if os.getenv("ENVIRONMENT") == "test":
    endpoint_url = "http://localhost:4566"
    valkey_endpoint = "localhost"
else:
    endpoint_url = "http://ministack:4566"
    valkey_endpoint = "valkey"

lambda_client = boto3.client(
    "lambda",
    endpoint_url=endpoint_url,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1",
)

cache_client = valkey.Valkey(host=valkey_endpoint, port=6379, db=0)

@app.post("/add")
def add(operands: Operands):
    logger.info("Add operation requested")
    
    # check if result is already in cache
    if cache_client.exists(f"add_{operands.a}_{operands.b}"):
        logger.info(f"Result found in cache for add operation {operands.a} + {operands.b}")
        return {"result": int(cache_client.get(f"add_{operands.a}_{operands.b}"))}
    
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "add", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())

    # store result in cache with timeout of 10 minutes
    cache_client.set(f"add_{operands.a}_{operands.b}", result["body"], ex=600)
    logger.info(f"Result {result['body']} stored in cache for add operation {operands.a} + {operands.b}")
    return {"result": result["body"]}


@app.post("/subtract")
def subtract(operands: Operands):
    logger.info("Subtract operation requested")

    # check if result is already in cache
    if cache_client.exists(f"subtract_{operands.a}_{operands.b}"):
        logger.info(f"Result found in cache for subtract operation {operands.a} - {operands.b}")
        return {"result": int(cache_client.get(f"subtract_{operands.a}_{operands.b}"))}

    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "subtract", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())

    # store result in cache with timeout of 10 minutes
    cache_client.set(f"subtract_{operands.a}_{operands.b}", result["body"], ex=600)
    logger.info(f"Result {result['body']} stored in cache for subtract operation {operands.a} - {operands.b}")
    return {"result": result["body"]}


@app.post("/multiply")
def multiply(operands: Operands):
    logger.info("Multiply operation requested")

    # check if result is already in cache
    if cache_client.exists(f"multiply_{operands.a}_{operands.b}"):
        logger.info(f"Result found in cache for multiply operation {operands.a} * {operands.b}")
        return {"result": int(cache_client.get(f"multiply_{operands.a}_{operands.b}"))}

    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "multiply", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())

    # store result in cache with timeout of 10 minutes
    cache_client.set(f"multiply_{operands.a}_{operands.b}", result["body"], ex=600)
    logger.info(f"Result {result['body']} stored in cache for multiply operation {operands.a} * {operands.b}")
    return {"result": result["body"]}


@app.post("/divide")
def divide(operands: Operands):
    logger.info("Divide operation requested")

    # check if result is already in cache
    if cache_client.exists(f"divide_{operands.a}_{operands.b}"):
        logger.info(f"Result found in cache for divide operation {operands.a} / {operands.b}")
        return {"result": float(cache_client.get(f"divide_{operands.a}_{operands.b}"))}

    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "divide", "a": operands.a, "b": operands.b}),
    )
    logger.info(f"Lambda response: {response}")
    result = json.loads(response["Payload"].read())

    # store result in cache with timeout of 10 minutes
    cache_client.set(f"divide_{operands.a}_{operands.b}", result["body"], ex=600)
    logger.info(f"Result {result['body']} stored in cache for divide operation {operands.a} / {operands.b}")
    return {"result": result["body"]}
