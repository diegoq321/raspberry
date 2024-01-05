import sys
import tensorflow as tf

# Ruta al modelo preentrenado
ruta_modelo = "/homeassistant/models/disp.h5"

# Obtener los argumentos de la línea de comandos
argumentos = sys.argv[1:]

# Cargar el modelo
modelo = tf.keras.models.load_model(ruta_modelo)

# Realizar una predicción (ajustar según las necesidades de tu modelo)
# Este es solo un ejemplo de cómo podrías usar los argumentos
entrada_modelo = [float(arg) for arg in argumentos]
prediccion = modelo.predict([entrada_modelo])

# Umbral para tomar decisiones (ajustar según tus necesidades)
umbral = 0.8

# Ejemplo: si la predicción es mayor que el umbral, realizar alguna acción
if prediccion > umbral:
    # Acción en Home Assistant (por ejemplo, encender luces)
    service.call("light", "turn_on", {"entity_id": "light.tu_luz"})