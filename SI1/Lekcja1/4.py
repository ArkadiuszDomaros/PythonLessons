import random
import math
x = []
y = []

for i in range(10):
    x.append(random.randint(0,20))
    y.append(random.randint(0,20))

k = 0
l = 0
for i in range(10):
    k+= (x[i]*x[i])
    l+= (y[i]*y[i])
k = math.sqrt(k)
l = math.sqrt(l)

#iloczyn skalarny
il = 0
for i in range(10):
    il += x[i]*y[i]
print("Iloczyn: ", il)

#dlugosc wektorow
print("Dlugość wektora x: " + str(k) + " Długość wektora y: " + str(l))

#cosinus
cos = il/(k*l)
print("Cosinus kąta między wektorami: " + str(cos))

#radiany i stopnie
kat = math.acos(cos)
print("Radiany: " + str(kat))
print("Stopnie: " + str(kat * (180/3.14)))




