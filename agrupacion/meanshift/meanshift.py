import pandas as pd
from sklearn.cluster import MeanShift
from sklearn import metrics
from sklearn.cluster import estimate_bandwidth

#data = pd.read_csv('./V_Agrupacion_2.csv', index_col=0)
#X = data.to_numpy()
#
##print(estimate_bandwidth(X))#, *, quantile=0.3, n_samples=None, random_state=0, n_jobs=None))
## result estimate bandwidth 0.8652281923964116
#
#
#ms = MeanShift(bandwidth=2).fit(X)
#
#y = ms.labels_
#
#data['Cluster'] = y 
#print(data.head())
#
#data.to_csv('./meanshift/meanshift_2.csv')
#
#print('Metricas de evaluacion:')
##print(f'Adjusted Rand Index: {metrics.adjusted_rand_score(target, pred)}')
#print(f"Silhouette Coefficient: {metrics.silhouette_score(X, y):.3f}")
#print(f'Davies-Bouldin Index: {metrics.davies_bouldin_score(X, y)}\n')
##print(f'Mutual Information Score: {metrics.mutual_info_score(target, pred)}') 

data = pd.read_csv('./meanshift/meanshift_2.csv', index_col=0)
#print(data.head())
print()
a = data[data.Cluster == 0]
print(a.mode())
b = data[data.Cluster == 1]
print(b.mode())

#print('Clusters y cantidad de elementos:')
#print(data['Cluster'].value_counts())
#print(data.groupby('Cluster').mode())