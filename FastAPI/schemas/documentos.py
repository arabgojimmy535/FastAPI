def documentoEntidad(documento)-> dict:
    return {
        "id": str(documento["_id"]),
        "titulo": documento["titulo"],
        "autor": documento["autor"],
        "imagen": documento["imagen"],
        "tipo": documento["tipo"],
        "precio": documento["precio"],
        "stock": documento["stock"],
        "digital": documento["digital"]
    }

def documentosEntidad(documentos)-> list:
    return [documentoEntidad(documento) for documento in documentos]