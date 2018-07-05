import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import tensorflow as tf
import xlrd


data_file = "data/Smoking.xls"

# read in data from Excel sheet -- data is in workbook 1 and has
# three columns - X1, X2 and Y
book = xlrd.open_workbook(data_file, encoding_override="utf-8")

# get first workbook
sheet = book.sheet_by_index(0)

# loop through data in worksheet and save each row in data array
data = np.asarray([sheet.row_values(i) for i in range(1, sheet.nrows)])

# total samples is number of rows - 1 because of header
total_samples = sheet.nrows - 1

# make placeholders for input and output variables

# print run size in thousands
X1 = tf.placeholder(tf.float32, name='X1')
# number of pages
X2 = tf.placeholder(tf.float32, name='X2')

# number of orders in thousands
Y = tf.placeholder(tf.float32, name='Y')

# create weights and bias variables, initialize as zero -- will be
# adjusted through each iteration over graph
w1 = tf.Variable(0.0, name='weights1')
w2 = tf.Variable(0.0, name='weights2')
b = tf.Variable(0.0, name='bias')


# define model for predicting number of orders given print run size and
# number of pages
Y_predicted = (X1 * w1) + (X2 * w2) + b

# define loss function using squared errors (distance of predicted
# number of orders from actual)
loss = tf.square(tf.subtract(Y, Y_predicted), name='loss')


# make gradient descent optimizer to minimize error as calculated by loss function
#
# set learning rate very low to avoid getting loss values of infinity/nan
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.000000001).minimize(loss)


with tf.Session() as sess:
    # initialize variables: w1, w2 and b
    sess.run(tf.global_variables_initializer())

    # make writer to save data for review in TensorBoard
    writer = tf.summary.FileWriter('./graphs/linear_reg2', sess.graph)

    # train the model by iterating over training data and minimizing
    # error as defined by our loss function

    # iterate 50 times as in example
    for i in range(50):
        total_loss = 0

        # iterate over three columns of data in each row
        for x1,x2,x3,y in data:
            # Session runs train_op and fetch values of loss
            _, l = sess.run([optimizer, loss], feed_dict={X1 : x1, X2 : x2, Y : y})
            total_loss += l
        print('Epoch {0}: {1}'.format(i, total_loss / total_samples))


    writer.close()

    # get weights and bias
    w1, w2, b = sess.run([w1, w2, b])

# plot the results - use a 3d plot since we have two predictors and an
# outcome variable
X1, X2, Y = data.T[0], data.T[1], data.T[2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1, X2, Y, 'bo', label='Real data')
ax.scatter(X1, X2, (X1*w1) + (X2*w2) + b, 'r', label='Predicted data')

plt.legend()
plt.show()
