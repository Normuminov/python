# app.py
import os

host = os.uname()[1]
user = os.getlogin()

def mainloop():
    try:
        cwd = os.getcwd()

        command = input(f"{user}@{host}:{cwd}$ ")
        os.system(command)
        mainloop()
    except KeyboardInterrupt:
        print('^C')
    except:
        print('Something went wrong')
        raise

mainloop()