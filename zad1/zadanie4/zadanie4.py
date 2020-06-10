import datetime
import os.path
import subprocess as sp

nazwa = os.path.join(os.getcwd(),datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".txt"
programName = "notepad.exe"
process = sp.Popen([programName, nazwa])

f = open(nazwa,"w")
f.close()
process.wait()

count = len(open(nazwa, 'r').readlines())

if count == 0:
    g = open("puste.txt", "a+").write(nazwa + "\n")
elif count == 1:
    g = open("krótkie.txt", "a+").write(nazwa + "\n")
elif count > 1 and count < 10:
    g = open("srednie.txt", "a+").write(nazwa + "\n")
else:
    g = open("długie.txt", "a+").write(nazwa + "\n")





