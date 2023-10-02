import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans,AgglomerativeClustering
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

iris=load_iris()
data=iris.data

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
kmeans_labels=kmeans.labels_
kmeans_centroids=kmeans.cluster_centers_

print("KMeans Cluster Labels" , kmeans_labels)
print("KMeans Centroids" , kmeans_centroids)

dist_matrix=np.linalg.norm(data[:,np.newaxis]-data,axis=-1)
mst=minimum_spanning_tree(csr_matrix(dist_matrix))
connectivity=mst.toarray().astype(bool)
clustering=AgglomerativeClustering(n_clusters=3,connectivity=connectivity)
mst_labels=clustering.fit_predict(data)

print("MST Labels",mst_labels)
