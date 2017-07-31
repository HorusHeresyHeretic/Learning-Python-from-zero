# нужны модули pandas и Nympy

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import warnings
warnings.simplefilter('ignore')
import pandas as pd
import numpy as pr
df = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/telecom_churn.csv")
"""
df.head()                                    # возвращает первые 5 строк из файла
"""
"""
pd.set_option('display.max_columns', 100)    # изменяет максимальное число выводимых столбцов
pd.set_option('display.max_rows', 100)       # изменяет максимальное число выводимых строк
"""
print(df.shape)                              # возвращает (3333, 20) - (строки, столбцы)
print(df.columns)                            # возвращает название столбцов
print(df.info())                             # общая информация по дата фрейму
df['Churn'] = df['Churn'].astype('int64')
df.describe()                                # общая стата по основным числовым характеристикам
df.describe(include=['object', 'bool'])      # возвращает статистику по нечисловым признакам
df['Churn'].value_counts()                   # распределение данных по переменной Churn
df.sort_values(by='Total day charge',        # сортировка по признаку Total day charge
        ascending=False).head()              # ascending=False для сортировки по убыванию 
df.sort_values(by='Total day minutes',       # сортировка по признаку Total day minutes
        ascending=False).head() 
df.sort_values(by=['Churn', 'Total day charge'],  # сортировка по группе столбцов
        ascending=[True, False]).head()
df['Churn'].mean()                           # возвращает долю нелояльных клиентов в датафрейме  
df[df['Churn'] == 1].mean()                  # возвращает средние значения числовых признаков в Churn(1) 
df[df['Churn'] == 0].mean()                  # возвращает средние значения числовых признаков в Churn(0)
df[df['Churn'] == 1]['Total day minutes'].mean()  # возвращает среднее время разговора в среде Churn(1) 
df[df['Churn'] == 0]['Total day minutes'].mean()  # возвращает среднее время разговора в среде Churn(0) 
df[(df['Churn'] == 0) & (df['International plan'] == 'No')]['Total intl minutes'].max()
df[(df['Churn'] == 1) & (df['International plan'] == 'No')]['Total intl minutes'].max()
df.loc[0:5, 'State':'Area code']             # возвращает значение 6 строк в столбцах от Стате до Ареа 
df.iloc[0:5, 0:3]                            # возвращает значение первых пяти строк в первых 3 столбцах
df[-1:]                                      # последняя строка дата фрейма
len(df)
"""
df[111:112]                                  # 112 строка датаффрейма  (ну вот так она возвращается)
"""
df.apply(pr.max)                             # ищет и возвращает аккаунт с максимальными значения по всему датафрейму 
df.apply(pr.min)                             # ищет и возвращает аккаунт с минимальныни значенияи по всему даатфрейму
"""
df.apply(pr.sum, axis = 1)                   # возвращает варп воронку с исключениями
"""
d = {'No' : False, 'Yes' : True}             # на что меняем значения в колонке 
df['International plan'] = df['International plan'].map(d)      # в какой колонке меняем значения (типа .format)
df.head()                                    # возвращает всю информацию по фрейму с заменой значений в International plan
"""
d = {'No' : False, 'Yes' : True} 
df = df.replace({'Voice mail plan': d})      # тоже что и в предыдущем случае 
df.head()
"""
"""
df.groupby(df=grouping_colums)[columns_to_show].function()      # точечная нотация описывающая метод резделения 
"""
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']      #  см коммент на 422
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes'] 
df.groupby(['Churn'])[columns_to_show].agg([pr.mean, pr.std, pr.min, pr.max])            # использованием NumPy
pd.crosstab(df['Churn'], df['International plan'])                                       # табличная ересь!!!
pd.crosstab(df['Churn'], df['Voice mail plan'], normalize=True)
df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['Area code'], aggfunc='mean').head(10)
df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'], ['International plan'], aggfunc='min').head()
""" выше мы создаём сводные таблицы - смотри комменты в строках 500+"""
total_calls = df['Total day calls'] + df['Total eve calls'] + df['Total night calls'] + df['Total intl calls']
df.insert(loc=len(df.columns), column='Total calls', value=total_calls) 
# loc - номер столбца, после которого нужно вставить данный Series
# мы указали len(df.columns), чтобы вставить его в самом конце
df.head()
df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
df.head()
df = df.drop(['Total charge', 'Total calls'], axis=1)       # избавляемся от созданных только что столбцов 
df.drop([1, 2]).head()                                      # а вот так можно удалить строчки
pd.crosstab(df['Churn'], df['International plan'], margins=True)    # прогнозирование оттока
pd.crosstab(df['Churn'], df['Customer service calls'], margins=True)# ещё один прогноз
df['Many_service_calls'] = (df['Customer service calls'] > 3).astype('int')  # добавляем новый бинарный признак
pd.crosstab(df['Many_service_calls'], df['Churn'], margins=True)             # строим прогноз на его основании
pd.crosstab(df['Many_service_calls'] & df['International plan'] , df['Churn']) # сводим полученные данные 