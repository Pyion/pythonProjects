import time
import os
t = time.time()
input()
while 1:
    tc = time.time() - t
    os.system("clear")
    if(int(tc%60<10)):
        print(str(int(tc//60))+":0"+str(int(tc%60)))
    else:
        print(str(int(tc//60))+":"+str(int(tc%60)))
    time.sleep(1)
