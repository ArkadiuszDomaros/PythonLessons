from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris=datasets.load_iris()

x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4)

for i in range(len(x)):
    print(str(x[i]) + " " + str(y[i]))


def myIrisClassifier(db):
    predictions = []
    for db_record in db:
        if db_record[3] < 0.6:
            predictions.append(0)
        elif db_record[2] > 4.5:
            predictions.append(2)
        else:
            predictions.append(1)
    return predictions


predictions = myIrisClassifier(x_test)
print(accuracy_score(y_test,predictions))
