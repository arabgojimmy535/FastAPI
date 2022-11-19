from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.clientes import clienteEntidad,clientesEntidad
from models.clientes import cliente
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

clientes = APIRouter()

@clientes.get("/clientes")
def get_clientes():
    return clientesEntidad(conn.loslibros.clientes.find())

@clientes.get("/clientes/{id}")
def get_cliente(id:str):
    return clienteEntidad(conn.loslibros.clientes.find_one({"_id": ObjectId(id)}))

@clientes.post("/clientes")
def post_cliente(cliente: cliente):
    nuevo_cliente = dict(cliente)
    id=conn.loslibros.clientes.insert_one(nuevo_cliente).inserted_id
    cliente= conn.loslibros.clientes.find_one({"_id": id})
    return clienteEntidad(cliente)

@clientes.put("/clientes/{id}")
def update_cliente(id:str, cliente:cliente):
    cliente= dict(cliente)
    cliente_update={}
    for llave in cliente:
        if cliente[llave]!=None:
            cliente_update[llave]= cliente[llave]
    clienteEntidad(conn.loslibros.clientes.find_one_and_update({"_id": ObjectId(id)},{"$set": cliente_update}))
    return clienteEntidad(conn.loslibros.clientes.find_one({"_id": ObjectId(id)}))

@clientes.delete("/clientes/{id}")
def delete_clientes(id:str):
    print(clienteEntidad(conn.loslibros.clientes.find_one_and_delete({"_id": ObjectId(id)})))
    
    return Response(status_code= HTTP_204_NO_CONTENT)

