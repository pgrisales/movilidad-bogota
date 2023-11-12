import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics

data = pd.read_csv('./V_Agrupacion_2.csv', index_col=0)
X = data.to_numpy()
eps = 0.4
min_samples = 200 

db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
labels = db.labels_

data['Cluster'] = labels
print(data.head())

data.to_csv('./dbscan/dbscan_2.csv')

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

print(f'eps: {eps}, min_samples: {min_samples}')
print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)

print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")

#data = pd.read_csv('./dbscan.csv', index_col=0)
#print(data.head())
print(data['Cluster'].value_counts())