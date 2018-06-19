import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

X = []
Y = []


                    #get the data and append it to ARRAY
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            #print(', '.join(row))
            X.append(int(row[0]))
            Y.append(int(row[1]))
    return

                      #PLot the graph
def show_plot(X, Y):
    linear_mod = linear_model.LinearRegression()
    X = np.reshape(X, (len(X), 1))  # converting to matrix of n X 1
    Y = np.reshape(Y, (len(Y), 1))
    linear_mod.fit(X, Y)  # fitting the data points in the model
    plt.scatter(X, Y, color='orange')  # plotting the initial datapoints
    plt.plot(X, linear_mod.predict(X), color='green', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return




get_data('tabledata.csv')  # calling get_data method by passing the csv file to it
print
X
print
Y
print
"\n"

show_plot(X, Y)
