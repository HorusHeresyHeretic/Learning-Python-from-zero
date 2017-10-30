len(str(2 ** 1000000)) # сколько цифр в действительно большом числе?

import math            # загрузить встроенный модель математики
math.pi                # обратиться к атрибуту pi внутри модуля.

import random                   # загрузить модуль случайных числе
random.random()                 # обратиться к атрибуту внутри молуля
random.choice([2,3,4,5,6,7])    # задать варианты выбора с помощью списка.

anime = "Ghost"                 # переменная = строка: последовательность односимвольных строк
len(anime)                      # len - возвращает длинны последователньости
anime[0]                        # переменная[0] - возврат первого символа последователньости
anime[1]                        # переменная[1] - возврат второго символа последователньости
anime[-1]                       # последний элемент в конце
anime[-2]                       # предпоследний эелемент
anime[-1]                       # Формально отрицательные индексы складываются с длиной строки
anime[len(anime)-1]             # Отрицательная индексация - эквивалентна anime[-1]
 
# внутри квадратных скобок допускается использовать не только жестко заданные числовые литералы,
# но и любые другие выражения – везде, где Python ожидает получить значение, можно использовать
# литералы, переменные или любые выражения. Весь синтаксис языка Python следует этому принципу.

anime = "Ghost"                # строка из 5 символов
anime[1:3]                     # срез строки с 2 по 3
anime[1:]                      # всё кроме первого элемента (1:len(anime))
anime                          # вся строка без изменений
anime[0:4]                     # всё кроме последнего символа
anime[:4]                      # тоже самое что и anime[0:4]
anime[:-1]                     # ещё раз, всё кроме последнего эелемента, но проще (0:-1)
anime[:]                       # всё содержимое, как обычная копия (0:len(anime))

anime = "Ghost"                # запись строки
anime + anime                  # коннетация строки
anime * 8                      # повторение строки 8 раз

anime = "Ghost"
anime[0] = "z"                 # неизменяемые объекты нельзя изменить.
anime = "z" + anime[0:]        # но с помощью выражений можно создать новые объекты
anime                          # возвращает zGhost

anime = "Ghost"                
anime.find("st")               # возвращает 3 - порядковый номер в индексе с начала подстроки 
anime.replace("ost","11")      # (old,new) замена подстроки ost на подсктроку 11, возвращает Gh11
anime.replace("Gh", "seven")   # (!) замена подстроки Gh на подстроку seven - возвращает sevenost
 
# независимо от имен этих строковых методов, мы не изменяем оригинальную строку, а создаем новую

anime = "aaa,bbb,ccc,xxx"     # разбивает строку по разделителю и создаёт список из этих строк
anime.split(",")              # возвращает ["aaa","bbb","ccc","xxx"]
anime.upper()                 # преобразование в верхний регистр
anime.isalpha()               # проверка содержимого по типу (возвращает false - не по алфавиту)

# anime.is...()               # вызов встроенных методов роверки переменно # смотри name.is...() 

anime = "aaa,bbb,ccc,xxx,dd\n" 
anime = anime.rstrip()        # удаляет завершающие пробельные символы (-+/* ит.п.)
anime                         # возвращает 'aaa,bbb,ccc,xxx,dd'

# anime.comandname()          # куча встроенных методов вылезает по нотации anime.

anime = "aaa,bbb,ccc,xxx,dd\n" 
anime.title()                 # например преобразует шрифт заглавных символов

anime = "Ghost in the shell"  # ниже - моя попытка отформатировать строку
"{0}, Major, and {1}".format("Ghost int the shell", "soul")
dir(anime)                    # возвращает список атрибутов и методов объекта
help(anime.format)

anime = "A\nB\tC"             # \n - это смивол "конец строки" \t - символ табуляции
len(anime)                    # возвращает - 5, \n и \t соотвествуют единственному символу

ord('\n')                     # возвращает 10; В ASCII \n – это байт с числовым значением 10

anime = 'A\0B\0C'             # \0 – это двоичный ноль, не является завершителем строки
len(anime)                    # возвращает 5
anime                         # возвращает 'A\x00B\x00C'

anime = """ Ghost in the shell
Final Fantasy Naruto """     # перед Final Fantasy вернёт \n - символ конца строки 
anime                        # возвращает ' Ghost in the shell\nFinal Fantasy Naruto '

Major = "Ghost in the shell" 
import re                    # загрузка встроенного модуля re - поиск по шаблону в строке
match = re.match("Ghost[ \t]*(.*)shell", "Ghost in the shell")
print(match)                 # <_sre.SRE_Match object; span=(0, 18), match='Ghost in the shell'>
match.group(0)               # возвращает 'Ghost in the shell'
match.group(1)               # возвращает искомую подстроку  'in the '

anime = [11, "Ghost", 11.11] # список из 3х объектов разных типов: числа, строки, числа с точкой
len(anime)                   # возвращает 3
anime[0]                     # обращение к первому индексу в списке - возвращает 11
anime[:-1]                   # получение среза, возвращает новый список [11, 'Ghost']
anime + [404, "Major"]       # коннетация, возвращает список [11, 'Ghost', 11.11, 404, 'Major']
anime.append("Shell")

anime = [11, "Ghost", 11.11] 
anime.append("Shell")        # увеличение, в конце списка добавляется новый объект
anime                        # возвращает [11, 'Ghost', 11.11, 'Shell']
anime.pop(2)                 # уменьшение, удалет объект из списка по номеру индекса в сбоках
anime                        # возвращает [11, 'Ghost', 'Shell']
del anime[0]                 # аналог pop
anime                        # врзвращает ['Ghost', 'Shell']

anime = ["xx", "yy", "aa", "bb"]
anime.sort()                 # сортировка по алфавиту (по умолчанию - сортирует по возрастанию )
anime                        # возвращает ['aa', 'bb', 'xx', 'yy']

anime = ["xx", "yy", "aa", "bb"]
anime.reverse()              # сортировка по убыванию
anime                        # возвращает ['bb', 'aa', 'yy', 'xx']
anime[99]                    # возвращает list index out of range
anime[99] = 1                # возвращает list assignment index out of range

# нельзя присвоить переменную тому - чего нет: в последовательности нет объекта - 99 индекса

anime = [[11, 404, 11],     # матрица 3х3 в виде вложенных списков
         [11, 404, 11],
         [404, 11, 11]]
anime                       # возвращает  [[11, 404, 11], [11, 404, 11], [404, 11, 11]]
anime[1]                    # вернуть строку 2
anime[1][2]                 # вернуть строку 2, элемент 3
col2 = [row[1] for row in anime]
col2                        # возвращает [404, 404, 11]
anime                       # матрица не изменилась
col3 = [shell[1] + 1 for shell in anime]
col3                        # возвращает [405, 405, 12] 
col4 = [shell[1] for shell in anime if shell[1] % 2 == 0]
col4                        # возвращает [404, 404]
diag = [anime[i][i] for i in [0, 1,2 ]]
diag                        # возвращает выборку элементов диагонали матрицы [11, 404, 11]

doubles = [c * 2 for c in 'Ghost']
doubles                     # возвращает  ['GG', 'hh', 'oo', 'ss', 'tt']


anime = [[11, 404, 11],     # матрица 3х3 в виде вложенных списков
         [11, 404, 11],
         [404, 11, 11]]
g = (sum(row) for row in anime) 
next(g)                    # возвращает суммы элементов строк - 426
list(map(sum, anime))      # возвращает [426, 426, 426]

anime = [[11, 404, 11],[9, 9, 9]]
g = (sum(row) for row in anime)
next(g)                    # возвращает суммы элементов строк - 426
list(map(sum, anime))      # возвращает [426, 27]

list(map(sum, anime))      # вернуть сумму из объекта, указанного после запятой

anime = [[11, 404, 11],[9, 9, 9]]
{sum(shell) for shell in anime}        # создать " множество " сумм строк
{i : sum(anime[1]) for i in range(2)}  # создать таблицу из пар "ключ - значение" из суммы строк

anime = [[11, 404, 11],[9, 9, 9]]
{sum(shell) for shell in anime}        # range(x) - где х это число пар
{i : sum(anime[1]) for i in range(3)}  # возвращает {0: 27, 1: 27, 2: 27}
{i : sum(anime[0]) for i in range(4)}  # возвращает {0: 426, 1: 426, 2: 426, 3: 426}

[ord(x) for x in 'anime']              # возвращает список кодов символов в строке
[ord(x) for x in 'Ghoost']             # возвращает [71, 104, 111, 115, 116]
{ord(x) for x in 'Ghoost'}             # множества ликвидируют дубликаты (дубликаты кодов)
{x: ord(x) for x in "Ghost"}           # возвращает уникальные ключи своварей (это просто супер)

magic = { "fire": "damage", "target": 3, "color": "red"}
magic["fire"]                         # возвращает 'damage' - значение связанное с ключом fire.
magic["target"] += 1                  # возвращает 4 - прибываить 1 к значению ключа 'target'

magic = {}                            # создание пустого словаря
magic["fire"] = "damage"              # запись пары: ключ - значение
magic["target"] = 3
magic["color"] = "red"
magic                                 # возрв. {'fire': 'damage', 'color': 'red', 'target': 3}
print(magic["color"])                 # возвращает red - значение по нотации (словарь["ключ"])


anime = {'Major': {'Ghost': "Shell", "Stand": "Alone"},
         "Name": ["Kusanagi", "Motoka"],
         'age': 99.9}
anime["Major"]                       # возвращает {'Stand': 'Alone', 'Ghost': 'Shell'}
anime["Major"]["Stand"]              # обращение к элементу вложенного словаря, возрв. 'Alone'
anime["Name"]                        # возвращает вложенный список ['Kusanagi', 'Motoka']
anime["Name"][1]                     # возвращает элемент вложенного списка  'Motoka'
anime["Name"].append("Virus")        # расширяет вложеный список
anime                                # возвращает
anime = 0                            # очищает память занимаемую предыдущим объектом.

# {'Major': {'Ghost': 'Shell', 'Stand': 'Alone'}, 'Name': ['Kusanagi', 'Motoka', 'Virus'], 'age': 99.9}
    
D = {"a": 1, "b": 2, "c": 3}
Ks = list(D.keys())                  # создание неупорядоченного списка ключей из словаря
Ks.sort()                            # сортировка списка ключей по алфавиту
Ks                                   # возвращает ['a', 'b', 'c']
for key in Ks:                       # обход списка ключей
    print(key, "=", D[key])          

# История про маленький паравозик, который не зря читает Лутца и смог в гибкость данных. 

[ord(z) for z in 'Ghost in the shell, Stand Alone Complex, Post traumatic syndrome']    # возвращает список кодов в строке 'Ghost in the shell, Stand Alone Complex, Post traumatic syndrome'
{ord(z) for z in 'Ghost in the shell, Stand Alone Complex, Post traumatic syndrome'}    # ликивдирует дубликаты - возвращает только уникальные универсальные коды
{z: ord(z) for z in 'Ghost in the shell, Stand Alone Complex, Post traumatic syndrome'} # возвращает уникальные ключи словаря
anime = {'l': 108, ',': 44, 'n': 110, 'P': 80, 'C': 67, 'i': 105, 's': 115, 't': 116, 'A': 65, 'p': 112, 'c': 99, 'x': 120, 'S': 83, ' ': 32, 'a': 97, 'm': 109, 'y': 121, 'h': 104, 'o': 111, 'G': 71, 'd': 100, 'e': 101, 'r': 114, 'u': 117}
story = list(anime.keys())                                                              # создаёт неупорядоченный список ключей внутри новой переменной story
story.sort()                                                                            # сортировка списка ключей (необязательно, но упрощает чтение списка)
story                                                                                   # читаем объект
{x: ord(x) for x in story}                                                              # мы запращиваем ключи из списка story, а Python возвращает ключи из словаря anime (!)
for key in story:                                                                       # обход отсортированного списка ключей (необязательно, но упрощает чтение списка) 
    print(key, "=", anime[key])                                                                                         
anime["A"] = "Major"                                                                    # Майор атакует данные - она любит это делать
anime['n'] = "Major"                                                                    # Майор атакует данные - она любит это делать
anime['i'] = "Major"                                                                    # Майор атакует данные - она любит это делать
anime['m'] = "Major"                                                                    # Майор атакует данные - она любит это делать
anime['e'] = "Major"                                                                    # Майор атакует данные - она любит это делать
for key in story:                                                                       # обход отсортированного списка ключей (необяхательно, но упрощает поиски следов Майора) 
    print(key, "=", anime[key])
story                                                                                   # возвращает список 
anime                                                                                   # возвращает словарь 
type(story)                                                                             # это список
type(anime)                                                                             # это словарь                                                                                        

# Python расшифровал строку "Ghost in the shell, Stand Alone Complex, Post traumatic syndrome" в код, упаковал её в словарь и позволил обратиться к пространсту имён внутри словаря с помощью переменной типа List.
# В результате команда {x: ord(x) for x in story} вернула результат свойственный словарю, а не списку - которым на тот момент является переменная story - по факту я написал модуль ядра бибилиотеки переводчика.
# В бибилиотеки нет имён - только данные строчного типа, которые могут быть записаны из вне, за доступ к данным отвечает переменная типа list которая может быть импортированна в сценарий верхнего уровня.  

D = {"a": 1, "c": 3, "b": 2,}
for key in sorted(D):                 # использование втроенной функции sorted упрощает код
    print(key, "=", D[key])

for shell in 'anime':                 # обойти все символы в строке anime
    print(shell.upper())              # вывести все символы в верхнем регистре
                       
anime = 4                             
while anime > 0:                      # пока anime больше 0 
    print("shell" * anime)            # печатать строку shell помноженную на значение переменной anime
    anime -=1                         # с каждым следующем шагом отнимать от значение переменной anime 1


anime = 4                             
while anime > 0:                      # пока anime больше 0 
    print("shell" * anime)            # печатать строку shell помноженную на значение переменной anime
    anime -= 1                        # хитрая штука, которая предотващает бесконечное воспроизведение

# если в команде anime - = 1  убрать (-) - цикл будет выполняться бесконечно, значение перемнной - шаг.

cub = [x ** 2 for x in [1,2,3,4,5]]   # генератор списков - который вычисляет квадраты чисел в списке
cub                                   # возвращает [1, 4, 9, 16, 25]

cub = []                              # создание спика
for x in [1,2,3,4,5]:                 # создание списка чисел в списке cub
    cub.append(x**2)                  # вычисление согласно протоколу интераций (слева направо)
cub                                   # возвращает [1, 4, 9, 16, 25]

D = {"a": 1, "c": 3, "b": 2,}
for key in sorted(D):                 # использование втроенной функции sorted упрощает код
    print(key, "=", D[key])
'F' in D                              # проверяю наличие ключа "F" в словаре D - возвращает False
if not "F" in D:                      # аналог in - принцип тотже, работает через true\false
    print("error")
value = D.get("c", 0)                 # попытка получить значение, указав значение по умолчанию
value                                 # возвращает 3; если указать ("x", 0) - возвращает 0
value = D["a"] if "a" in D else 0     # аналог .get через if - обходит слева направо 
value                                 # возвращает значение ключа "a" - возвращает 1
value = D["x"] if "x" in D else 7     # обходит слева направо, провераяет true\false 
value                                 # возаращает значение ключа "x" - возаращает 7

#  D.get("c", 0) и D["x"] if "x" in D else 7  - используют значения, присовенные по умолчанию == 0 и 7

anime = (1,2,3,4,5,11)                # кортеж
len(anime)                            # 6 
type(anime)                           # <class 'tuple'>
anime + anime                         # возвращает (1, 2, 3, 4, 5, 11, 1, 2, 3, 4, 5, 11)
anime[0]                              # возвращает 1
shell = anime + anime
shell                                 # возвращает (1, 2, 3, 4, 5, 11, 1, 2, 3, 4, 5, 11)
shell + (44, 404)
shell                                 # возаращает (1, 2, 3, 4, 5, 11, 1, 2, 3, 4, 5, 11)

# при операции коннетации shell + (44, 404) исходный кортеж shell остаёться неизменным. 

anime = (1,2,3,4,5,11)  
anime.index(4)                        # значение 4 находиться в позиции 3
anime.index(11)                       # значение 11 находиться в позиции 5
anime.count(11)                       # значение 11 присуствует в единственном экземпляре

anime = ("Major", 2.0, [11, 404, "Ghost"])   # тот же список - только его изменять нельзя
anime[1]                                     # возвращает 2.0
anime[-1]                                    # возвращает [11, 404, 'Ghost']
anime[2][0]                                  # возвращает  11
anime[2][-1]                                 # возвращает 'Ghost'
anime.append(4)                              # возвращает исключение: объект кортеж является неизменяемым

anime = open("data.txt", "w")        # создание файла data.txt для вывод - "w"
anime.write("Hello\n")               # запись строки байтов в файл - возвращает 6
anime.write("Ghost in the shell")    # возвращает 18  
len("Ghost in the shell")            # 18
anime.close()                        # закрывает файл и выталкивает выходные буферы на диск

# 28.03.2017 в нижеуказанном каталоге появился файл data.txt
# файл содержит две записи: 1 строка - Hello; 2 строка -  Ghost in the shell
# C:\Users\Battlestation\Documents\Visual Studio 2015\Projects\PythonApplication1\PythonApplication1

anime = open("data.txt")             # без указания режима доступа
text = anime.read()                  # читать файл целиком в строку
text                                 # возвращает 'Hello\nGhost in the shell'
print(text)                          # вывод ( с попутной интерпретацией слежубных символов)

anime = open("data.txt", "r")        # ‘r’ – это режим доступа к файлу по умолчанию 
text = anime.read()                  # читать файл целиком в строку
text                                 # возвращает 'Hello\nGhost in the shell'
print(text)                          # вывод ( с попутной интерпретацией слежубных символов)
text.split()                         # содержимое файла всегда является строкой - возвращает .str
text = anime.readline()

anime = open("data.bin", "w")        # создание файла data.bin для вывод в режиме - "w" (write)
anime.write("Hello\n")               # запись строки байтов в файл - возвращает 6
anime.write("Ghost in the shell")    # возвращает 18  
len("Ghost in the shell")            # 18
anime.close()
 
anime = open("data.bin", "rb").read()# открыть файл data.bin в режиме - чтения байтов rb, прочитать всё()    
anime                                # возвращает b'Hello\r\nGhost in the shell'
anime[4:8]                           # возвращает b'o\r\nG'

anime = set("Ghost int the shell")   # создание множества через встроенную фукнцию set
anime                                # возвращает {'i', 't', 'n', 'e', 'l', ' ', 'h', 'o', 'G', 's'}
shell = {"E","l","e","v","e","n"}    # в версии 3.0+ можно определять литераты множеств
anime,shell                          # возвращает - ({'h', 'n', 'i', 'l', 't', ' ', 'G', 'e', 's', 'o'}, {'e', 'n', 'E', 'v', 'l'})
anime&shell                          # пересечение: возвращает {'e', 'l', 'n'}
anime|shell                          # объединение - возвращает {'h', 'E', 'n', 'v', 'i', 'l', 't', ' ', 'G', 'e', 's', 'o'}
anime - shell                        # разность - возвращает {'G', 'h', 'o', 'i', 't', ' ', 's'}

{x**2 for x in [1,2,3,4,5]}          # генератор множеств, возвращает {16, 1, 4, 9, 25}

1 / 3                                # возвращает  0.3333333333333333
(2/3) + (1/2)                        # возвращает  1.1666666666666665

import decimal                       # запуск модуля вещественные числа с фиксированной точностью
data = decimal.Decimal("3.141")      # запуск конструктора, см. PartV c 555 
data + 1                             # возвращает Decimal('4.141')

import decimal 
decimal.getcontext().prec = 13                      # = x - количество знаков после запятой
decimal.Decimal("1.00") / decimal.Decimal("3.00")   # возвращает  Decimal('0.3333333333333')

from fractions import Fraction       # рациональные числа - числитель и знаменатель
data = Fraction(2,3)                 # 
data + 2                             # возвращает Fraction(8, 3)  ( data + x = 2 + 3 * x)
data + Fraction(1,1)                 # возвращает Fraction(5, 3)  (!моя не понимает это!)

1 > 2, 2 > 1                         # возвращает (False, True)
bool("anime")                        # возвращает True 

x = None
print(x)                             # возвращает None

L = [None] * 100
L                                    # возвращает 100 объектов None

anime = [11, "Major", "shell", 404]  # список для примера про гибкость кода: с.148
type(anime)                          # возвращает <class 'list'>   - "список" это класс
type(type(anime))                    # возвращает <class 'type'>   - "тип" это класс
if type(anime) == type([]):          # проверка класса объекта: если объект anime это список, тогда
    print("Yes")                     # возвращает Yes
if type(anime) == type({}):          # если объект anime это словарь, тогда 
    print("Yes")
else:
    print("NO")                      # возвращает NO

anime = [11, "Major", "shell", 404]  # список для примера про гибкость кода: с.148
type(anime)                          # возвращает <class 'list'>   - "список" это класс
type(type(anime))                    # возвращает <class 'type'>   - "тип" это класс
if type(anime) == type([]):          # проверка класса объекта: если объект anime это список, тогда
    print("Yes")                     # возвращает Yes
if type(anime) == type({}):          # если объект anime это словарь, тогда 
    print("Yes")
elif type(anime) == type(()):
    print("append")
elif type(anime) == str:             # проверка и использованием имени типа объекта - строки
    print("str")
elif type(anime) == int:             # проверка и использованием имени типа объекта - числа
    print("int")
else:
    print("NO")                      # возвращает NO
if isinstance(anime, list):          # проверка в объекто-ориентированном стиле
    print("Yes")                     # возвращает YES

class anime:                         # задаём имя класса
    def __init__(self, name, story, pay):              # инициализация при создании, self это сам объект 
        self.name = name                               # атрибут name
        self.story = story                             # атрибут story
        self.pay = pay                                 # атрибут pay
    def LastName(self):                  # метод 
        return self.name.split()[-1]     # описание поведения объекта свойсвтенному классу в рамках метода
    def LastStory(self):                 # метод
        return self.story.split()[-1]    # разбить строку по символам пробела 
    def Payment(self, percent):          # метод
        self.pay *= (1.0 + percent)      # обновить сумму выпла на %, размер % необходмио будет указать
Major = anime("Matoko Kusanagi", "Stand Alone Complex", 111)
Lina = anime("Lina Inverse", "Dragon Slayer", 404)
Celcia = anime("Elven Princess", "Talking Dog", 10)
Major.name                           # возвращает 'Matoko Kusanagi'
Major.story                          # возвращает 'Stand Alone Complex'
Major.pay                            # возвращает  111
Major.LastName()                     # возвращает  'Kusanagi'
Lina.LastStory()                     # возвращает  'Slayer'
Celcia.Payment(.10)                  # указываем процент на который необходимо увеличить оплату (.x) 
Celcia.pay                           # возвращает 11.0
type(anime)                          # возвращает <class 'type'>
type(Major)                          # возвращает <class '__main__.anime'>

 