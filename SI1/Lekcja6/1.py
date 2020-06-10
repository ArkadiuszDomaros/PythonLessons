import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from apyori import apriori

store_data = pd.read_csv('store_data.csv', header=None)
store_data.head()
records = []
for i in range(0, 7501):
    records.append([str(store_data.values[i,j]) for j in range(0, 20)])

print(records)

association_rules = apriori(records, min_support=0.0045, min_confidence=0.5, min_lift=2, min_length=3)
association_results = list(association_rules)

print(len(association_results))
print(association_results[0])
for item in association_results:

    # first index of the inner list
    # Contains base item and add item
    tab = []
    pair = item[0]
    if len(pair) == 3:
        items = [x for x in pair]
        print("Rule: " + str(item[2][0][0]) + " -> " + str(item[2][0][1]))
        print("Support: " + str(item[1]))
        print("Confidence: " + str(item[2][0][2]))
        print("Lift: " + str(item[2][0][3]))
        print("=====================================")
        for y in items:
            if y != 'nan':
                print(y)
