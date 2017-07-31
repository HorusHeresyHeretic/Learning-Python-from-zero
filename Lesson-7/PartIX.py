
anime = ()
type(anime)                        # <class 'tuple'> - это кортеж

anime = (1,)                       # Кортеж из одного элемента (не выражение)
print(anime)                       # (1,)

anime = (1, "Stand alone", 1.2, 4) # Кортеж из четырех элементов
print(anime)                       # (1, 'Stand alone', 1.2, 4)

anime = 1, "Ghost shell", 1.2, 5   # по факту кортежи можно записывать без скобок
anime                              # (1, 'Ghost shell', 1.2, 5)

anime = 1, ("manga"), 1.2, 5       # но без скобок не получается вложенности, см следующую строку аниме
anime                              # (1, 'manga', 1.2, 5)

anime = (1, ("manga", 1.2), 5)     # не знаю почему, но вложенный кортеж получаеться только с двумя элементами
anime                              # (1, ('manga', 1.2), 5)

""" а не получаеться потому, что внутри скобок нужно ставить запятую после первого элемента """

T = ("abc", ("def",), "ghi")       # вложенные кортежи 
T                                  # ('abc', ('def',), 'ghi')

anime = (1, ("manga",), 1.2, 5)    # запятая - решает все проблемы
anime                              # (1, ('manga',), 1.2, 5)

anime = tuple("Motoka Kusanagi")   # создание кортежа из интерируемого объекта
print(anime)                       # ('M', 'o', 't', 'o', 'k', 'a', ' ', 'K', 'u', 's', 'a', 'n', 'a', 'g', 'i')
anime[0]                           # 'M'
anime[1]                           # 'o'
anime[0:5]                         # ('M', 'o', 't', 'o', 'k')


T = ("abc", ("def",), "ghi")       
T[0][0]                            # 'a'
T[0][1]                            # 'b'
T[0][2]                            # 'c'
T[1][0]                            # 'def'
T[2][0]                            # 'g' 
T[2][1]                            # 'h'
T[2][2]                            # 'i'
T[1][0][0]                         # 'd'
T[1][0][1]                         # 'e'
T[1][0][2]                         # 'f'

anime = tuple("Motoka Kusanagi")   # создание кортежа из интерируемого объекта
T = ("abc", ("def",), "ghi")
anime + T                          # операция коннетации работает, возвращает

# ('M', 'o', 't', 'o', 'k', 'a', ' ', 'K', 'u', 's', 'a', 'n', 'a', 'g', 'i', 'abc', ('def',), 'ghi')

T = ("abc", ("def",), "ghi")      # операция повторения работает, возвращает 
T * 3                             # ('abc', ('def',), 'ghi', 'abc', ('def',), 'ghi', 'abc', ('def',), 'ghi')

anime = tuple("Motoka Kusanagi")  # операция обхода в цикле работает, возвращает годноту
for i in anime: print(i)

anime = tuple("Motoka Kusanagi")  # проверка на вхождение работает
"Ghost" in anime                  # вовзвращает False

T = ("abc", ("def",), "ghi")      # генератор списков тоже работает на основании правила методов - раз тип объекта доступен методу = работает
[x * 2 for x in T]                # ['abcabc', ('def', 'def'), 'ghighi']


anime = tuple("Motoka Kusanagi")  # подсчёт вхождений тоже работает
anime.count("Ni")                 # 0
anime.count("ka")                 # 0
anime.count("a")                  # 3

# ещё должен быть anime.index

anime = (1, "Stand alone", 1.2, 4)
anime.index("Stand alone")       # 1
anime.index("Ghost")             # tuple.index(x): x not in tuple 

# кортеэи в действии по Лутцу.

anime = (1, 2) + (3, 4)          # коннетация
anime                            # (1, 2, 3, 4)

anime = (1, 2, 5) * 3            # повторение
anime                            # (1, 2, 5, 1, 2, 5, 1, 2, 5)

anime = (11, 501, "Ghost", "Shell")
print(anime)                     # кортеж (11, 501, 'Ghost', 'Shell')
anime = list(anime)
anime                            # список [11, 501, 'Ghost', 'Shell']
try:
    anime.sort()                 # unorderable types: str() < int()
except TypeError:
    print(anime)

anime = (11, 501, 404, 00)
print(anime)                    # (11, 501, 404, 0)
anime = list(anime)             # делаем список из кортежа, спасибо системе Питон по разименованию ссылок 
anime.sort()                    # сортируем список
anime                           # возвращает [0, 11, 404, 501]
anime = tuple(anime)            # делаем кортеж из отсортированного нами списка
anime                           # вовзаращет (0, 11, 404, 501)

anime = (11, 501, 404, 00)      # или используем новую фукнцию sorted(x) которая умеет работать со всем
sorted(anime)                   # [0, 11, 404, 501] 


anime = (11, 501, 404, 00)      # аниме - ссылка на объект "кортеж" в системной таблице 
anime = list(anime)             # аниме - ссылка на объект "список" в системной таблице
anime                           # ссылка аниме на объект "кортеж" была разименованна.

anime = (11, 501, 404, 00)     
ghost = [i + 20 for i in anime] # использование генератора списков с объектами кортежа
ghost                           # [31, 521, 424, 20]

anime = (11, 501, 11, 501, 404, 11, 11)
anime.index(11)                 # первое вхождение находиться на первой позиции - возвращает 0
anime.index(501)                # второе вхождение находиться на второй позиции - возвращает 1
anime.index(11, 2)  

anime = (11, 501, 11, 501, 404, 11, 11)
anime.index(11, 2)             #  2  - второе вхождение по индексу "11" находиться на 3ий позиции
anime.index(11, 3)             #  5  - третье вхождение по индексу "11" находиться на 6ой позиции
anime.index(11, 4)             #  5  - интересный случай: сдоенная позиции вхождения по 11 индексу
anime.index(11, 6)             #  6  - четвёртое вхождение по индексу "11" находиться на 7ой позиции


anime = (11, 501, 11, 501, 404, 11, 11)
anime.count(11)                # возвращает 4
anime.count(501)               # возвращает 2


anime = (11, 501, [11, 501], 404, 11, 11)
anime[0]                       #  возвращает элемент кортежа - возвращает 11, этот элемент нельзя измениьь
anime[1]                       #  возвращает элемент кортежа - возвращает 501  и его нельзя изменить тоже
anime[2]                       #  возвращает список - возвращает [11, 501], список можно имзенять.
anime[2] = [11]                #  возвращает исключение 'tuple' object does not support item assignment
anime[2][0] = 501
anime                          #  возвращает (11, 501, [501, 501], 404, 11, 11)
anime[2][1] = "Ghost"
anime                          #  (11, 501, [501, 'Ghost'], 404, 11, 11)

"""супер ценные команды по работе с файлам"""

# output открывает файл для записи

output = open(r"C:\\Users\\Battlestation\\Documents\\Visual Studio 2015\\Projects\\PythonApplication1\\PythonApplication1\\anime.py", "w")

input = open("anime.py", "r")  # открывает файл для чтения
input = open("anime.py")       # тоже самое, режим "r" всегда используеться по умолчанию

# создаём новый текстовый файл по Лутцу

myfile = open("myfile.txt", "w")             # открывает файл (создаёт, очищает)
myfile.write("Ghost in the shell file\n")    # записывает строку текста
myfile.write("Stand Alone complex end\n")    # записывает ещё одну строку
myfile.close()                               # выталкивает выходные буферы на диск


myfile = open("myfile.txt")                  # открывает файл, режим чтение "r" по умолчанию
myfile.readline()                            # читает, возвращает 'Ghost in the shell file\n' 
myfile.readline()                            # читает, возвращает 'Stand Alone complex end\n'
myfile.readline()                            # читает, возвращает пустую строку (типа конец) - ''

# не уидивительно что в файле 50 байт, 2 раза по 24 символа + 2символа пустой строки = 50


myfile = open("myfile.txt")  
myfile.readline(0)                           # возвращает ''
myfile.readline(1)                           # возвращает 'G'
myfile.readline(0-24)  

myfile = open("myfile.txt")  
myfile.readline(0-24)                        # возвращает 'Ghost in the shell file\n'

open("myfile.txt").read()                    # прочитать файл целиком в одну строку 

print(open("myfile.txt").read())             # дружбомагия чтения файла в одну строку 
   
for line in open("myfile.txt"):              # использование интератора для чтения файла
    print(line, end = "")

# учимся работать с файлами, слева ссылка - справа комнады на чтение и имя файла, содержимое по ссылке.

for line in open("ghost1.py"):              # использование интератора для чтения файла
    print(line, end = "")                   # возвращает весь файл построчно, с сохранением структуры

print(open("ghost1.py").read())             # также возвращает весь файл построчно, со структурой

myfile = open("ghost1.py")                  # myfile - это ссылка на объект, имя ссылки может быть любым
myfile.readline()                           # возвращает "Ghost = 'Ghost'\n"

for line in open("ghost1.py", encoding="latin-1"):
    print(line, end = "")                   # возвращает кракозябры в комментах

for line in open("ghost1.py", "rb"):
    print(line, end = "")                   # возвращает лютую хуйю в байтах с использованием экранирования

input = open("ghost1.py")                   # input - это ссылка на объект, имя ссылки может быть любым
aString = input.read()                      # aString - это имя ссылки на объекты файла, которые читаем
aString                                     # возвращает всё сожержимое файла в строку с экранированием

input = open("ghost1.py")
file = input.read()                         # чтение файла в единственную строку
file                                        # возвращает содержимое файла строкой
file = input.read(11)                       # чтение 11 символов 9или 11 байтов) в строку
file                                        # возвращает ''

# судя по всему нельзя  просто так спамить Питон командами на чтение и иногда нужно переоткрывать файл.

input = open("ghost1.py")
file = input.read()                         # чтение файла в единственную строку
file                                        # возвращает содержимое файла строкой
input = open("ghost1.py")                   # (!) без этой строчки команда  x = input.read(11) вернёт ''
x = input.read(11)                          # чтение 11 символов 9или 11 байтов) в строку
x                                           # возвращает "Ghost = 'Gh"

input = open("ghost1.py")
file = input.read(11)                       # чтение 11 символов 9или 11 байтов) в строку
file                                        # возвращает "Ghost = 'Gh"

anime = open("ghost1.py")
file = anime.read()                         # чтение файла в единственную строку
file                                        # возвращает весь файл в одну строку с символами экранирования

anime = open("ghost1.py")
file = anime.read(11)                       # Чтение следующих N символов (или байтов) в строку
file                                        # "Ghost = 'Gh"

anime = open("ghost1.py")
file = anime.readline()                     # Чтение следующей текстовой строки(включая символ конца строки) в строку
file                                        # "Ghost = 'Ghost'\n"

anime = open("ghost1.py")
file1 = anime.readline() 
file2 = anime.readline()
file1                                       # "Ghost = 'Ghost'\n"
file2                                       # "Shell = 'Shell'\n"

anime = open("ghost1.py")
file1 = anime.readlines()                   # Чтение файла целиком в список строк (включая символ конца строки)
file1                                       # возвращает файл в строку с экранирование в []
type(file1)                                 # <class 'list'>
anime.close()                               # закрытие файла вручную


anime = open("ghost1.py", "a")
anime.write("Major")                       # записывает упоминание о Майоре, которая гуляет по чужим файлам
anime.close()

"""АХТУНГ - если писать что либо из вне в файл и использовать "w" то всё содержимое файла будет удалено"""
 
anime = open("ghost1.py", "w")             # режим записи "w" - опасная штука, не пользуйся им 
anime.write("Major")                       # тупо перезаписывает все строки файла на Майора в 1ой позиции
anime.close()

# работа с двоичным данными из файла   (у нас с Лутцем разные файлы и разные версии языка)

data = open("data.bin", "rb").read()      # rb - режим чтения двоичных данных
data                                      # возвращает b'Hello\r\nGhost in the shell'
data[4:8]                                 # b'o\r\nG'

x,y,z = 11,501,404                        # числа - преобразовать в строки для записи в файл 
S = "anime"                               # строка - трогать не надо и так пойдёт
D = {"a":1,"b":2}                         # словарь - преобразовать в строку
L = [1,2,3]                               # список - преобразовать в строку
L
F = open("datafile.txt","w")              # открываем (и создаём) новый текстовый файл
F.write(S + "\n")                         # записываем туда строку и ставим символ конца строки - \n
F.write("%s,%s,%s\n" % (x,y,z))           # преобразуем числа в строки с помощью форматирования и пишем
F.write(str(L) + "$" + str(D) + "\n")     # преобразуем словарь и список в строки и разделяем символом $
F.close                                   # закрываем

print(open("datafile.txt").read())        # проверяем что получилось.

data = open("datafile.txt").read()        # побайтовое представление с символами экранирования (\n)
data

Heresy = open("datafile.txt")
line1 = Heresy.readline()                  # присвоить ссылку результату команды "прочитать одну строку" 
line1                                      # возвращает -  'anime\n'
line1.rstrip()                             # удалить символ конца строки - возвращает  'anime'
line2 = Heresy.readline()
line2                                      # возвращает  - '11,501,404\n'
parts = line2.split(",")                   # даём команды - разбить на подстроки с запятыми
parts                                      # возвращает "список строк" ['11', '501', '404\n']
int(parts[1])                              # преобразовать строку в целое число по индексу элемента  - 501
numbers = [int(i) for i in parts]          # используем простой цикл для каждой части объекта - объект int
numbers                                    # возвращает [11, 501, 404]
line3 = Heresy.readline()
line3                                      # возвращает "[1, 2, 3]${'b': 2, 'a': 1}\n"
parts = line3.split("$")                   # разбить на подстроки по символу "$"
parts                                      # возвращает ['[1, 2, 3]', "{'b': 2, 'a': 1}\n"]
eval(parts[0])                             # eval - интерпретирует строку как код, возвращает - [1, 2, 3]
objects = [eval(i) for i in parts]
objects                                    # [[1, 2, 3], {'a': 1, 'b': 2}]
part1 = objects[0]
part1                                      # [1, 2, 3]
part2 = objects[1]
part2                                      # {'b': 2, 'a': 1}

Anime = {"Major":11, "Ghost":501, "Complex": "Alone"}
Anime                                                   # {'Ghost': 501, 'Major': 11, 'Complex': 'Alone'}
File = open("superfile.pkl", "wb")                      # создаём новый файл с непонятным расширением
import pickle                                           # загружаем супер модуль
pickle.dump(Anime,File)                                 # даём команду - свалить объекты Anime в файл File 
File.close()

print(open("superfile.pkl").read())                     # возвращает резкие возмущения варпа и ереси в нём
 
Heresy = open("superfile.pkl", "rb")
import pickle                                           # не забудь загрузить модуль про повторном чтении
Read = pickle.load(Heresy)
Read                                                    # {'Complex': 'Alone', 'Major': 11, 'Ghost': 501}

open("superfile.pkl", "rb").read()

import pickle  
help()                                                  # смотри если что

binary = open("bindata.bin", "wb")                      # открываем файл в режиме записи в байтах
import struct                                           # загружаем полезный модуль типа pickle для bin
data = struct.pack(b">i4sh", 7, b"Spam", 8)             # запаковать данные в () методом модуля struck 
data                                                    # b'\x00\x00\x00\x07Spam\x00\x08'  
binary.write(data)                                      # записать данные в формате bin в файл
binary.close()                                          # закрыть файл
                                
binary = open("bindata.bin", "wb")                        # открываем файл в режиме записи в байтах
import struct                                             # загружаем полезный модуль типа pickle для bin
data = struct.pack(b">i18sh", 7, b"Ghost in the shell", 8)# запаковать строку из18 символов через спецификатор 18s 
data                                                      # b'\x00\x00\x00\x07Spam\x00\x08'  
binary.write(data)                                        # записать данные в формате bin в файл
binary.close()  

binary = open("bindata.bin", "rb")
data = binary.read()
data                                                    # b'\x00\x00\x00\x07Ghost in the shell\x00\x08'
import struct
values = struct.unpack(">i18sh", data)
values                                                  # (7, b'Ghost in the shell', 8)
values[1]
print(values[1])

# ниже более дружественный вариант записи форматирования через спецификаторы

binary = open("bindata2.bin", "wb")                        
import struct      
values = (1, b"Ghost in the shell", 8)
s = struct.Struct('>i 18s h')
packed_data = s.pack(*values)
packed_data
binary.write(packed_data)
binary.close()
   
binary = open("bindata2.bin", "rb")
data = binary.read()
data                                                    
import struct
values = struct.unpack(">i 18s h", data)
values
type(values[1])                                                  
print(values[1])
values[1].decode("utf-8")                 # декодирование b'Ghost in the shell' в 'Ghost in the shell'

binary = open("bindata2.bin", "rb")
try:
    for line in binary:
        print(line)
finally:
    binary.close()                       # возвращает b'\x00\x00\x00\x01Ghost in the shell\x00\x08'


Heresy = open("datafile.txt")
try:
    for line in Heresy:
        print(line)
finally:
    Heresy.close()                       # возвращает всё содержимое файла


Heresy = open("datafile.txt")
try:
    Heresy.readline()                    # возвращает  'anime\n'
finally:
    Heresy.close()

class MyHeresy:
    def __init__(self, date):
        self.date = date
    def __getitem__(self, index):        # Вызывается при выполнении операции self[index]
        self.index = self[index]
    def __add__(self, other):            # # Вызывается при выполнении операции self + other
        self.other = self + other 
FirstGame = MyHeresy("01.01.2017")
SecondGame = MyHeresy(FirstGame)
FirstGame.date

x = [1,2,3]
y = ["a", x, "b"]                        # ['a', [1, 2, 3], 'b']
z = {"x":x, "y":2}                       # {'y': 2, 'x': [1, 2, 3]}
x[1] = "im stupid and my class isnt work at all"
y                                        # ['a', [1, 'im stupid and my class isnt work at all', 3], 'b']
z                                        # {'x': [1, 'im stupid and my class isnt work at all', 3], 'y': 2}

anime = [1,2,3]
heresy = {"Horus":1, "Impi":0}
a = anime[:]
b = heresy.copy()
a[1] = "complex"
b["chaos"] = "quest"
anime, heresy                            #  ([1, 2, 3], {'Horus': 1, 'Impi': 0})
a, b                                     #  ([1, 'complex', 3], {'Horus': 1, 'chaos': 'quest', 'Impi': 0})
 

x = [1,2,3]
y = ["a", x[:], "b"]                     # операция извлечения среза создаёт копию ссылки на объект
z = {"x":x[:], "y":2}                    # благодаря чему ссылки y и z ссылаються на копии отличные от х
x[1] = "im stupid and my class isnt work at all"
y                                        # ['a', [1, 2, 3], 'b']
z                                        # {'y': 2, 'x': [1, 2, 3]}

import copy
y = [1,2,3]
x = copy.deepcopy(y)                    # полная копия объекта со снолько угодно большой вложенностью
y
x
id(y)                                   # 20838152
id(x)                                   # 52587208

Heresy1 = [1,2,3,4]
Heresy2 = [1,2,3,4]
Heresy1 == Heresy2, Heresy1 is Heresy2  # равны - (True), один и тот же объект ? - (False)

Heresy1 = "HorusHeresy"
Heresy2 = "HorusHeresy"
Heresy1 == Heresy2, Heresy1 is Heresy2  # (True, True)

Heresy1 = "Horus is Heresy"
Heresy2 = "Horus is Heresy"
Heresy1 == Heresy2, Heresy1 is Heresy2  # (True, False)


Heresy1 = [1,2,3,(4,1)]
Heresy2 = [1,2,3,(4,2)]
Heresy1 < Heresy2, Heresy1 == Heresy2, Heresy1 > Heresy2      #   (True, False, False)

Heresy = {"Horus":1,"Impi":0}           # 5 интеракций дадут одинаковый результат в порядке объекто сортед
Anime = {"Ghost":11, "Shell":501}
Anime == Heresy                         # False
list(Heresy.items())                    # [('Horus', 1), ('Impi', 0)]
sorted(Heresy.items())                  # [('Horus', 1), ('Impi', 0)]
list(Anime.items())                     # [('Shell', 501), ('Ghost', 11)]
sorted(Anime.items())                   # [('Ghost', 11), ('Shell', 501)]
sorted(Heresy.items()) > sorted(Anime.items())                # True
sorted(Heresy.items()) < sorted(Anime.items())                # False

bool(1)                                 # True
bool([])                                # False
bool({})                                # False
bool(())                                # False
bool("Heresy")                          # True

Heresy1 = 1
Heresy2 = 2
bool(Heresy1 < Heresy2), bool(Heresy1 == Heresy2), bool(Heresy1 > Heresy2)

type(1) == type(int)                   # False (скорее всего потому что сравниваем непустое с пустым)

type([1]) == type([])                  # True
type([1]) == list                      # True
isinstance([1], list)                  # True - Список или объект класса, производного от list

import types                           # В модуле types определены имена других типов
def F(): pass
type(F) == types.FunctionType          # True

import types                           # В модуле types определены имена других типов
def F(): pass
type(11) == types.FunctionType         # False

Heresy = ["Horus Heresy"]
Heresy.append(Heresy)                 # Создает циклический объект: [...]
Heresy                                # ['Horus Heresy', [...]]

Heresy = "Horus Heresy"; Heresy       # 'Horus Heresy'

a = 1; b = 2; c = 3; a,b,c            # кортеж   (1, 2, 3)








