import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

from datasets import(
    circles, 
    moons,
    blobs,
    anisotropic,
    random,
    varied_variances
)

X = circles() # 0.1 misses a few obvious points. 0.5 only denotes one cluster, too big. 
X = moons() # Two distinct clusters, barely misses one point at 0.1
X = blobs() # 0.1 Everything is an outlier, too small! 0.5 is still a bit too small. 0.75 gets a lot more. 
X = anisotropic() # Three distinct clusters, barely misses one point at 0.1, decreasing allows us to see more outliers
X = random() # One large cluster, no real distinction even at 0.1. Even at 0.01 it only highlights one. 
X = varied_variances() # 0.1 too low, eps 1 three clusters of varying spread. Works best when clsuters have about the same variance
 

dbscan = DBSCAN(eps=0.1, min_samples=5) # 0.1 misses a few obvious points. 0.5 only denotes one cluster, too big. 

dbscan.fit(X)

# get inliers and their cluster
x_inlier=X[dbscan.labels_ != -1]
y_inlier=dbscan.labels_[dbscan.labels_ != -1]

# get outliers
x_outlier = X[dbscan.labels_ == -1]

plt.scatter(x_inlier[:,0], x_inlier[:,1], c=y_inlier, cmap='Dark2')
plt.scatter(x_outlier[:,0], x_outlier[:,1], c='k')
plt.show()