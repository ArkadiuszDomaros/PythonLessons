from pyeasyga import pyeasyga

data = [1, 4, 6, 11, 13, 20, 35]

ga = pyeasyga.GeneticAlgorithm(data)


def fitness(individual, data):
    value, valueb = 0, 0
    for selected, box in zip(individual, data):
        if selected:
            value += box
        if not selected:
            valueb += box
    if value != valueb:
        value = 0
    return value


ga.fitness_function = fitness
ga.run()

print(ga.best_individual())
