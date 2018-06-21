from sklearn.linear_model import LogisticRegression
from sklearn import datasets

irisdatasets = datasets.load_iris()
x = irisdatasets.data
y = irisdatasets.target

model = LogisticRegression()
model.fit(x, y)
print(model.score(x, y))







import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
dataset = pd.read_csv(r"C:\Users\shrut\Desktop\py4e\ICP1 SOurce code\ICP6\Python_Lesson6") 
X = dataset.iloc[:,:].values
kmeans = KMeans(n_clusters = 3, init = 'k-means++', random_state = 123) 
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1') 
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2') 
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of Stock') 
plt.xlabel('Returns') 
plt.ylabel('Dividend Yield') 
plt.show()