from sklearn import datasets, svm, metrics
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from pylab import *
from sklearn.neural_network import MLPClassifier

digits = datasets.load_digits()
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
tab = []

classifier = svm.SVC(gamma=0.001)
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])
images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:60]):
    plt.subplot(6, 10, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title(prediction)
plt.show()
# print("Raport z klasyfikacji %s:\n%s\n"
# % (classifier, metrics.classification_report(expected, predicted)))
print("Macierz bledu:\n%s" % metrics.confusion_matrix(expected, predicted))
print('SVM: ' + str(accuracy_score(expected, predicted)))
tab.append(accuracy_score(expected, predicted))


# K NEAREST NEIGHBOURS
print('----------------------------------------------------------')
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
y_pred = classifier.predict(data[:n_samples // 2])
print(confusion_matrix(digits.target[:n_samples // 2], y_pred))
print('k Nearest Neighbours: ' + str(accuracy_score(digits.target[:n_samples // 2], y_pred)))
tab.append(accuracy_score(digits.target[:n_samples // 2], y_pred))


# neurony
print('----------------------------------------------------------')
mlp = MLPClassifier(hidden_layer_sizes=(10), solver='sgd', learning_rate_init=0.001, max_iter=2000)
mlp.fit(data[:n_samples // 2], digits.target[:n_samples // 2])
pred = mlp.predict(data[:n_samples // 2])
print(confusion_matrix(digits.target[:n_samples // 2], pred))
print('Neuron: ' + str(mlp.score(data[:n_samples // 2], digits.target[:n_samples // 2])))
tab.append(mlp.score(data[:n_samples // 2], digits.target[:n_samples // 2]))

x_data = ['SVM', 'KNN', 'Neuron']
plt.bar(x_data, tab)
plt.show()

