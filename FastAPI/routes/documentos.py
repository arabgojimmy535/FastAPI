from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.documentos import documentoEntidad, documentosEntidad
from models.documentos import documento
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT
documentos = APIRouter()


@documentos.get("/documentos", response_model=list[documento], tags=["Documentos"])
def get_documentos():
    return documentosEntidad(conn.loslibros.documentos.find())


@documentos.get("/documentos/{id}", response_model=documento, tags=["Documentos"])
def get_documento(id: str):
    return documentoEntidad(conn.loslibros.documentos.find_one({"_id": ObjectId(id)}))


@documentos.post("/documentos", response_model=documento, tags=["Documentos"])
def post_documentos(documento: documento):
    nuevo_documento = dict(documento)
    del nuevo_documento["id"]
    id = conn.loslibros.documentos.insert_one(nuevo_documento).inserted_id
    documento = conn.loslibros.documentos.find_one({"_id": id})
    return documentoEntidad(documento)


@documentos.put("/documentos/{id}", response_model=documento, tags=["Documentos"])
def update_documento(id: str,documento: documento):
    documento= documento.dict()
    documento_updated= {}
    for llave in documento:
        if documento[llave]!=None:
            documento_updated[llave]=documento[llave]
    documentoEntidad(conn.loslibros.documentos.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": documento_updated}))
    return documentoEntidad(conn.loslibros.documentos.find_one({"_id": ObjectId(id)}))


@documentos.delete("/documentos/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Documentos"])
def delete_documento(id: str):
    documentoEntidad(
        conn.loslibros.documentos.find_one_and_delete({"_id": id}))
    return Response(status_code=HTTP_204_NO_CONTENT)
