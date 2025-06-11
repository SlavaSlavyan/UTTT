import subprocess
import time

VERS = "2.13.14 DEV"

loading = subprocess.Popen(['python', 'function\\loading.py'])
time.sleep(1)

from function.Main import Main

UTTT = Main(VERS)

loading.terminate()

while True:
    
    UTTT.main()