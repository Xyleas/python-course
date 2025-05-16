import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

from datasets import(
    circles, 
    moons,
    blobs,
    anisotropic,
    random,
    varied_variances
)

X = circles() # No outliers w/ single linkage
X = moons() # Two clusters, makes sense
X = blobs() # 3 clusters, works great
X = anisotropic() # 3 distinct clusters, complete linkage misses some, average linkage works well as well. The different styles kinda define the strictness
X = random() # mostly one, but some small tiny tiny clustesr
X = varied_variances() # single linkage merges two clusters, 

hac= AgglomerativeClustering(n_clusters=3, linkage='single')
hac.fix(X)

plt.scatter(X[:,0], X[:,1], c=hac.labels_)
plt.show()
