from machine import Pin, time_pulse_us
import time

TRIG = Pin(5, Pin.OUT)  
ECHO = Pin(18, Pin.IN)  

def medir_distancia():
    TRIG.value(0)
    time.sleep_us(2)
    TRIG.value(1)
    time.sleep_us(10)
    TRIG.value(0)

    duracion = time_pulse_us(ECHO, 1, 30000) 
    if duracion < 0:
        print("Tiempo excedido")
        return None

    distancia = (duracion / 2) / 29.1
    return distancia

while True:
    dist = medir_distancia()
    if dist:
        print("Distancia: {:.2f} cm".format(dist))
    else:
        print("Error al medir")
    time.sleep(1)
