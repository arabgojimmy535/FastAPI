def documentoEntidad(documento)-> dict:
    return {
        "id": documento["id"],
        "titulo": documento["titulo"],
        "autor": documento["autor"],
        "tipo": documento["tipo"],
        "precio": documento["precio"],
        "fecha_publicacion": documento["fecha_publicacion"], 
        "vendido": documento["vendido"],
        "stock": documento["stock"],
        "digital": documento["digital"]
    }

def documentosEntidad(documentos)-> list:
    [documentoEntidad(documento) for documento in documentos]