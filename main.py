
#import csv
import json
import pandas as pd
import numpy as np

    

df1 = pd.read_csv('TESLA.csv')

df1["Precio"] = (df1["Close"] - df1["Open"])

print('\n','Desarrollo Parte 1')
print('\n')
print(f'Dataframe orgininal al leer TEST.csv','\n')
print(df1)

print('\n','INICIO desarrollo Parte 1, generar archivo := analisis_archivo.csv')

conditionlist = [
    (df1["Precio"] > 0),
    (df1["Precio"] < 0),
    (df1["Precio"] == 0)]

choicelist = ['SUBE', 'BAJA', 'ESTABLE']
df1["Comportamiento de la accion"] = np.select(conditionlist, choicelist, default='Not Specified')

df1["Ajuste Cuadratico de Close"] = np.sqrt((df1["Close"] - df1["Adj Close"])**2)

df1.rename(columns={ "Date": "Fecha" }, inplace=True)
df1 = df1[["Fecha", "Comportamiento de la accion", "Ajuste Cuadratico de Close"]]

print('\n')
print(f'Este es el Dataframe con las 3 columnas a dejar en analisis_archivo.csv ')
print('\n')
print(df1)

df1.to_csv("analisis_archivo.csv",index=None, sep='\t',mode='w')  

#==========================================

# INICIO SEGUNDA PARTE

print('\n','Inicio Segunda Parte, generar archivo := detalles.json')

df5 = pd.read_csv('TESLA.csv')

print('\n')
print(f'Dataframe original al leer TEST.csv','\n')
print(df5.head(3))


pos_lowest_open = df5["Open"].idxmin()
date_lowest_open = df5.iloc[pos_lowest_open,0]
lowest_open = df5["Open"][df5["Open"].idxmin()]

print('\n','++++')
print(f'Index lowest open :',pos_lowest_open)
print(f'date_lowest_open = ',date_lowest_open)
print(f'lowest_open      = ',lowest_open)
print(f' ++++')

pos_highest_close = df5["Close"].idxmax()
date_highest_close = df5.iloc[pos_highest_close,0]
highest_close = df5["Close"][df5["Close"].idxmax()]

print('\n','====')
print(f'Index Highest Close :',pos_highest_close)
print(f'date_highest_close = ',date_highest_close)
print(f'highest_close      = ',highest_close)
print(f' ====')

mean_volume = df5["Volume"].mean()

print('\n','++++')
print(f'mean_volume        = ',mean_volume)

df5["Diferencia"] = (df5["Low"] - df5["High"]).abs()
pos_greatest_difference = df5["Diferencia"].idxmax()
date_greatest_difference = df5.iloc[pos_greatest_difference,0]
greatest_difference = df5["Diferencia"][df5["Diferencia"].idxmax()]

print('\n')
print(df5)

print('\n','####')
print(f'Index Greatest difference :',pos_greatest_difference)
print(f'date_greatest_difference = ',date_greatest_difference)
print(f'greatest_difference      = ',greatest_difference)
print(f' ####')


objeto_resultado = { "date_lowest_open": date_lowest_open, "lowest_open": lowest_open, "date_highest_close": date_highest_close, "highest_close": highest_close, "mean_volume": mean_volume, "date_greatest_difference": date_greatest_difference, "greatest_difference": greatest_difference }

print('\n')
print(f'Objeto Json resultado',objeto_resultado)

with open('detalles.json','w') as json_file:
    json.dump(objeto_resultado, json_file)



print('\n')
print(f'Listos, reto realizado!!')

    
   