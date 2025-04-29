from machine import Pin
import time

sensor_izq = Pin(14, Pin.IN)  
sensor_der = Pin(27, Pin.IN)  

while True:
    izq = sensor_izq.value()
    der = sensor_der.value()

    if izq == 1 and der == 1:
        print("Dos activos")
    elif izq == 0 and der == 1:
        print("Derecho activo")
    elif izq == 1 and der == 0:
        print("Izquierdo activo")
    else:
        print("Ninguno activo")

    time.sleep(0.05)
