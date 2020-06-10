import psutil
import time

a = open("plik.txt","w")
a.write("")
a.close()


def memo():
    mem = psutil.virtual_memory().total
    truemem = mem/1024/1024/1024
    pid = psutil.pids()
    process = []
    plist = []
    for i in range(len(pid)):
        plist.append("")
    f = open("plik.txt","a")
    for i in range(len(pid)):
        process.append(psutil.Process(pid[i]))
        plist[i] = str(process[i].pid) + " " + str(process[i].name()) + " " + str(process[i].cpu_percent()) + " " + str(process[i].memory_percent())
        if process[i].memory_percent() > truemem/100 or process[i].cpu_percent() > 1:
            f.write(plist[i] + "\n")
    for i in plist:
        print(i)
    f.close()


while True:
    memo()
    time.sleep(60.0)



