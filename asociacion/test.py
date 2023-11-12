import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, apriori, association_rules

# To bool
#one_hot_encoding = pd.read_csv('./one_hot_encoding.csv', index_col=0)
#one_hot_encoding = one_hot_encoding.astype(bool)
#one_hot_encoding.to_csv('./one_hot_encoding_bool.csv')

one_hot_encoding = pd.read_csv('./one_hot_encoding_bool.csv', index_col=0)
print(one_hot_encoding.head())


df_apriori = apriori(one_hot_encoding, min_support=0.009, use_colnames=True).sort_values(by=['support'],ascending=False)
df_apriori.to_csv('./frequent_items_apriori.csv')
res = association_rules(df_apriori, metric="confidence", min_threshold=0.02)
print(res.head())
res.to_csv('./rules_apriori.csv')
#
#df_fpgrowth = fpgrowth(one_hot_encoding, min_support=0.02, use_colnames=True)
#print(df_fpgrowth.head())
#df_fpgrowth.to_csv('./frequent_items_fpgrowth.csv')
#res = association_rules(df_fpgrowth, metric="confidence", min_threshold=0.02)
#print(res.head())
#res.to_csv('./rules_fpgrowth.csv')



#data = pd.read_csv('./Viajes_subsidio.csv', sep=',',index_col=0)
#data = data.drop(columns=['id_hogar','id_persona','id_viaje', 'fecha'])#, 'utam_origen', 'utam_destino'])
#
#duracion_df = pd.read_excel('./duracion.xlsx')
#
#data['duracion'] = duracion_df['duracion']
#
#asociacion = data.copy()
#
#l_edu = {
#1: 'Preescolar', 
#2: 'Primaria incompleta', 
#3: 'Primaria completa',
#4: 'Secundaria incompleta',
#5: 'Secundaria completa',
#6: 'Media incompleta (10º y 11º)',
#7: 'Media completa (10º y 11º)',
#8: 'Técnico/Tecnológico incompleta',
#9: 'Técnico/Tecnológico completa',
#10: 'Universitario incompleto',
#11: 'Universitario completo',
#12:'Posgrado incompleto',
#13: 'Posgrado completo',
#14: 'Ninguno',
#99: 'Sin información'}
#
## Nivel educativo, zat, modo viaje y duracion 
#asociacion['nivel_educativo'] = asociacion.nivel_educativo.map(l_edu)
#
#asociacion['duracion'] = pd.cut(asociacion['duracion'], bins=[0, 20, 40, 60, 80, 100, 300], labels=['0-20 minutos', '20-40 minuto', '40-60 minutos','60-80 minutos','80-100 minutos', 'mas de 100 minutos'])
#
#hot_edu = pd.get_dummies(asociacion['nivel_educativo'])#.reset_index(drop=True, inplace=True)
#hot_duracion = pd.get_dummies(asociacion['duracion'])
#print(hot_duracion.head())
#print('##################################################')
#hot_utam_origen = pd.get_dummies(asociacion['utam_origen'])#.reset_index(drop=True, inplace=True)
#print(hot_utam_origen.head())
#print('##################################################')
#hot_utam_destino = pd.get_dummies(asociacion['utam_destino'])#.reset_index(drop=True, inplace=True)
#print(hot_utam_destino.head())
#print('##################################################')
#hot_modo = pd.get_dummies(asociacion['modo_principal'])#.reset_index(drop=True, inplace=True)
#print(hot_modo.head())
#print('##################################################')
#
##list_one_hot = [hot_edu, hot_duracion, hot_utam_origen, hot_utam_destino, hot_modo]
#list_one_hot = [hot_edu, hot_utam_origen, hot_utam_destino, hot_modo]
#one_hot = pd.concat(list_one_hot, axis=1)
#
#print('Final:')
#print(one_hot.head())
#one_hot.to_csv('one_hot_encoding.csv')