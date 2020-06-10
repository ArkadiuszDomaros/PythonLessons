import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics


digits = datasets.load_digits()
# print(digits['data'])
images_and_labels = list(zip(digits.images, digits.target))


# print("Obrazek:")
# print(images_and_labels[39][0])
# print("Cyfra:")
# print(images_and_labels[39][1])

plt.axis('off')
plt.imshow(images_and_labels[39][0], cmap=plt.cm.gray_r, interpolation='nearest')
plt.title('Cyfra: %i' % images_and_labels[39][1])
# plt.show()
plt.savefig('digits.png')

# Liczymy ile jest cyfr
n_samples = len(digits.images)
# Splaszczamy obrazki (sprawdz co sie z nimi stanie!)
data = digits.images.reshape((n_samples, -1))
# Tworzenie klasyfikatora
classifier = svm.SVC(gamma=0.001)
# Trenowanie klasyfiktora na pierwszej polowie bazy danych
classifier.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

expected = digits.target[n_samples // 2:]
predicted = classifier.predict(data[n_samples // 2:])
print("Raport z klasyfikacji %s:\n%s\n"
% (classifier, metrics.classification_report(expected, predicted)))
print("Macierz bledu:\n%s" % metrics.confusion_matrix(expected, predicted))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image, prediction) in enumerate(images_and_predictions[:10]):
    plt.subplot(1, 10, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title(prediction)
