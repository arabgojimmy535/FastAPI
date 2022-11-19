def clienteEntidad(cliente) -> dict:
    return{
        "id": str(cliente["_id"]),
        "nombres": cliente["nombres"],
        "apellidos": cliente["apellidos"],
        "usuario": cliente["usuario"],
        "email": cliente["email"],
        "contraseña": cliente["contraseña"],
        "publicaciones": cliente["publicaciones"],
        "compras": cliente["compras"]
    }

def clientesEntidad(clientes) -> list:
    return [clienteEntidad(cliente) for cliente in clientes]