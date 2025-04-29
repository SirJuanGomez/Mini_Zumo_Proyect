import machine as mch 
import time

ir_pin=mch.Pin(14,mch.Pin.IN)

print("Esperando señal IR...")

def leer_pulsos_ir(pin):
    timestamp = time.ticks_us()
    estado = pin.value()
    print("Cambio detectado: Estado =", estado, "Tiempo =", timestamp)

ir_pin.irq(trigger=mch.Pin.IRQ_RISING | mch.Pin.IRQ_FALLING, handler=leer_pulsos_ir)

while True:
    time.sleep(1)
