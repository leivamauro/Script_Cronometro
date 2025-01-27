# Cronómetro en Python

Este script proporciona una implementación simple de un cronómetro utilizando perf_counter de la librería `time` de Python. El cronómetro permite iniciar, pausar, reiniciar y obtener el tiempo transcurrido.

## Funcionalidades

La clase `Crono` ofrece las siguientes funcionalidades:

- **Iniciar el cronómetro (`start`)**: Inicia o reanuda el cronómetro si estaba pausado.
- **Pausar el cronómetro (`pause`)**: Detiene el cronómetro temporalmente, registrando el tiempo pausado.
- **Reiniciar el cronómetro (`restart`)**: Restablece el cronómetro a su estado inicial.
- **Obtener el tiempo (`get_time`)**: Devuelve el tiempo transcurrido en segundos desde que se inició el cronómetro, teniendo en cuenta el tiempo pausado.
- **Obtener el tiempo (`get_time_in_HHMMSSms`)**: Devuelve el tiempo transcurrido en una cadena de horas, minutos, segundos y milisegundos (00:00:00.000) desde que se inició el cronómetro, teniendo en cuenta el tiempo pausado.

## Uso

### Ejemplo de uso básico:

```python
from time import sleep

# Crear instancia del cronómetro
mi_crono = Crono()

# Iniciar cronómetro
mi_crono.start()

# Pausar cronómetro después de unos segundos
mi_crono.pause()

# Obtener el tiempo transcurrido
print(mi_crono.get_time())

# Reiniciar el cronómetro
mi_crono.restart()

# Iniciar nuevamente
mi_crono.start()

# Pausar nuevamente
mi_crono.pause()

# Obtener el tiempo final
print(mi_crono.get_time())

# Obtener el tiempo cada cierto intervalo
while True:
    if mi_crono.get_is_running is True:
        print(mi_crono.get_time())
    sleep(10)
