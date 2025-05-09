import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from datasets import(
    circles, 
    moons,
    blobs,
    anisotropic,
    random,
    varied_variances
)

X = circles()

kmeans = KMeans(n_clusters=2, random_state=17)
kmeans.fit(X)

plt.figure()
plt.scatter(X[:,0], X[:,1])
plt.scatter(X[:,0], X[:,1], c=kmeans.labels_) 
plt.show()