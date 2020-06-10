from sklearn.datasets import load_breast_cancer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import NearestNeighbors
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from pylab import *
import matplotlib.pyplot as plt

data = load_breast_cancer()
tab = []
# 0 maligant
# 1 benign

x = data.data
y = data.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

# DECISION TREE
classifier1 = tree.DecisionTreeClassifier()
classifier1.fit(x_train, y_train)
predictions = classifier1.predict(x_test)
print("Decision Tree: " + str(accuracy_score(y_test, predictions)))
print(confusion_matrix(y_test, predictions))
tab.append(accuracy_score(y_test, predictions))

# NAIVE BAYES
gnb = GaussianNB()
y_pred = gnb.fit(data.data, data.target).predict(data.data)
expected = data.target
print("Naive Bayes: " + str(accuracy_score(expected, y_pred)))
print(confusion_matrix(expected, y_pred))
tab.append(accuracy_score(expected, y_pred))

# K NEAREST NEIGHBOURS
nbrs = NearestNeighbors(n_neighbors=2, algorithm='ball_tree').fit(x_test)
distances, indices = nbrs.kneighbors(x_test)
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print('k Nearest Neighbours: ' + str(accuracy_score(y_test, y_pred)))
print(confusion_matrix(y_test, y_pred))
tab.append(accuracy_score(y_test, y_pred))

# SVM CLASSIFER
svm = SVC(kernel='rbf', random_state=0, gamma=0.5, C=1.0)
svm.fit(x_train, y_train)
pred = svm.predict(x_test)
print('SVM classifier: ' + str(accuracy_score(y_test, pred)))
print(confusion_matrix(y_test, pred))
tab.append(accuracy_score(y_test, pred))

x_data = ['DT', 'NB', 'KNN', 'SVM']
# plot(x_data, tab, 'ro')
# show()
plt.bar(x_data, tab)
plt.show()
