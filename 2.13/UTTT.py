import subprocess

VERS = "2.13.15 DEV"

loading = subprocess.Popen(['python', 'function\\loading.py'])

from function.Main import Main

UTTT = Main(VERS)

loading.terminate()

while True:
    
    UTTT.main()