from sklearn.neural_network import MLPClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

datatrain = pd.read_csv('iris.csv')
datatrain.loc[datatrain['species'] == "setosa", 'species'] = 0
datatrain.loc[datatrain['species'] == "versicolor", 'species'] = 1
datatrain.loc[datatrain['species'] == "virginica", 'species'] = 2
datatrain = datatrain.apply(pd.to_numeric)
datatrain_array = datatrain.values

X_train, X_test, y_train, y_test = train_test_split(datatrain_array[:, :4], datatrain_array[:, 4], test_size=0.2)
X_test = X_test.astype('int')
y_test = y_test.astype('int')

mlp = MLPClassifier(hidden_layer_sizes=(5), solver='sgd', learning_rate_init=0.001, max_iter=1000)

mlp.fit(X_test, y_test)

print(mlp.score(X_test, y_test))
pred = mlp.predict(X_test)
print(confusion_matrix(y_test, pred))


