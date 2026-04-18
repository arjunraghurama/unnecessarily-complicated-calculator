import boto3, json, zipfile, io


def push_code_to_lambda(lambda_client):
    basic_math_function_lambda_code = ""
    with open("basic_math_function_lambda.py", "r") as f:
        basic_math_function_lambda_code = f.read()

    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w") as zf:
        zf.writestr("basic_math_function_lambda.py", basic_math_function_lambda_code)

    lambda_client.create_function(
        FunctionName="basic-math-lambda-function",
        Runtime="python3.12",
        Role="arn:aws:iam::000000000000:role/fake-role",
        Handler="basic_math_function_lambda.handler",
        Code={"ZipFile": zip_buffer.getvalue()},
    )


def validate_result(lambda_client):
    response = lambda_client.invoke(
        FunctionName="basic-math-lambda-function",
        Payload=json.dumps({"operation": "add", "a": 1, "b": 2}),
    )
    result = json.loads(response["Payload"].read())
    assert result == {"statusCode": 200, "body": 3}


def main():
    lambda_client = boto3.client(
        "lambda",
        endpoint_url="http://ministack:4566",
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name="us-east-1",
    )

    push_code_to_lambda(lambda_client=lambda_client)
    validate_result(lambda_client=lambda_client)


if __name__ == "__main__":
    main()
