import logging
import logging_loki

handler = logging_loki.LokiHandler(
    url="http://loki:3100/loki/api/v1/push",
    tags={"app": "calculator-api-server"},
    version="2"
)

logger = logging.getLogger("calculator-api-server")
# Also attach the loki handler to uvicorn access logs
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.addHandler(handler)

logger.addHandler(handler)