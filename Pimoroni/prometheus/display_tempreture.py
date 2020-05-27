#!/usr/bin/env python

import time
import socket
from envirophat import weather
from microdotphat import write_string, set_decimal, clear, show
from prometheus_client import Gauge, start_http_server


def show_temperature(delay):
    clear()
    temp = weather.temperature()
    write_string( "%.2f" % temp + "c", kerning=False)
    show()
    time.sleep(delay)
    g.labels(host=host).set(temp)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)

    print("""Display Tempreture.

    Press Ctrl+C to exit.

    """)
    host = socket.gethostname()
    g = Gauge("pi_tempreture_celsius", "Temperature from envirophat", ['host'])

    try:
        while True:
            show_temperature(delay=1)

    except KeyboardInterrupt:
        pass
