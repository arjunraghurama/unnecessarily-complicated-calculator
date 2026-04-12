from api_server.main import add
from api_server.schema import Operands


def test_add():
    assert add(Operands(a=1, b=2)) == {"result": 3}
