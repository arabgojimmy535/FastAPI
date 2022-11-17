from pydantic import BaseModel

class documento(BaseModel):
    titulo: str
    autor: str
    tipo: str
    precio: str
    fecha_publicacion: str
    vendido: str
    stock: str
    digital: str
