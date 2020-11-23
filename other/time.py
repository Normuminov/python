# time.py

try:
    from datetime import time, datetime
    from time import sleep

    def main():
        now = datetime.now().strftime("%H:%M:%S")

        print('\r' + now, end='')

    while True:
        main()
        sleep(1)
except KeyboardInterrupt:
    pass
except:
    print("Something went wrong")
    raise

