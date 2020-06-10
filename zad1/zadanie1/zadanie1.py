class Element:
    def __init__(self, wartosc, nastEl=None):
        self.wartosc = wartosc
        self.nastEl = nastEl

    def setWart(self, nowaWart):
        self.wartosc = nowaWart

    def getWart(self):
        return self.wartosc

    def setNastEl(self, nastElem):
        self.nastEl = nastElem

    def getNastEl(self):
        return self.nastEl

    def delNast(self):
        self.nastEl = None


class Stos:
    def __init__(self, rt=None):
        self.root = rt
        self.ilElem = 0

    def dodajElem(self, nowy):
        if self.root == None:
            self.root = nowy
        else:
            tmprt = self.root
            while (tmprt.getNastEl() != None):
                tmprt = tmprt.getNastEl()
            tmprt.setNastEl(nowy)
        self.ilElem += 1

    def wierzchStosu(self):
        if self.ilElem == 0:
            print('Stos jest pusty')
        else:
            tmprt = self.root
            i = 0
            while (i < self.ilElem - 1):
                tmprt = tmprt.getNastEl()
                i += 1
            return tmprt.getWart()

    def wysokosc(self):
        return self.ilElem

    def usunEl(self):
        if self.ilElem == 0:
            print('Brak elementow do usuniecia')
        elif self.ilElem == 1:
            wartosc = self.root.getWart()
            self.root = None
            self.ilElem = 0
            return wartosc
        else:
            tmprt = self.root
            i = 0
            while (i < self.ilElem - 1):
                tmprt = tmprt.getNastEl()
                i += 1
            wartosc = tmprt.getWart()
            tmprt.delNast()
            self.ilElem -= 1
            return wartosc


mojStos = Stos()
element1 = Element(4)
element2 = Element(5)
element3 = Element(3)
element4 = Element(1)

mojStos.dodajElem(element1)
mojStos.dodajElem(element2)
mojStos.dodajElem(element3)
mojStos.dodajElem(element4)

print(mojStos.wierzchStosu())
print(mojStos.wysokosc())
print(mojStos.usunEl())
print('---------------------')
print(mojStos.wierzchStosu())
print(mojStos.wysokosc())
print(mojStos.usunEl())
print('---------------------')
print(mojStos.wierzchStosu())
print(mojStos.wysokosc())
print(mojStos.usunEl())
print('---------------------')
print(mojStos.wierzchStosu())
print(mojStos.wysokosc())
print(mojStos.usunEl())
print('---------------------')
print(mojStos.wierzchStosu())
print(mojStos.wysokosc())
print(mojStos.usunEl())








