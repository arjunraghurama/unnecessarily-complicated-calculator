from pydantic import BaseModel


class Operands(BaseModel):
    a: int
    b: int