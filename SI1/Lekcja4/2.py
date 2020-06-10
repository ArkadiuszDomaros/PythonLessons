from pyeasyga import pyeasyga

data = [{'value': 19, 'weight': 18},
        {'value': 39, 'weight': 46},
        {'value': 30, 'weight': 15},
        {'value': 40, 'weight': 41},
        {'value': 23, 'weight': 31},
        {'value': 16, 'weight': 30},
        {'value': 14, 'weight': 32},
        {'value': 38, 'weight': 42},
        {'value': 11, 'weight': 32},
        {'value': 37, 'weight': 11}]

ga = pyeasyga.GeneticAlgorithm(data)


def fitness(individual, data):
    values, weights = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            values += box.get('value')
            weights += box.get('weight')
    if weights > 120:
        values = 0
    if values >= 140:
        print(str(weights) + " " + str(values))
    return values


ga.fitness_function = fitness
ga.run()
if ga.best_individual()[0] >= 140:
    print(ga.best_individual())
else:
    print("Fail")
