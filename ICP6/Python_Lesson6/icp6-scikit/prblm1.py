from sklearn import datasets,metrics

from sklearn.naive_bayes import GaussianNB

from sklearn.model_selection import KFold

from sklearn import cross_validation as cv

import numpy as np

gaussian = GaussianNB()

iris = datasets.load_iris()

data = iris.data

labels = iris.target

splits = cv.train_test_split(data, labels, test_size=0.2)

X_train , X_test , y_train , y_test = splits

y_pred = gaussian.fit(X_train,y_train).predict(X_test)

print(metrics.confusion_matrix(y_test, y_pred)) 
print(metrics.classification_report(y_test, y_pred)) 
print(metrics.accuracy_score(y_test,y_pred))