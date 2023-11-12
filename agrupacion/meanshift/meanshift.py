import pandas as pd
from sklearn.cluster import MeanShift
from sklearn import metrics

data = pd.read_csv('./V_Agrupacion_2.csv', index_col=0)
X = data.to_numpy()

ms = MeanShift(bandwidth=2).fit(X)

y = ms.labels_

data['Cluster'] = y 
print(data.head())

data.to_csv('./meanshift/meanshift_2.csv')
print(f"Silhouette Coefficient: {metrics.silhouette_score(X, y):.3f}")

#data = pd.read_csv('./meanshift.csv', index_col=0)
#print(data.head())
print(data['Cluster'].value_counts())