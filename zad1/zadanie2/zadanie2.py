class Tablica:

    def __init__(self, tab):
        self.tab = tab

    def dodawanieMac(self, doDod):
        x = 0
        y = 0
        for i in self.tab:
            y = 0
            for i in self.tab:
                self.tab[x][y] += doDod[x][y]
                y += 1
            x += 1
        print(self.tab)

    def mnozenieMac(self, doMn):
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for k in range(0, 3):
            for i in range(0, 3):
                result[i][k] = self.tab[i][0] * doMn[0][k] + self.tab[i][1] * doMn[1][k] + self.tab[i][2] * doMn[2][k]
                i += 1
            k += 1
        print(result)

    def wyznacznik(self):
        wyz = self.tab[0][0] * self.tab[1][1] * self.tab[2][2] + self.tab[0][1] * self.tab[1][2] * self.tab[2][0] + \
              self.tab[1][0] * self.tab[2][1] * self.tab[0][2] - self.tab[2][0] * self.tab[1][1] * self.tab[0][2] - \
              self.tab[1][0] * self.tab[0][1] * self.tab[2][2] - self.tab[0][0] * self.tab[2][1] * self.tab[1][2]
        print(wyz)


tab1 = [[1, 2, 4],
        [3, 5, 2],
        [4, 1, 5]]
tab2 = [[2, 1, 3],
        [2, 4, 5],
        [1, 3, 1]]

newTab = Tablica(tab1)
newTab.wyznacznik()
newTab.mnozenieMac(tab2)
newTab.dodawanieMac(tab2)