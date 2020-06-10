import numpy
import random

x = []
#wypelnij randomowymi
for i in range(30):
    x.append(random.randint(0,100))

x.sort()
#wypisz najwieksza i najmniejsza
print(x[0])
print(x[29])

k = 0
#wypisz posortowana
print(x)
for i in range(len(x)):
    k += x[i]
#srednia
avg = k/30
print(avg)

#odchylenie standardowe
od = 0
for i in range(len(x)):
    od += x[i]-avg
trueod = od/30
print(trueod)

#wektor znormalizowany
z = []
for i in range(len(x)):
    z.append((x[i]-x[0])/(x[29]-x[0]))
print(z)

#wektor standaryzowany
stan = []
for i in range(len(x)):
    stan.append((x[i]-avg)/trueod)
print(stan)




