from pydantic import BaseModel
from typing import Optional


class documento(BaseModel):
    id: Optional[str]
    titulo: Optional[str]
    autor: Optional[str]
    imagen: Optional[str]
    tipo: Optional[str]
    precio: Optional[str]
    stock: Optional[int]
    digital: Optional[bool]
