from fastapi import APIRouter
from config.db import conn
from schemas.documentos import documentoEntidad,documentosEntidad
from models.documentos import documento
documentos= APIRouter()

@documentos.get("/documentos")
def get_documentos():
    return documentosEntidad(conn.loslibros.documentos.find())


@documentos.post("/documentos")
def post_documentos(documento: documento):
    nuevo_documento= dict(documento)
    id= conn.loslibros.documentos.insert_one(nuevo_documento).inserted_id
    documento= conn.loslibros.documentos.find_one({"_id": id})
    return documentoEntidad(documento)
