import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from sklearn.decomposition import PCA

iris=load_iris
x=iris.data

pca=PCA(n_components=2)
X=pca.fit_transform(x)
agg_clustering=AgglomerativeClustering(n_clusters=3)
agg_labels=agg_clustering.fit_predict(x)

plt.scatter(X[:,0],X[:,1],c=agg_labels, cmap='rainbow')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()
