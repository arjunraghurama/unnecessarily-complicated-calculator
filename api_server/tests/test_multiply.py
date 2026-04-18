from api_server.main import multiply
from api_server.schema import Operands


def test_multiply():
    assert multiply(Operands(a=2, b=3)) == {"result": 6}
