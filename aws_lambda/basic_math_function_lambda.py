def handler(event, context):
    operation = event.get("operation")
    if not operation:
        return {"statusCode": 400, "body": "Operation not specified"}

    if operation == "add":
        a = event.get("a")
        b = event.get("b")
        return {"statusCode": 200, "body": a + b}
    elif operation == "subtract":
        a = event.get("a")
        b = event.get("b")
        return {"statusCode": 200, "body": a - b}
    elif operation == "multiply":
        a = event.get("a")
        b = event.get("b")
        return {"statusCode": 200, "body": a * b}
    elif operation == "divide":
        a = event.get("a")
        b = event.get("b")
        return {"statusCode": 200, "body": a / b}
    else:
        return {"statusCode": 400, "body": "Invalid operation"}
