import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import metrics
import math

#data = pd.read_csv('./V_Agrupacion_2.csv', index_col=0)
#X = data.to_numpy()
#eps = 0.4
#min_samples = 200 
#
#db = DBSCAN(eps=eps, min_samples=min_samples).fit(X)
#labels = db.labels_
#
#data['Cluster'] = labels
#print(data.head())
#
#data.to_csv('./dbscan/dbscan_2.csv')
#
## Number of clusters in labels, ignoring noise if present.
#n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#n_noise_ = list(labels).count(-1)
#
#print(f'eps: {eps}, min_samples: {min_samples}')
#print("Estimated number of clusters: %d" % n_clusters_)
#print("Estimated number of noise points: %d" % n_noise_)
#
#print('Metricas de evaluacion:')
##print(f'Adjusted Rand Index: {metrics.adjusted_rand_score(target, pred)}')
#print(f"Silhouette Coefficient: {metrics.silhouette_score(X, labels):.3f}")
#print(f'Davies-Bouldin Index: {metrics.davies_bouldin_score(X, labels)}\n')
##print(f'Mutual Information Score: {metrics.mutual_info_score(target, pred)}') 
#
data = pd.read_csv('./dbscan/dbscan_2.csv', index_col=0)
#print(data.head())
print()
a = data[data.Cluster == 0]
print(a.mode())
b = data[data.Cluster == 1]
print(b.mode())
#print(data['Cluster'].value_counts())

#def calculate_kn_distance(X,k):
#
#  kn_distance = []
#  for i in range(len(X)):
#    eucl_dist = []
#    for j in range(len(X)):
#      eucl_dist.append(
#        math.sqrt(
#          ((X[i,0] - X[j,0]) ** 2) +
#          ((X[i,1] - X[j,1]) ** 2)))
#
#    eucl_dist.sort()
#    kn_distance.append(eucl_dist[k])
#
#  return kn_distance
#
#eps_dist = calculate_kn_distance(X,4)
#plt.hist(eps_dist,bins=30)
#plt.ylabel('n')
#plt.xlabel('Epsilon distance')