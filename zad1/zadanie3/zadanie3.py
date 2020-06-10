plik = open("a.csv")
l = plik.readline()
elem = l.replace("\n", "").split(";")
ilkom = 31
zbior = dict()
zbior["nazwaglowna"] = [0]*ilkom
zbior["suma"] = [0]*ilkom

for i in range(ilkom):
    zbior["nazwaglowna"][i] = elem[i+6]
for x in plik:
    el = x.split(";")
    if (not zbior.__contains__(el[0])):
        zbior[el[0]] = [0]*ilkom
    for y in range(ilkom):
        zbior[el[0]][y] += int(el[y+6])
        zbior["suma"][y] += int(el[y+6])
plik.close()

f = open("plik.txt","w", encoding="UTF-8")
for i in range(len(zbior["nazwaglowna"])):
    print(zbior["nazwaglowna"][i] + " Polska: " + str(zbior["suma"][i])  + " Dolnośląskie: " + str(zbior["dolnoÅ“lÂ¹skie"][i]) + " Kujawsko-Pomorskie: " + str(zbior["kujawsko-pomorskie"][i]) + " Lubelskie: " + str(zbior["lubelskie"][i]) + " Lubuskie: " + str(zbior["lubuskie"][i]) + " Łódzkie: " + str(zbior["Â³Ã³dzkie"][i]) + " Małopolskie: " + str(zbior["maÂ³opolskie"][i]) + " Mazowieckie: " + str(zbior["mazowieckie"][i]) + " Opolskie: " + str(zbior["opolskie"][i]) + " Podkarpackie: " + str(zbior["podkarpackie"][i]) + " Podlaskie: " + str(zbior["podlaskie"][i]) + " Pomorskie: " + str(zbior["pomorskie"][i]) + " Śląskie: " + str(zbior["Å“lÂ¹skie"][i]) + " Świętokrzyskie: " + str(zbior["Å“wiÃªtokrzyskie"][i]) + " Warmińsko-Mazurskie: " + str(zbior["warmiÃ±sko-mazurskie"][i]) + " Wielkopolskie: " + str(zbior["wielkopolskie"][i]) + " Zachodniopomorskie: " + str(zbior["zachodniopomorskie"][i]))
    f.write(zbior["nazwaglowna"][i] + " Polska: " + str(zbior["suma"][i])  + " Dolnośląskie: " + str(zbior["dolnoÅ“lÂ¹skie"][i]) + " Kujawsko-Pomorskie: " + str(zbior["kujawsko-pomorskie"][i]) + " Lubelskie: " + str(zbior["lubelskie"][i]) + " Lubuskie: " + str(zbior["lubuskie"][i]) + " Łódzkie: " + str(zbior["Â³Ã³dzkie"][i]) + " Małopolskie: " + str(zbior["maÂ³opolskie"][i]) + " Mazowieckie: " + str(zbior["mazowieckie"][i]) + " Opolskie: " + str(zbior["opolskie"][i]) + " Podkarpackie: " + str(zbior["podkarpackie"][i]) + " Podlaskie: " + str(zbior["podlaskie"][i]) + " Pomorskie: " + str(zbior["pomorskie"][i]) + " Śląskie: " + str(zbior["Å“lÂ¹skie"][i]) + " Świętokrzyskie: " + str(zbior["Å“wiÃªtokrzyskie"][i]) + " Warmińsko-Mazurskie: " + str(zbior["warmiÃ±sko-mazurskie"][i]) + " Wielkopolskie: " + str(zbior["wielkopolskie"][i]) + " Zachodniopomorskie: " + str(zbior["zachodniopomorskie"][i]) + "\n")
f.close()

