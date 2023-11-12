import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

one_hot_encoding = pd.read_csv('./one_hot_encoding_bool.csv', index_col=0)
print(one_hot_encoding.head())

df_fpgrowth = fpgrowth(one_hot_encoding, min_support=0.02, use_colnames=True)
print(df_fpgrowth.head())
df_fpgrowth.to_csv('./frequent_items_fpgrowth.csv')
res = association_rules(df_fpgrowth, metric="confidence", min_threshold=0.02)
print(res.head())
res.to_csv('./rules_fpgrowth.csv')