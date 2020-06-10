from sklearn.metrics import confusion_matrix
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)
tab1 = []
tab2 = []

# DECISION TREE
classifier1 = tree.DecisionTreeClassifier()
classifier1.fit(x_train, y_train)
predictions = classifier1.predict(x_test)
print("Decision Tree: " + str(accuracy_score(y_test, predictions)))
print(confusion_matrix(y_test, predictions))
tab1.append(confusion_matrix(y_test, predictions)[1][2])
tab2.append(confusion_matrix(y_test, predictions)[2][1])

# NAIVE BAYES
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
expected = iris.target
print("Naive Bayes: " + str(accuracy_score(expected, y_pred)))
print(confusion_matrix(expected, y_pred))
tab1.append(confusion_matrix(expected, y_pred)[1][2])
tab2.append(confusion_matrix(expected, y_pred)[2][1])

# K NEAREST NEIGHBOURS
nbrs = NearestNeighbors(n_neighbors=3, algorithm='ball_tree').fit(x_test)
distances, indices = nbrs.kneighbors(x_test)
classifier = KNeighborsClassifier(n_neighbors=3)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print('k Nearest Neighbours: ' + str(accuracy_score(y_test, y_pred)))
print(confusion_matrix(y_test, y_pred))
tab1.append(confusion_matrix(y_test, y_pred)[1][2])
tab2.append(confusion_matrix(y_test, y_pred)[2][1])

print("Pomyłka z versicolor na virginica: ")
print("# DECISION TREE: " + str(tab1[0]) + " NAIVE BAYES: " + str(tab1[1]) + " K NEAREST NEIGHBOURS: " + str(tab1[2]))
print("Pomyłka z virginica na versicolor: ")
print("# DECISION TREE: " + str(tab2[0]) + " NAIVE BAYES: " + str(tab2[1]) + " K NEAREST NEIGHBOURS: " + str(tab2[2]))

# 0 setosa
# 1 versicolor
# 2 virginica
