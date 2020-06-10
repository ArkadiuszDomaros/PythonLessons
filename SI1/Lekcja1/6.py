import random
import matplotlib.pyplot as pl
import numpy as np
x = []
#wypelnij randomowymi
for i in range(100):
    x.append(random.randint(0,20))

y = []
for i in range(20):
    y.append(0)

for i in range(20):
    for j in range(len(x)):
        if i == x[j]:
            y[i]+=1

print(x)
print(y)
z = []
k=0
for i in range(20):
    z.append(k)
    k+=1

print(z)

number = 20

il = np.arange(number)
width = 0.30

p1 = pl.bar(il, y, width)
pl.xticks(il, z)
pl.yticks(il, z)
pl.show()

