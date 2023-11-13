import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules

f = './asociacion_2.csv'
one_hot_encoding = pd.read_csv(f, index_col=0)
#print(one_hot_encoding.head())

df_fpgrowth = fpgrowth(one_hot_encoding, min_support=0.4, use_colnames=True).sort_values(by=['support'],ascending=False)

pd.set_option('display.max_colwidth', None)

print()
print(f)
print()
print(df_fpgrowth.head(6))
print(df_fpgrowth.info())
df_fpgrowth.to_csv('./frequent_items_fpgrowth_2.csv')
res = association_rules(df_fpgrowth, metric="confidence", min_threshold=0.7).sort_values(by=['confidence'],ascending=False)
res = res[['antecedents', 'consequents', 'confidence']]

print()
print(res.head(6))
print(res.info())
print()
res.to_csv('./rules_fpgrowth_2.csv')