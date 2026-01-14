import time
import subprocess
import sys

sys.argv.append("2.14.6 DEV")

loading_screen = subprocess.Popen(["python", "src\\main\\loading.py", "LOADING"])
time.sleep(0.5)

from src.main.program import Program

Program = Program()
loading_screen.kill()
Program.start()