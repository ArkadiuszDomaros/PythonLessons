from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import NearestNeighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from pylab import *
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt


faces = datasets.fetch_olivetti_faces()
n_samples = len(faces.images)
data = faces.images.reshape((n_samples, -1))
tab = []
X_train, X_test, y_train, y_test = train_test_split(
        faces.data, faces.target, test_size=0.25, random_state=0)

# SVC
svc = SVC(kernel='linear')
svc.fit(X_train, y_train)
y_pred = svc.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print('SVM: ' + str(accuracy_score(y_test, y_pred)))
tab.append(accuracy_score(y_test, y_pred))

# printing faces
images_and_predictions = list(zip(faces.images[n_samples // 2:], y_pred))
for index, (image, prediction) in enumerate(images_and_predictions[:60]):
    plt.subplot(6, 10, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

# K NEAREST NEIGHBOURS
print('----------------------------------------------------------')
classifier = KNeighborsClassifier(n_neighbors=2)
classifier.fit(data[:n_samples // 2], faces.target[:n_samples // 2])
y_pred = classifier.predict(data[:n_samples // 2])
print(confusion_matrix(faces.target[:n_samples // 2], y_pred))
print('k Nearest Neighbours: ' + str(accuracy_score(faces.target[:n_samples // 2], y_pred)))
tab.append(accuracy_score(faces.target[:n_samples // 2], y_pred))


# neurony
print('----------------------------------------------------------')
mlp = MLPClassifier(hidden_layer_sizes=(10), solver='sgd', learning_rate_init=0.001, max_iter=5000)
mlp.fit(data[:n_samples // 2], faces.target[:n_samples // 2])
pred = mlp.predict(data[:n_samples // 2])
print(confusion_matrix(faces.target[:n_samples // 2], pred))
print('Neuron: ' + str(mlp.score(data[:n_samples // 2], faces.target[:n_samples // 2])))
tab.append(mlp.score(data[:n_samples // 2], faces.target[:n_samples // 2]))

x_data = ['SVM', 'KNN', 'Neuron']
plt.bar(x_data, tab)
plt.show()

