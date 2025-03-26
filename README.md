✨ 1. Arquitectura de Juego Multijugador en Línea en Tiempo Real

Este repositorio contiene el diseño técnico y arquitectural de un juego multijugador en línea en tiempo real basado en microservicios, con soporte para alta concurrencia, baja latencia y escalabilidad.

⚡ Arquitectura del Proyecto



✨ Características Principales

Alta concurrencia: Uso de WebSockets y Redis para minimizar latencia.

Tolerancia a fallos: Kubernetes con Auto Scaling y PostgreSQL con Multi-AZ.

Escalabilidad: Uso de microservicios desacoplados con balanceo de carga.

Seguridad: OAuth 2.0 con JWT, cifrado de datos y mitigación contra DDoS.

✨ 2. Pruebas de Caché en Python

Para verificar la eficiencia del almacenamiento en caché con Redis, se puede realizar una prueba en Python:

import redis
import time

# Conectar a Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Prueba de escritura y lectura
start_time = time.time()
r.set("test_key", "valor almacenado", ex=10)  # Clave con expiración de 10 segundos
value = r.get("test_key")
end_time = time.time()

print(f"Valor obtenido: {value}")
print(f"Tiempo de acceso: {end_time - start_time} segundos")

Esta prueba permite evaluar la latencia de acceso a Redis y su impacto en la optimización del juego.

✅ Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto

Hecho por Angela Anaya

