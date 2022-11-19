from pydantic import BaseModel
from typing import Optional

class cliente(BaseModel):
    id: Optional[str]
    nombres: Optional[str]
    apellidos: Optional[str]
    usuario: Optional[str]
    email: Optional[str]
    contraseña: Optional[str]
    publicaciones: Optional[dict]
    compras: Optional[dict]
