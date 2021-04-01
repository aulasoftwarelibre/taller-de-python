# Tiempo, fechas y horas: `time`, `datetime`, `calendar`

A menudo necesitamos utilidades para calcular tiempos, horas, fechas, etc. En Python lo tenemos muy fácil gracias a estos tres módulos.

Las funciones del módulo `time` están relacionadas con tiempos de espera y tiempos de cómputo. Por ejemplo, `time.perf_counter()` mide tiempo real, incluyendo tiempo de inactividad. Sólo tiene sentido si calculamos una *diferencia entre dos llamadas*:
```python
import time
import math

inicio = time.perf_counter()  # Empezamos el "cronómetro"

fact = math.factorial(100000)  # Cálculo largo
print(str(fact)[:10])  # Primeros 10 dígitos
# >> 2824229407
fin_factorial = time.perf_counter()  # Fin del cálculo largo
time.sleep(1)  # Ahora un segundo de inactividad

fin = time.perf_counter()  # Paramos el "cronómetro"

print(f'Tiempo de cálculo: {fin_factorial - inicio:.2f} segundos')
print(f'Tiempo total: {fin - inicio:.2f} segundos')
# >> Tiempo de cálculo: 2.38 segundos
# >> Tiempo total: 3.38 segundos
```

Por otro lado, `time.process_time()` mide tiempo *de proceso*, sin incluir el tiempo que el proceso está inactivo (por ejemplo, esperando a que el usuario introduzca algún valor o esperando a algún dispositivo de E/S):
```python
import time
import math

inicio = time.process_time()  # Empezamos el "cronómetro"

fact = math.factorial(100000)  # Cálculo largo
print(str(fact)[:10])  # Primeros 10 dígitos
# >> 2824229407
fin_factorial = time.process_time()  # Fin del cálculo largo
time.sleep(1)  # Ahora un segundo de inactividad

fin = time.process_time()  # Paramos el "cronómetro"

print(f'Tiempo de cálculo: {fin_factorial - inicio:.2f} segundos')
print(f'Tiempo total: {fin - inicio:.2f} segundos')
# >> Tiempo de cálculo: 2.44 segundos
# >> Tiempo total: 2.45 segundos
```

!!! info "Información"
    La pequeña discrepancia en el tiempo de cálculo y tiempo total del último ejemplo se debe a que la propia llamada a `time.sleep(1)`, así como `time.process_time()`, tiene cierta *sobrecarga*.

Podemos usar `datetime` para lidiar con fechas y horas del "mundo real":
```python
from datetime import datetime

# Mi fecha de nacimiento
nacimiento = datetime(1995, 4, 22, 6, 0)
print(nacimiento.weekday())  # ¿Qué día de la semana? (0 = lunes)
# >> 5

# ¿Cuántos años tengo? (datetime - datetime = timedelta)
td = datetime.now() - nacimiento
print(td)
# >> 9473 days, 13:30:38.442574
print(td.days // 365)
# >> 25
print(td.total_seconds())
# >> 818515838.442574
```

Por último `calendar` contiene utilidades relacionadas con calendarios: años bisiestos, nombres de los meses/días de la semana...
```python
import calendar

# Para configurar la localización de fecha/hora a España,
# tenemos que ejecutar lo siguiente:
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


nombre_dia_semana = calendar.day_name[nacimiento.weekday()]
nombre_dia_mes = calendar.month_name[nacimiento.month]
print(f'Nací un {nombre_dia_semana}, {nacimiento.day} de {nombre_dia_mes} de {nacimiento.year}')
# >> Nací un sábado, 22 de abril de 1995
```

!!! warning "Cuidado"
    Si tu aplicación necesita gestionar más de una localización (p. ej.: español de España y español de México) se desaconseja el uso de `locale.setlocale()`. Este es sólo un pequeño ejemplo.
    
