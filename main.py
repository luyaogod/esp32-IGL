from ubluetooth import BLE
from machine import Pin

led = Pin(2,Pin.OUT)

ble = BLE()
ble.active(True)

def advertise():
    ble.gap_advertise(100,adv_data = b'\x02\x01\x06\x1A\xFF\x4C\x00\x02\x15\xFD\xA5\x06\x93\xA4\xE2\x4F\xB1\xAF\xCF\xC6\xEB\x07\x64\x78\x25\x27\xDA\x42\x72\xC5')

advertise()

def ble_irq(event, data):
    if event == 1:
        led.on()
        advertise()
    elif event == 2:
        led.off()
        advertise()
        
ble.irq(ble_irq)


