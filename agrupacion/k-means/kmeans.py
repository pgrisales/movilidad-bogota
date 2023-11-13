import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt

#data = pd.read_csv('./V_Agrupacion_2.csv', index_col=0)
#X = data.to_numpy()
#
#kmeans = KMeans(n_clusters=3, random_state=2)#.fit(X)
#
#pred = kmeans.fit_predict(X)
#
#data['Cluster'] = pred
#print(data.head())
#
#data.to_csv('./k-means/k-means_2.csv')
#
#print('Metricas de evaluacion:')
##print(f'Adjusted Rand Index: {metrics.adjusted_rand_score(target, pred)}')
#print(f"Silhouette Coefficient: {metrics.silhouette_score(X, pred):.3f}")
#print(f'Davies-Bouldin Index: {metrics.davies_bouldin_score(X, pred)}\n')
##print(f'Mutual Information Score: {metrics.mutual_info_score(target, pred)}') 
#
data = pd.read_csv('./k-means/k-means_2.csv', index_col=0)
#print(data.head())
print()
#print(data.groupby('Cluster'))
a = data[data.Cluster == 0]
print(a.mode())
b = data[data.Cluster == 1]
print(b.mode())
c = data[data.Cluster == 2]
print(c.mode())

#print('Clusters y cantidad de elementos:')
#print(data['Cluster'].value_counts())

# K-Means elbow
##Find optimum number of cluster
#sse = [] #SUM OF SQUARED ERROR
#for k in range(1,12):
#  km = KMeans(n_clusters=k, random_state=2)
#  km.fit(X)
#  sse.append(km.inertia_)
#
#sns.set_style("whitegrid")
#g=sns.lineplot(x=range(1,12), y=sse)
# 
#g.set(xlabel ="Number of cluster (k)", 
#      ylabel = "Sum Squared Error", 
#      title ='Elbow Method')
# 
#plt.show()