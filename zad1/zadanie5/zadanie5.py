import os
import datetime
import shutil
a = os.getcwd()
pat = os.listdir(a + "\\a")
list = "\n".join(str(x) for x in pat)
f = open("path.txt", "w").write(list)

nowy = os.path.join(a + '\\b\\',datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))
os.mkdir(nowy)

for root, dirs, files in os.walk(a + '\\a\\'):
   for file in files:
      path_file = os.path.join(root, file)
      shutil.copy2(path_file,nowy)
