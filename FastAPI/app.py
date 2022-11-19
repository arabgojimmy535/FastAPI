from fastapi import FastAPI
from routes.documentos import documentos
from routes.clientes import clientes
app= FastAPI(
    title= "FASTAPI GESTION DE DOCUMENTOS",
    version=1.0
)

app.include_router(documentos)
app.include_router(clientes)

