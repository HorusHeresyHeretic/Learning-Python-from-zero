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

# я есть бог и делаю как мне угодно.
# https://github.com/Yorko/mlcourse_open/blob/master/jupyter_notebooks/topic01_pandas_data_analysis/hw1_adult_pandas.ipynb

import pandas as pd      
matplotlib inline                              # чтоб картинки рисовались в тетрадке (в анаконде не работает)    
import matplotlib.pyplot as plt           
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 8)
import pandas as pd
import numpy as pr
data = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
data.head()                                    # возвращает первые 5 строк из файла - просто проверяем.
print(data.shape)                              # возвращает (32561, 15) - 32561 строка в 15 столбцах
print(data.columns)                            # возвращает название столбцов
print(data.info())                             # общая информация по дата фрейму
"""
data['Sex'] = data['Sex'].astype('int64')
"""
data.describe()                                # общая стата по основным числовым характеристикам
data.describe(include=['object', 'bool'])      # возвращает статистику по нечисловым признакам
data['sex'].value_counts()                     # распределение данных по переменной sex
data.sort_values(by='sex',                     # сортировка по признаку sex (наверное это правильно)
    ascending=False).head()                    # ascending=False для сортировки по убыванию 

 
import pandas as pd      
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = (10, 8)
import pandas as pd
import numpy as pr
data = pd.read_csv("J:/HiEnd/mlcourse_open-master/mlcourse_open-master/data/adult.data.csv")
data.head()                                    # возвращает первые 5 строк из файла - просто проверяем.
print(data.shape)                              # возвращает (32561, 15) - 32561 строка в 15 столбцах
print(data.columns)                            # возвращает название столбцов
print(data.info())                             # общая информация по дата фрейму
data.describe()                                  # общая стата по основным числовым характеристикам 
""" проведём сортировку датафрейма по числовм признакам, используем метод сортировки по убиванию ascending=False """ 
data.sort_values(by="age",                       # сортировка по признаку Age
        ascending=False).head()     
data.sort_values(by="fnlwgt",                    # сортировка по признаку fnlwgt
        ascending=False).head() 
data.sort_values(by="education-num",             # сортировка по признаку education-num 
        ascending=False).head() 
data.sort_values(by="capital-gain",              # сортировка по признаку capital-gain 
        ascending=False).head() 
data.sort_values(by="capital-loss",              # сортировка по признаку capital-loss 
        ascending=False).head() 
data.sort_values(by="hours-per-week",            # сортировка по признаку hours-per-week 
        ascending=False).head() 
data.describe(include=['object', 'bool'])         # возвращает статистику по нечисловым признакам
""" проведём сортировку датафрейма по нечисловм признакам, используем метод сортировки по убиванию ascending=False """
data.sort_values(by="workclass",                       # сортировка по признаку workclass
        ascending=False).head() 
data.sort_values(by="education",                       # сортировка по признаку education
        ascending=False).head() 
data.sort_values(by="marital-status",                  # сортировка по признаку marital-status
        ascending=False).head() 
data.sort_values(by="occupation",                      # сортировка по признаку occupation
        ascending=False).head()
data.sort_values(by="relationship",                    # сортировка по признаку relationship
        ascending=False).head() 
data.sort_values(by="race",                            # сортировка по признаку race
        ascending=False).head()
data.sort_values(by="sex",                             # сортировка по признаку sex
        ascending=False).head() 
data.sort_values(by="native-country",                  # сортировка по признаку native-country
        ascending=False).head()  
data.sort_values(by="salary",                          # сортировка по признаку salary
        ascending=False).head()  
""" посмотрим на распределение данных в отношении объектов датафрейма"""
data['sex'].value_counts()                             # вывод чисел по признаку Sex 
data['workclass'].value_counts()                       # вывод чисел по признаку workclass 
data['education'].value_counts()                       # вывод чисел по признаку education 
data['marital-status'].value_counts()                  # вывод чисел по признаку marital-status 
data['occupation'].value_counts()                      # вывод чисел по признаку occupation
data['relationship'].value_counts()                    # вывод чисел по признаку relationship
data['race'].value_counts()                            # вывод чисел по признаку race
data['native-country'].value_counts()                  # вывод чисел по признаку native-country
data['salary'].value_counts()                          # вывод чисел по признаку salary
""" посмотрим на распределение данных по числовым объектам """
data['age'].value_counts()                             # вывод чисел по признаку age
data['fnlwgt'].value_counts()                          # вывод чисел по признаку fnlwgt
data['education-num'].value_counts()                   # вывод чисел по признаку education-num 
data['capital-gain'].value_counts()                    # вывод чисел по признаку capital-gain 
data['capital-loss'].value_counts()                    # вывод чисел по признаку capital-loss 
data['hours-per-week'].value_counts()                  # вывод чисел по признаку hours-per-week 
""" отсортируем столбцы датафрейма по группе столбцов 'sex', 'workclass - True == female, False == male"""
data.sort_values(by=['sex', 'workclass'],                # сортировка по группе столбцов в отношении Female
        ascending=[True, False]).head()
data.sort_values(by=['sex', 'workclass'],                # сортировка по группе столбцов в отношении Male
        ascending=[False, False]).head()
""" процедура извлечения данных (индексации) из отдельных столбцов, рабоатет только с численными типами объектов """
data['age'].mean()                                       # средний возвраст 38.58164675532078
data['fnlwgt'].mean()                                    # 189778.36651208502 
data['education-num'].mean()                             # 10.0806793403151
data['capital-gain'].mean()                              # 1077.6488437087312
data['capital-loss'].mean()                              # 87.303829734959
data['hours-per-week'].mean()                            # 40.437455852092995
""" процедура извлечения логической индексации из отдельных столбцов, рабоатет только с НЕчисленными типами объектов """
data['workclass'] = data['workclass'].astype('bool') 
data['workclass'] = data['workclass'].astype('int64')   
data[data['workclass'] == 1].mean()   
data['education'] = data['education'].astype('bool') 
data['education'] = data['education'].astype('int64')   
data[data['education'] == 1].mean()   
data['marital-status'] = data['marital-status'].astype('bool') 
data['marital-status'] = data['marital-status'].astype('int64')   
data[data['marital-status'] == 1].mean()   
data['occupation'] = data['occupation'].astype('bool') 
data['occupation'] = data['occupation'].astype('int64')   
data[data['occupation'] == 1].mean()          
data['relationship'] = data['relationship'].astype('bool') 
data['relationship'] = data['relationship'].astype('int64')   
data[data['relationship'] == 1].mean()    
data['race'] = data['race'].astype('bool') 
data['race'] = data['race'].astype('int64') 
data[data['race'] == 1].mean()
data['sex'] = data['sex'].astype('bool') 
data['sex'] = data['sex'].astype('int64') 
data[data['sex'] == 1].mean()
data['native-country'] = data['native-country'].astype('bool') 
data['native-country'] = data['native-country'].astype('int64')   
data[data['native-country'] == 1].mean()
data['salary'] = data['salary'].astype('bool') 
data['salary'] = data['salary'].astype('int64')   
data[data['salary'] == 1].mean()
"""data[data['workclass'] == 0].mean() и другие строки с == 00 возвращают - NaN (None) типа нету такого объекта """ 
data.apply(pr.max)                             # ищет и возвращает аккаунт с максимальными значения по всему датафрейму 
data.apply(pr.min)                             # ищет и возвращает аккаунт с минимальными значения по всему датафрейму
data.loc[0:5, 'sex':'salary']                  # возвращает значение 6 строк в столбцах от sex до salary
data.loc[0:5, 'age':'race']                    # возвращает значение 6 строк в столбцах от age до race
data[100:101]                                  # возвращает 100 строку датафрейма
"""посмотрим максимальные значения датафрейма по числовым признакам, с нечисловыми типами естественно не работает"""
data['age'].max()                              # возвращает 90
data['fnlwgt'].max()                           # 1484705
data['education-num'].max()                    # 16
data['capital-gain'].max()                     # 99999
data['capital-loss'].max()                     # 4356
data['hours-per-week'].max()                   # 99
"""data['salary'].max()/min() - возвращет 1 поскольку это объект, а не int64 == даже если преобразовать .astype"""
