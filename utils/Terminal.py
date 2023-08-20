

from time import sleep
import sys

def terminal_write(text, time_sleep=0.008, endl=True):
    for _text_ in text:
        sys.stdout.write(_text_)
        sys.stdout.flush()
        sleep(time_sleep)
    if endl:
        print(' ')  
