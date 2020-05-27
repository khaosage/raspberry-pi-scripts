import os
import time
from microdotphat import write_string, set_decimal, clear, show


try:
    while True:
        clear()
        ts = os.popen('date +%s').read().split('\n')
        time.sleep(1)
        print(ts[0][-6:])
        write_string(ts[0][-6:], kerning=False)
        #write_string("TK-427", kerning=False)
        show()

except KeyboardInterrupt:
    pas
