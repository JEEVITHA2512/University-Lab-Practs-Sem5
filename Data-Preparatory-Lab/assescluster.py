from sklearn.datasets import load_iris
from sklearn.metrics import silhouette_score,adjusted_rand_score,davies_bouldin_score
from sklearn.cluster import KMeans

iris=load_iris()
data=iris.data

kmeans=KMeans(n_clusters=3)
kmeans.fit(data)
labels=kmeans.labels_

silhouette=silhouette_score(data,labels)
rand_index=adjusted_rand_score(iris.target,labels)
davies=davies_bouldin_score(data,labels)
wcss=kmeans.inertia_

print("Silhouette",silhouette)
print("rand_index",rand_index)
print("davies",davies)
print("WCSS",wcss)