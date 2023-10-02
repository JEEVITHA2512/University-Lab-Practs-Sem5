import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import MiniBatchKMeans

n_samples=10000
n_features=2
n_clusters=4
X,y=make_blobs(n_samples=n_samples , n_features=n_features , random_state=42)

batch_size=1000
n_init=10
mbk=MiniBatchKMeans(n_clusters=n_clusters, batch_size=batch_size ,n_init=n_init)
mbk_labels=mbk.fit_predict(X)

plt.scatter(X[:,0],X[:,1],c=mbk_labels, cmap='rainbow')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

