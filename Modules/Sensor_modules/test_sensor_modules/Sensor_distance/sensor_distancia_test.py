from machine import ADC, Pin
from time import sleep
import math

# Crear objeto ADC (puede variar el pin según la placa)
adc = ADC(Pin(36))  # En ESP32: GPIO36 (VP)
adc.atten(ADC.ATTN_11DB)  # Rango de voltaje hasta ~3.3V
adc.width(ADC.WIDTH_10BIT)  # Resolución de 10 bits: 0-1023

def leer_distancia():
    valor = adc.read()
    voltaje = valor * (3.3 / 1023)  # Convertir a voltaje
    try:
        # Fórmula empírica para GP2Y0A21YK0F
        distancia = 27.86 * math.pow(voltaje, -1.15)
    except:
        distancia = -1  # En caso de error matemático (división por cero, etc.)

    return voltaje, distancia

while True:
    volt, dist = leer_distancia()
    print("Voltaje: {:.2f} V | Distancia: {:.2f} cm".format(volt, dist))
    sleep(0.5)
