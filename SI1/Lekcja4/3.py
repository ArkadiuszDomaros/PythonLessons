from pyeasyga import pyeasyga
import time
import matplotlib.pyplot as plt

data = [{'name': 'box1', 'value': 19, 'weight': 18},
         {'name': 'box2', 'value': 39, 'weight': 46},
         {'name': 'box3', 'value': 30, 'weight': 15},
         {'name': 'box4', 'value': 40, 'weight': 41},
         {'name': 'box5', 'value': 23, 'weight': 31},
         {'name': 'box6', 'value': 16, 'weight': 30},
         {'name': 'box7', 'value': 14, 'weight': 32},
         {'name': 'box8', 'value': 38, 'weight': 42},
         {'name': 'box9', 'value': 11, 'weight': 32},
         {'name': 'box10', 'value': 37, 'weight': 11}]

data2 = [{'name': 'box1', 'value': 42, 'weight': 50},
        {'name': 'box2', 'value': 50, 'weight': 46},
        {'name': 'box3', 'value': 34, 'weight': 30},
        {'name': 'box4', 'value': 44, 'weight': 21},
        {'name': 'box5', 'value': 18, 'weight': 34},
        {'name': 'box6', 'value': 27, 'weight': 41},
        {'name': 'box7', 'value': 21, 'weight': 43},
        {'name': 'box8', 'value': 12, 'weight': 35},
        {'name': 'box9', 'value': 31, 'weight': 7},
        {'name': 'box10', 'value': 25, 'weight': 29},
        {'name': 'box1', 'value': 34, 'weight': 41},
        {'name': 'box2', 'value': 50, 'weight': 2},
        {'name': 'box3', 'value': 32, 'weight': 14},
        {'name': 'box4', 'value': 29, 'weight': 10},
        {'name': 'box5', 'value': 36, 'weight': 12},
        {'name': 'box6', 'value': 6, 'weight': 34},
        {'name': 'box7', 'value': 11, 'weight': 45},
        {'name': 'box8', 'value': 40, 'weight': 6},
        {'name': 'box9', 'value': 36, 'weight': 47},
        {'name': 'box10', 'value': 25, 'weight': 6}]

data3 = [{'name': 'box1', 'value': 88, 'weight': 55},
         {'name': 'box2', 'value': 18, 'weight': 68},
         {'name': 'box3', 'value': 86, 'weight': 73},
         {'name': 'box4', 'value': 89, 'weight': 3},
         {'name': 'box5', 'value': 90, 'weight': 27},
         {'name': 'box6', 'value': 58, 'weight': 26},
         {'name': 'box7', 'value': 93, 'weight': 24},
         {'name': 'box8', 'value': 32, 'weight': 57},
         {'name': 'box9', 'value': 89, 'weight': 43},
         {'name': 'box10', 'value': 90, 'weight': 89},
         {'name': 'box1', 'value': 75, 'weight': 43},
         {'name': 'box2', 'value': 75, 'weight': 40},
         {'name': 'box3', 'value': 24, 'weight': 3},
         {'name': 'box4', 'value': 85, 'weight': 1},
         {'name': 'box5', 'value': 35, 'weight': 54},
         {'name': 'box6', 'value': 25, 'weight': 29},
         {'name': 'box7', 'value': 97, 'weight': 99},
         {'name': 'box8', 'value': 71, 'weight': 66},
         {'name': 'box9', 'value': 15, 'weight': 53},
         {'name': 'box10', 'value': 82, 'weight': 41},
         {'name': 'box1', 'value': 87, 'weight': 34},
         {'name': 'box2', 'value': 33, 'weight': 72},
         {'name': 'box3', 'value': 3, 'weight': 14},
         {'name': 'box4', 'value': 3, 'weight': 21},
         {'name': 'box5', 'value': 98, 'weight': 75},
         {'name': 'box6', 'value': 87, 'weight': 44},
         {'name': 'box7', 'value': 81, 'weight': 87},
         {'name': 'box8', 'value': 49, 'weight': 56},
         {'name': 'box9', 'value': 14, 'weight': 7},
         {'name': 'box10', 'value': 70, 'weight': 69}]

data4 = [{'name': 'box1', 'value': 72, 'weight': 29},
         {'name': 'box2', 'value': 6, 'weight': 71},
         {'name': 'box3', 'value': 83, 'weight': 53},
         {'name': 'box4', 'value': 78, 'weight': 73},
         {'name': 'box5', 'value': 39, 'weight': 32},
         {'name': 'box6', 'value': 11, 'weight': 66},
         {'name': 'box7', 'value': 57, 'weight': 26},
         {'name': 'box8', 'value': 5, 'weight': 90},
         {'name': 'box9', 'value': 17, 'weight': 60},
         {'name': 'box10', 'value': 24, 'weight': 53},
         {'name': 'box1', 'value': 34, 'weight': 15},
         {'name': 'box2', 'value': 95, 'weight': 28},
         {'name': 'box3', 'value': 43, 'weight': 5},
         {'name': 'box4', 'value': 33, 'weight': 60},
         {'name': 'box5', 'value': 79, 'weight': 11},
         {'name': 'box6', 'value': 46, 'weight': 67},
         {'name': 'box7', 'value': 56, 'weight': 35},
         {'name': 'box8', 'value': 6, 'weight': 83},
         {'name': 'box9', 'value': 86, 'weight': 25},
         {'name': 'box10', 'value': 81, 'weight': 93},
         {'name': 'box1', 'value': 60, 'weight': 40},
         {'name': 'box2', 'value': 2, 'weight': 24},
         {'name': 'box3', 'value': 74, 'weight': 81},
         {'name': 'box4', 'value': 44, 'weight': 96},
         {'name': 'box5', 'value': 81, 'weight': 100},
         {'name': 'box6', 'value': 18, 'weight': 76},
         {'name': 'box7', 'value': 47, 'weight': 60},
         {'name': 'box8', 'value': 15, 'weight': 15},
         {'name': 'box9', 'value': 72, 'weight': 38},
         {'name': 'box10', 'value': 84, 'weight': 61},
         {'name': 'box1', 'value': 4, 'weight': 38},
         {'name': 'box2', 'value': 34, 'weight': 26},
         {'name': 'box3', 'value': 40, 'weight': 92},
         {'name': 'box4', 'value': 94, 'weight': 31},
         {'name': 'box5', 'value': 15, 'weight': 42},
         {'name': 'box6', 'value': 82, 'weight': 57},
         {'name': 'box7', 'value': 17, 'weight': 66},
         {'name': 'box8', 'value': 55, 'weight': 92},
         {'name': 'box9', 'value': 96, 'weight': 97},
         {'name': 'box10', 'value': 70, 'weight': 86}]

data5 = [{'name': 'box1', 'value': 177, 'weight': 174},
         {'name': 'box2', 'value': 120, 'weight': 28},
         {'name': 'box3', 'value': 33, 'weight': 181},
         {'name': 'box4', 'value': 167, 'weight': 116},
         {'name': 'box5', 'value': 122, 'weight': 39},
         {'name': 'box6', 'value': 29, 'weight': 78},
         {'name': 'box7', 'value': 26, 'weight': 22},
         {'name': 'box8', 'value': 46, 'weight': 86},
         {'name': 'box9', 'value': 148, 'weight': 110},
         {'name': 'box0', 'value': 85, 'weight': 48},
         {'name': 'box1', 'value': 98, 'weight': 4},
         {'name': 'box2', 'value': 139, 'weight': 142},
         {'name': 'box3', 'value': 28, 'weight': 36},
         {'name': 'box4', 'value': 5, 'weight': 173},
         {'name': 'box5', 'value': 37, 'weight': 105},
         {'name': 'box6', 'value': 46, 'weight': 121},
         {'name': 'box7', 'value': 63, 'weight': 145},
         {'name': 'box8', 'value': 26, 'weight': 131},
         {'name': 'box9', 'value': 132, 'weight': 4},
         {'name': 'box0', 'value': 184, 'weight': 45},
         {'name': 'box1', 'value': 145, 'weight': 9},
         {'name': 'box2', 'value': 200, 'weight': 97},
         {'name': 'box3', 'value': 190, 'weight': 114},
         {'name': 'box4', 'value': 41, 'weight': 98},
         {'name': 'box5', 'value': 93, 'weight': 164},
         {'name': 'box6', 'value': 66, 'weight': 14},
         {'name': 'box7', 'value': 12, 'weight': 135},
         {'name': 'box8', 'value': 146, 'weight': 166},
         {'name': 'box9', 'value': 170, 'weight': 200},
         {'name': 'box0', 'value': 41, 'weight': 69},
         {'name': 'box1', 'value': 43, 'weight': 193},
         {'name': 'box2', 'value': 162, 'weight': 172},
         {'name': 'box3', 'value': 62, 'weight': 107},
         {'name': 'box4', 'value': 170, 'weight': 122},
         {'name': 'box5', 'value': 60, 'weight': 10},
         {'name': 'box6', 'value': 42, 'weight': 75},
         {'name': 'box7', 'value': 154, 'weight': 83},
         {'name': 'box8', 'value': 151, 'weight': 162},
         {'name': 'box9', 'value': 90, 'weight': 27},
         {'name': 'box0', 'value': 169, 'weight': 185},
         {'name': 'box1', 'value': 160, 'weight': 62},
         {'name': 'box2', 'value': 147, 'weight': 112},
         {'name': 'box3', 'value': 26, 'weight': 154},
         {'name': 'box4', 'value': 39, 'weight': 192},
         {'name': 'box5', 'value': 70, 'weight': 139},
         {'name': 'box6', 'value': 71, 'weight': 147},
         {'name': 'box7', 'value': 169, 'weight': 9},
         {'name': 'box8', 'value': 47, 'weight': 10},
         {'name': 'box9', 'value': 110, 'weight': 152},
         {'name': 'box0', 'value': 111, 'weight': 108},
         {'name': 'box1', 'value': 15, 'weight': 105},
         {'name': 'box2', 'value': 121, 'weight': 27},
         {'name': 'box3', 'value': 169, 'weight': 85},
         {'name': 'box4', 'value': 153, 'weight': 57},
         {'name': 'box5', 'value': 47, 'weight': 168},
         {'name': 'box6', 'value': 130, 'weight': 46},
         {'name': 'box7', 'value': 59, 'weight': 73},
         {'name': 'box8', 'value': 10, 'weight': 18},
         {'name': 'box9', 'value': 169, 'weight': 82},
         {'name': 'box0', 'value': 163, 'weight': 57}]

ga = pyeasyga.GeneticAlgorithm(data)
ga2 = pyeasyga.GeneticAlgorithm(data2)
ga3 = pyeasyga.GeneticAlgorithm(data3)
ga4 = pyeasyga.GeneticAlgorithm(data4)
ga5 = pyeasyga.GeneticAlgorithm(data5)
val = [10, 20, 30, 40]

def fitness(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 120:
        values = 0
    return values


def fitness2(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 240:
        values = 0
    return values


def fitness3(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 350:
        values = 0
    return values


def fitness4(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 450:
        values = 0
    return values


def fitness5(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 1000:
        values = 0
    return values


def fit(val):
    if val == 140:
        ga.fitness_function = fitness
        ga.run()
        if ga.best_individual()[0] >= val:
            print(ga.best_individual())
        else:
            fit(val)
    elif val == 400:
        ga2.fitness_function = fitness2
        ga2.run()
        if ga2.best_individual()[0] >= val:
            print(ga2.best_individual())
        else:
            fit(val)
    elif val == 800:
        ga3.fitness_function = fitness3
        ga3.run()
        if ga3.best_individual()[0] >= val:
            print(ga3.best_individual())
        else:
            fit(val)
    elif val == 850:
        ga4.fitness_function = fitness4
        ga4.run()
        if ga4.best_individual()[0] >= val:
            print(ga4.best_individual())
        else:
            fit(val)
    else:
        ga5.fitness_function = fitness5
        ga5.run()
        if ga5.best_individual()[0] >= val:
            print(ga5.best_individual())
        else:
            fit(val)




tab = []
#140 400 800 850 2000
start = time.time()
fit(140)
end = time.time()
jobtime = end - start
tab.append(jobtime)

start2 = time.time()
fit(400)
end2 = time.time()
jobtime1 = end2 - start2
tab.append(jobtime1)


start3 = time.time()
fit(800)
end3 = time.time()
jobtime2 = end3 - start3
tab.append(jobtime2)


start4 = time.time()
#fit(850)
end4 = time.time()
jobtime3 = end4 - start4
tab.append(jobtime3)


#start5 = time.time()
#fit(2000)
#end5 = time.time()
#jobtime4 = end5 - start5
#tab.append(jobtime4)

plt.plot(tab,val)
axes = plt.gca()
axes.set_xlim([0,15.0])
axes.set_ylim([0,40])
plt.show()

