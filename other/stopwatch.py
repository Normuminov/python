# stopwatch.py

from time import sleep

def display(hours, minutes, seconds):
    print('\r%s:%s:%s' % (hours, minutes, seconds), end='')

hours = 0
minutes = 0
seconds = 0

while(True):
    display(hours, minutes, seconds)

    seconds += 1

    if(seconds == 60):
        minutes += 1
        seconds = 0

    if(minutes == 60):
        hours += 1
        minutes = 0
        seconds = 0

    sleep(1)

