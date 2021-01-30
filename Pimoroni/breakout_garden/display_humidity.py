#!/usr/bin/env python


import time
from ltp305 import LTP305

try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

print("""collect humidity with bme280 and display with ltp305

Press Ctrl+C to exit!

""")

display = LTP305(0x61)


# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

while True:
    humidity = str(int(bme280.get_humidity()))
    print(humidity)
    left, right = humidity
    display.set_character(0, left)
    display.set_character(5, right)
    display.show()
    time.sleep(1)