import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

one_hot_encoding = pd.read_csv('./one_hot_encoding_bool.csv', index_col=0)
print(one_hot_encoding.head())

df_apriori = apriori(one_hot_encoding, min_support=0.009, use_colnames=True).sort_values(by=['support'],ascending=False)
df_apriori.to_csv('./frequent_items_apriori.csv')
res = association_rules(df_apriori, metric="confidence", min_threshold=0.02)
print(res.head())
res.to_csv('./rules_apriori.csv')