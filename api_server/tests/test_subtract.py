from api_server.main import subtract
from api_server.schema import Operands


def test_subtract():
    assert subtract(Operands(a=4, b=2)) == {"result": 2}