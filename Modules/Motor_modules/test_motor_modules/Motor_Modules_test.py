from machine import Pin
import time

in1 = Pin(5, Pin.OUT)   
in2 = Pin(4, Pin.OUT)   

def motor_adelante():
    in1.on()
    in2.off()
    print("Motor girando hacia adelante")

def motor_atras():
    in1.off()
    in2.on()
    print("Motor girando hacia atrás")

def motor_parar():
    in1.off()
    in2.off()
    print("Motor detenido")

# Prueba básica
while True:
    motor_adelante()
    time.sleep(2)
    motor_atras()
    time.sleep(2)
    motor_parar()
    time.sleep(2)
