from fastapi import FastAPI
from routes.documentos import documentos
app= FastAPI()

app.include_router(documentos)

