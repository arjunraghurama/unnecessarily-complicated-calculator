from api_server.main import divide
from api_server.schema import Operands


def test_divide():
    assert divide(Operands(a=4, b=2)) == {"result": 2}
