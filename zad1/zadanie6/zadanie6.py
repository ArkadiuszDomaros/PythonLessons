import os
import datetime

pliki = []
dict1 = dict()
dicttyg = dict()
dicttyg['suma'] = dict()

for x in os.scandir("D:\python\zad1\zadanie6\pliki"):
    if x.name.endswith(".csv") and x.is_file:
        pliki.append(x)

for i in pliki:
    check = 0
    for line in open(i):
        if check != 0:
            line = line.replace("\n", "")
            elem = line.split(",")
            if not dict1.__contains__(elem[0]):
                dict1[elem[0]] = 0
            e = elem[1].split(".")
            data = datetime.datetime(int(e[0]), int(e[1]), int(e[2]), int(e[3]), int(e[4]))
            dict1[elem[0]] += int(elem[2])
            if not dicttyg.__contains__(elem[0]):
                dicttyg[elem[0]] = dict()
            if not dicttyg['suma'].__contains__(data.strftime("%W")):
                dicttyg['suma'][data.strftime("%W")] = 0
            if not dicttyg[elem[0]].__contains__(data.strftime("%W")):
                dicttyg[elem[0]][data.strftime("%W")] = 0
            dicttyg[elem[0]][data.strftime("%W")] += int(elem[2])
            dicttyg['suma'][data.strftime("%W")] += int(elem[2])
        check += 1


suma = open("podsumowanie\\suma.txt", "w+", encoding="UTF-8")
for x in dict1:
    suma.write(x + ", ")
    suma.write(str(dict1[x]) + "\n")
suma.close()


cnt = [16,13]
i = 0
sred = open("podsumowanie\\srednianatydz.txt", "w+", encoding="UTF-8")
for week in dicttyg['suma']:
    sred.write(str(week) + ", " + str(dicttyg['suma'][week] / cnt[i]) + "\n")
    i+=1
sred.close()


napkt = open("podsumowanie\\sredniatygnapunkt.txt", "w+", encoding="UTF-8")
for pkt in dicttyg:
    if pkt != 'suma':
        napkt.write("Placowka nr: " + str(pkt) + " Tydzien 1: " +str(dicttyg[pkt]['38']/16) + "\n")
        napkt.write("Placowka nr: " + str(pkt) + " Tydzien 2: " + str(dicttyg[pkt]['39'] / 13) + "\n")
napkt.close()





