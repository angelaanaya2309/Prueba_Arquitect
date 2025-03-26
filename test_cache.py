import redis

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

def test_cache_operations():
    """Prueba las operaciones de almacenamiento, recuperación y eliminación en la caché."""
    test_key = "test_key"
    test_value = "test_value"

    # Almacenar un valor en caché
    redis_client.set(test_key, test_value)
    assert redis_client.get(test_key) == test_value

    # Eliminar el valor y verificar que ya no existe
    redis_client.delete(test_key)
    assert redis_client.get(test_key) is None
