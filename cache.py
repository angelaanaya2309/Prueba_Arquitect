import redis
import time
from fastapi import FastAPI
from pydantic import BaseModel

# Configuración de Redis
# Se establece la conexión con el servidor Redis local.
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# Inicializar la aplicación FastAPI
app = FastAPI()

class CacheItem(BaseModel):
    """Modelo de datos para un elemento de caché.
    Atributos:
        key (str): Clave única del elemento en la caché.
        value (str): Valor asociado a la clave.
        ttl (int, opcional): Tiempo de vida en segundos antes de la expiración del dato.
    """
    key: str
    value: str
    ttl: int = None  # Tiempo de vida opcional en segundos

@app.post("/cache/")
def set_cache(item: CacheItem):
    """Almacena un valor en la caché con una clave única y un TTL opcional.
    Si se proporciona un TTL, el valor expirará automáticamente después del tiempo indicado.
    """
    if item.ttl:
        redis_client.setex(item.key, item.ttl, item.value)
    else:
        redis_client.set(item.key, item.value)
    return {"message": "Dato almacenado", "key": item.key}

@app.get("/cache/{key}")
def get_cache(key: str):
    """Recupera un valor almacenado en la caché usando su clave.
    Devuelve un mensaje si la clave no se encuentra en la caché.
    """
    value = redis_client.get(key)
    if value is None:
        return {"message": "Clave no encontrada"}
    return {"key": key, "value": value}

@app.delete("/cache/{key}")
def delete_cache(key: str):
    """Elimina un elemento de la caché utilizando su clave.
    Retorna un mensaje confirmando la eliminación.
    """
    redis_client.delete(key)
    return {"message": "Clave eliminada", "key": key}