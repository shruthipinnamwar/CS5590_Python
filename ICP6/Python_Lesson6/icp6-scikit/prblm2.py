import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt



X = pd.read_csv(r"C:\Users\shrut\Desktop\py4e\ICP1 SOurce code\ICP6\Python_Lesson6\sample_stocks.csv")
X= np.array(X)


# no. of clusters
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Coordinates of cluster centers
centroids = kmeans.cluster_centers_
# Labels of each point
labels = kmeans.labels_

colors = ["g.","r.","c.","b."]

for i in range(len(X)):
    #print("coordinate:",X[i], "label:", labels[i])
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 3)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()