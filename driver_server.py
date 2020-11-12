import subprocess

#subp = subprocess.Popen("./run_server.sh")

d = input("Enter duration of the server process:") 
#subp = subprocess.run("python test_server.py", shell=False, check=True)
subp = subprocess.Popen(['python', 'test_server.py'],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
import psutil
import sys

duration = int(d)
p = psutil.Process(subp.pid)

print("process id:"+ str(subp.pid))

try:
    p.wait(timeout=duration)
except psutil.TimeoutExpired:
    print("Terminating process")
    sys.exit(0)

