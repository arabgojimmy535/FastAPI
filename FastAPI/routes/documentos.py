from fastapi import APIRouter
from config.db import conn
from schemas.documentos import documentoEntidad,documentosEntidad
documentos= APIRouter()

@documentos.get("/documentos")
def get_documentos():
    return "estamos melos"
