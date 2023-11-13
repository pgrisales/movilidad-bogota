import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

f = './asociacion_2.csv'
one_hot_encoding = pd.read_csv(f, index_col=0)
#print(one_hot_encoding.head())


df_apriori = apriori(one_hot_encoding, min_support=0.2, use_colnames=True).sort_values(by=['support'],ascending=False)
df_apriori.to_csv('./frequent_items_apriori_2.csv')

pd.set_option('display.max_colwidth', None)

print()
print(f)
print()
print(df_apriori.head(6))
print(df_apriori.info())
print()
res = association_rules(df_apriori, metric="confidence", min_threshold=0.7).sort_values(by=['confidence'],ascending=False)
res = res[['antecedents', 'consequents', 'confidence']]

print()
print(res.head(6))
print(res.info())
print()
res.to_csv('./rules_apriori_2.csv')