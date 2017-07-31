anime = "{0}, {1} and {2}"
anime.format ("stand", "alone", "complex")     #  'stand, alone and complex'

anime = "{0}, {2} and {1}"
anime.format ("stand", "alone", "complex")     #  'stand, complex and alone'

anime = "{0}, {1} Ghost in the shell {2}"
anime.format ("stand", "alone", "complex")     #   'stand, alone Ghost in the shell complex'

anime = "{stand}, {alone} and {complex}"
anime.format (stand = "ghost", alone = "in the", complex = "shell")  # 'ghost, in the and shell'

anime = "{stand}, {alone} and {complex}, {1}, {0}"
anime.format ("anime", "story", stand = "ghost", alone = "in the", complex = "shell")

# возвращает - 'ghost, in the and shell, story, anime' 

anime = "{stand}, {0}, {alone}, {complex}"
anime.format ("Ghost", stand = "in", alone = "the", complex = "shell")   # 'in, Ghost, the, shell'

anime = "{stand}, {1}, {alone}, {complex}, {0}"
anime.format ("Ghost", "Major", stand = "in", alone = "the", complex = "shell")   

# возвращает 'in, Major, the, shell, Ghost' ; Ghost == 0, Major == 1

"{stand}, {1}, {alone}, {complex}, {0}".format ("anime", "story", stand = 501, alone = [1,2], complex = {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"})
 
# возвращает "501, story, [1, 2], {'11': 'Crazy Major Friends', 'Godo': 'Evil Enemy', 'Ghost': 'Major', 'Bato': 'Major Friend'}, anime"


Major = "{stand}, {1}, {alone}, {complex}, {0}".format ("anime", "story", stand = 501, alone = [1,2], complex = {"Ghost":"Major"})
Major                                         # 501, story, [1, 2], {'Ghost': 'Major'}, anime"
Major.split("[1, 2]")                         # ['501, story, ', ", {'Ghost': 'Major'}, anime"]
anime = Major.replace(",", "Stand alone complex")     # заменил все запятые, оказывается так можно
anime

# возвращает "501Stand alone complex storyStand alone complex [1Stand alone complex 2]Stand alone complex {'Ghost': 'Major'}Stand alone complex anime"                                              

Major = "{stand}, {1}, {alone}, {complex}, {0}".format ("anime", "story", stand = 501, alone = [1,2], complex = {"Ghost":"Major"})
Major                                         # 501, story, [1, 2], {'Ghost': 'Major'}, anime"
Major.split("[1, 2]")                         # ['501, story, ', ", {'Ghost': 'Major'}, anime"]
anime = Major.replace("501", "Stand alone complex")     
anime                                         # "Stand alone complex, story, [1, 2], {'Ghost': 'Major'}, anime"

import sys
"My {1[spam]} runs {0.platform}".format(sys, {"spam": "laptop"})
"My {config[spam]} runs {sys.platform}".format(sys=sys, config = {"spam": "laptop"})

animelist = list("Ghost in the shell")        # создаём список
animelist  # ['G', 'h', 'o', 's', 't', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ', 's', 'h', 'e', 'l', 'l']
"first = {0[0]}, second = {0[1]}".format(animelist)         # 'first = G, second = h'
"first={0}, last={1}".format(animelist[0], animelist[-1])   #  'first=G, last=l'
parts = animelist[0], animelist[-1], animelist[1:3]
"first={0}, last={1}, middle={2}".format(*parts)            #  "first=G, last=l, middle=['h', 'o']"
 
anime = list("Stand alone complex")
story = "anime1 = {0[0]}, anime2= {0[1]}, anime3 = {0[2]}".format(anime)  
story                                         # возвращает 'anime1 = S, anime2= t, anime3 = a'

anime = list("Stand alone complex")
ghost = "anime1 = {0}, anime-1 = {1}".format(anime[0], anime[-1])
ghost                                         # возващает 'anime1 = S, anime-1 = x'

anime = list("Stand alone complex")           # создаём список lля использования индексов
Major = anime[0], anime[-1], anime[0:5]       # по индексам списка присваиваем значение переменной
Bato = "anime1 = {0}, anime2 = {1}, anime3 = {2}".format(*Major)    # форматируем через переменную
Bato                                          # "anime1 = S, anime2 = x, anime3 = ['S', 't', 'a', 'n', 'd']"

"{0:10} = {1:10}".format("Ghost", 123.456)   # возвращает 'Ghost      =    123.456'
 
"{0:<10} = {1:<10}".format("Ghost", 123.456) # возвращает 'Ghost      = 123.456   '

import sys
"{0.platform:>10} = {1[item]:<10}".format(sys, dict(item="laptop"))   #  возвр. '     win32 = laptop    '

"{0:10} = {1:10}".format("Ghost", 123.456)   # 'Ghost      =    123.456'
"{0:5} = {1:10}".format("Ghost", 123.456)    # 'Ghost =    123.456'
"{0:5} = {1:5}".format("Ghost", 123.456)     # 'Ghost = 123.456'
"{0:3} = {1:5}".format("Ghost", 123.456)     # 'Ghost = 123.456'

"{0:10} = {2:10}".format("Ghost", 123.456, 501.11)   # 'Ghost      =     501.11'
"{0:10} = {0:10}".format("Ghost", 123.456, 501.11)   # 'Ghost      = Ghost     
"{2:1} = {0:3}".format("Ghost", 123.456, 501.11)     # '501.11 = Ghost'

"{0:<10} = {1:<10}".format("Ghost", 123.456)       #  выравнивание по левому краю
"{0:>10} = {1:>10}".format("Ghost", 123.456)       #  выравнивание по правому краю
"{0:<10} = {1:>10}".format("Ghost", 123.456)       #  выравнивание по левому и правому краю
"{0:^10} = {1:^10}".format("Ghost", 123.456)       #  выравнивание по центру (центр по ширине вывода - 10)

import module1
"{0.a:>10} = {1:<10}".format(module1, "Shell")     #  возвращает - '     Ghost = Shell     '

import module1
"{0.a[1]!r:>10} = {1:<10}".format(module1, "Shell")   # "       'h' = Shell     "
"{0.b[4]!s:>10} = {1:<10}".format(module1, "Shell")   # '         l = Shell     '
"{0.c[4]!a:>10} = {1:<10}".format(module1, "Shell")   # "       'e' = Shell     "


"{0:e}, {1:.3e}, {2:g}".format(3.14159, 3.14159, 3.14159)        #'3.141590e+00, 3.142e+00, 3.14159'

"{0:f}, {1:.2f}, {2:06.2f}".format(3.14159, 3.14159, 3.14159)    # '3.141590, 3.14, 003.14'

"{0:X}, {1:o}, {2:b}".format(255, 255, 255)   # Шестнадцатеричное, восьмеричное и двоичное представление

bin(255), int("11111111", 2), 0b11111111      # проверяем, возвращает ('0b11111111', 255, 255)

"{0:.2f}".format(1 / 3.0)                     # '0.33'
"{00:.2f}".format(1 / 7.0)                    # '0.14'
"{000:.3f}".format(1 / 7.0)                   # '0.143'
"{000:.11f}".format(1 / 7.0)                  # '0.14285714286'

"%.2f" % (1 / 3.0)                            # '0.33'
"%.11f" % (1 / 3.0)                           # '0.33333333333'

"{0:.{1}f}".format(1 / 3.0, 4)                # '0.3333'
"%.*f" % (4, 1 / 3.0)                         # '0.3333'

"{1:.{1}f}".format(1 / 3.0, 4)                #  '4.0000' ( потому что 4 - это второй аргумент в скобках )

# как бы *f удобнее чем .{1}f - вообще я тут немного не понимаю что имеет ввиду Лутц. 
# .f - понятно, .{1}f непонятно. - зачем {1}? а вспомнил - это также фигня что и с:

x = 1
y = 2
"%f, %.10f" % (x, y)                        # %.xf - где х число знаков после запятой
"%f, %.10f, %.*f" % (x, y, 20, 11)          # без 11 - не работает, тоже и с .{1}f

# т.е по аналогии с оператором форматирования метод форматирования тоже хочет аргумент в качестве базы.
# ведь "{1:.{1}f}".format(1 / 3.0, 4)  в части .{1}f - указывает на 4 - т.е на второй аргумент в скобках

"{0:.{2}f}".format(1 / 3.0, 4, 10, 11)                # '0.3333333333'

"{0:.2f}".format(1.2345)           # Строковый метод
format(1.2345, ".2f")              # Встроенная функция
"%.2f" % 1.2345                    # Выражение форматирования

import anime
dir(anime)
a = "{0.NextGame.hostGoals:1} = {1:1}".format(anime, "Shell")
b = "{0.FirstGame.questteammembers!s:1} = {1:1}".format(anime, "Shell")
a                                  # '0 = Shell'
b                                  # 'Random Evil characters = Shell'

# наверное я чего то не понимаю, но, через форматирование выводит данные, а просто так нет.

# спустя 2 часа и https://wombat.org.ua/AByteOfPython/modules.html + http://younglinux.info/oopython/module.php

# надо завязывать учиться по ночам, но!!! оно работает , ещё бы старший брат не портил мне дома настроение

import anime
anime.FirstGame.date                                # '01.01.2017'
anime.FirstGame.hostTeam                            # 'AnimeTeam'
anime.FirstGame.guestTeam                           # 'EvilTeam'
anime.FirstGame.hostGoals                           # '100500'
anime.FirstGame.guestgoals                          # '0'
anime.FirstGame.hostteammembers                     # 'Ghost in the shell characters'
anime.FirstGame.questteammembers                    # 'Random Evil characters'
anime.NextGame.hostGoals                            # '0'
a = anime.FirstGame.date
b = anime.FirstGame.questteammembers
print(a, b)                                         #  01.01.2017 Random Evil characters

print("%s=%s" % ("spam", 42))                       # spam=42
print("%s=%s" % ("Ghost in the shell", 501))        # Ghost in the shell=501
print("{0} = {1}".format("Ghost in the shell", 501))# Ghost in the shell = 501 

anime = "%s, %s, %s"                             # %s - (s) тип объектов, строки.
anime % ("Stand", "Alone", "Complex")            # в скобках позиционные параметры
print(anime)                                     # %s, %s, %s
 
anime = "Major %s, Major %s, Major %s"           # %s - (s) тип объектов, строки.
anime % ("Stand", "Alone", "Complex")            # в скобках позиционные параметры
print(anime)                                     # Major %s, Major %s, Major %s

anime = "Major %s, Major %s, Major %s" % ("Stand", "Alone", "Complex") 
anime                                            # 'Major Stand, Major Alone, Major Complex'

anime = "%(Major)s, %(Ghost)s and %(State)s" % dict(Major="Stand", Ghost="Alone", State="Complex")
anime                                            # 'Stand, Alone and Complex'
          
template = "%(motto)s, %(pork)s and %(food)s"
template % dict(motto="spam", pork="ham", food="eggs")   # Ключи словаря 'spam, ham and eggs'

"%s, %s and %s" % (3.14, 42, [1, 2])             # '3.14, 42 and [1, 2]'

somelist = list("SPAM")
parts = somelist[0], somelist[-1], somelist[1:3]
"first=%s, last=%s, middle=%s" % parts           #  "first=S, last=M, middle=['P', 'A']"

"%-10s = %10s" % ("spam", 123.4567)              #  'spam       =   123.4567'
"%10s = %-10s" % ("spam", 123.4567)              #  '      spam = 123.4567  '

import sys
"%(plat)10s = %(item)-10s" % dict(plat=sys.platform, item="laptop")      #  '     win32 = laptop    '

"%e, %.3e, %g" % (3.14159, 3.14159, 3.14159)     # '3.141590e+00, 3.142e+00, 3.14159'
"%f, %.2f, %06.2f" % (3.14159, 3.14159, 3.14159) # '3.141590, 3.14, 003.14'

"%x, %o" % (255, 255)                            # 'ff, 377'

import sys
"My {1[spam]:<8} runs {0.platform:>8}".format(sys, {"spam": "laptop"})  # 'My laptop   runs    win32'
"My %(spam)-8s runs %(plat)8s" % dict(spam="laptop", plat=sys.platform) # 'My laptop   runs    win32'

"{0:d}".format(999999999999)                    #  '999999999999'
"{0:,d}".format(999999999999)                   #  '999,999,999,999'
"{:,d} {:,d}".format(9999999, 8888888)          #  '9,999,999 8,888,888'
"{:,.2f}".format(296999.2567)                   #  '296,999.26'
"{0:b}".format((2 ** 16) -1)                    #  '1111111111111111'

"{0:f}, {1:.2f}, {2:05.2f}".format(3.14159, 3.14159, 3.14159)   #  '3.141590, 3.14, 03.14'
"{:f}, {:.2f}, {:06.2f}".format(3.14159, 3.14159, 3.14159)      #  '3.141590, 3.14, 003.14'
"%f, %.2f, %06.2f" % (3.14159, 3.14159, 3.14159)                #  '3.141590, 3.14, 003.14'

# Вообще Лутц большой путанник - ему сразу нужно было рассазывать про метод .format - без выражения %

"%.2f" % 1.2345                                #  '1.23' (потому что ширина полосы вывода = 2)
"%.2f %s" % (1.2345, 99)                       #  '1.23 99' 

"%s" % 1.23                                    #   '1.23'
"%s" % (1.23,)                                 #   '1.23'
"%s" % ((1.23,),)                              #   '(1.23,)'

"{0:.2f}".format(1.2345)                       #   '1.23'
"{0:.2f} {1}".format(1.2345, 99)               #   '1.23 99'

"{0}".format(1.23)                             #   '1.23'
"{0}".format((1.23,))                          #   '(1.23,)'

help(list)                                     # методы доступные для списков
help(str)                                      # методы доступные для строк
help(int)                                      # методы доступные для чисел



Heresy = list("God Emperor Was Banned By The Horus Banhammer")      # команда на создание списка из строки
Heresy = []                                    # Пустой список
Heresy = [0, 1, 2, 3]                          # Четыре элемента с индексами 0..3
Heresy = [404, 501, ["Horus", "Banhammer"]]    # Вложенные списки

Heresy = list(range(-4, 4))    # создание спикска из последовательно чисел 
Heresy                         # возвращает [-4, -3, -2, -1, 0, 1, 2, 3]

Heresy = list("God Emperor Was Banned By The Horus Banhammer") 
Heresy[1]                      # индекса, возвращает ['o'] 
Heresy[1:7]                    # построение среза, возвращает ['o', 'd', ' ', 'E', 'm', 'p']
len(Heresy)                    # длинна, возвращает 45

Heresy = list("God Emperor Was Banned By The Horus Banhammer") 
Heresy[1][1]                   # в теории list[i][j] - i индекса, j - индекс индекса,
Heresy[1][0]                   # на практике пашет только через 0, видимо это индекс строки. 
Heresy[8][0]                   # возвращает 'r'


Heresy = list("God Emperor Was Banned By The Horus Banhammer") 
Heresy + Heresy                # коннетация
Heresy * 2                     # дублирование

Heresy = list("God Emperor Was Banned By The Horus Banhammer") 
for x in Heresy: print(x)      # обход в цикле
"G" in Heresy                  # проверка на вхождение, возвращает true
"God" in Heresy                # возвращает false

Heresy = list("God Emperor Was Banned By The Horus Banhammer") 
Heresy.append(4)               # метод добавления элементов в список
Heresy.extend([5,6,7])         # ещё один метод добавления элментов
X = 11
Heresy.insert(X, 2)            # вставить элемент 2 в список после элемента номер Х в списке.
Heresy.index(2)                # найти элемент 2 по номеру индекса в списке

""" count() метод подсчёта одинаковых элементов в спике"""

Heresy = [404, 501, 11]
Heresy.count(404)              # возвращает 1
Heresy.count(505)              # возвращает 0

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy.count("o")              # возвращает 3

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy.sort()                  # красиво сортирует элементы внутри списка
Heresy.reverse()               # изменяет порядок следования элементов на обратный

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
del Heresy[1]                  # удалить второй элемент списка
del Heresy[1:11]               # удалить срез со второго по 11 элементы внутри списка

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy.pop()                   # неведомая хуйня, 100% проистекает от импи и его упоротых лоялистов
Heresy.remove(2)               # тоже самое

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy[0:3] = []               # ещё один метод сократить список ереси
Heresy

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy[0] = "S"                # присваивание значений элементов по индексу
Heresy

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy[0:3] = [0,1,2,3]        # присваивание значений элементов по срезу
Heresy

Heresy = list("God Emperor Was Banned By The Horus Banhammer")
Heresy = [x**2 for x in range(5)]                # генератор списков (супер полезная вещь)
Heresy

list(map(ord, "god"))                            # методы отображений - ещё более полезная вещь.

3 in [1,2,3,4]                # True

for x in [1,2,3,4]:
    print(x +1)               # 2 3 4 5

Heresy = [x*2 for x in "Horus Heresy"]        # генератор списков
Heresy

Heresy = []
for x in "Horus Heresy":      # альтернатива генератора списков через for
    Heresy.append(x * 2)
Heresy                        # ['HH', 'oo', 'rr', 'uu', 'ss', '  ', 'HH', 'ee', 'rr', 'ee', 'ss', 'yy']

res = []
for c in "SPAM":                             
    res.append(c * 4)                        
res                           # ['SSSS', 'PPPP', 'AAAA', 'MMMM']

Heresy = list(map(abs, [1,2,3,4,5]))
Heresy                        #   [1, 2, 3, 4, 5]

Heresy = ["Horus", "Heresy", "Heretic"]
Heresy[0]                     #  'Horus'
Heresy[1]                     #   'Heresy'
Heresy[2]                     #    'Heretic'
Heresy[-2]                    #      'Heresy'
Heresy[:2]                    #       ['Horus', 'Heresy']

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]           # двухмерный массив
matrix[1]                                            # [4, 5, 6]
matrix[1][1]                                         # 5
matrix[2][0]
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix[1][1]                                         # 5

Heresy = ["Horus", "Heresy", "Heretic"]
Heresy[0] = "Chaos"                                  # присваивание по индексу элемента
Heresy                                               # ['Chaos', 'Heresy', 'Heretic']

Heresy = ["Horus", "Heresy", "Heretic"]
Heresy[0:2] = ["Chaos", "Exterminatus"]              # присваивание по срезу (удаление+вставка)
Heresy                                               # ['Chaos', 'Exterminatus', 'Heretic']

Heresy = ["Horus", "Heresy", "Heretic"]
Heresy.append("Chaos")                               # Вызов метода добавления элемента в конец списка
Heresy                                               # ['Horus', 'Heresy', 'Heretic', 'Chaos']
Heresy.sort()                                        # Сортировка элементов списка (‘S’ < ‘e’)
Heresy                                               # ['Chaos', 'Heresy', 'Heretic', 'Horus']

Heresy = ["abc", "ABD", "aBe"]
Heresy.sort()                                        # сортировка с учётом регистра символов
Heresy                                               # ['ABD', 'aBe', 'abc']
Heresy.sort(key=str.lower)                           # привидение символов к нижнему регистру
Heresy                                               # ['abc', 'ABD', 'aBe']
Heresy.sort(key=str.lower, reverse=True)             # изменение направления сортировки
Heresy                                               # ['aBe', 'ABD', 'abc']

Heresy = ["abc", "ABD", "aBe"]
sorted(Heresy, key=str.lower, reverse=True)          #  ['aBe', 'ABD', 'abc']
 
Heresy = ["abc", "ABD", "aBe"]
sorted([x.lower() for x in Heresy], reverse=True)    #  ['abe', 'abd', 'abc']


Heresy = list("God Emperor Was Banned By The Horus Banhammer")
sorted([x.lower() for x in Heresy], reverse=True)

# возвращает
# ['y', 'w', 'u', 't', 's', 's', 'r', 'r', 'r', 'r', 'p', 'o', 'o', 'o', 'n', 'n', 'n', 'm', 'm', 'm', 'h', 'h', 'h', 'g', 'e', 'e', 'e', 'e', 'e', 'd', 'd', 'b', 'b', 'b', 'a', 'a', 'a', 'a', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

Heresy = list("Banned By The Horus")
sorted([x+str(1) for x in Heresy], reverse=True) 

# ['y1', 'u1', 's1', 'r1', 'o1', 'n1', 'n1', 'h1', 'e1', 'e1', 'd1', 'a1', 'T1', 'H1', 'B1', 'B1', ' 1', ' 1', ' 1']


Heresy = list("Banned By The Horus")
Heresy.pop()                                  # удаляет и возвращает последний элемент списка - 's'
Heresy.reverse()                              # изменяет порядок следования элементов на обратный
Heresy                                        
list(reversed(Heresy))                        # встроенная функция сортировки в обратном порядке

"""(Last-In-First-Out, LIFO)"""

Heresy= []
Heresy.append(1)                              # втолкнуть на стек
Heresy.append(2)
Heresy
Heresy.pop()                                  # вытолкнуть со стека
Heresy

Heresy = ["Horus", "Heresy", "Heretic"]
Heresy.index("Horus")                         # возвращает индекс объекта в списке - 0
Heresy.insert(2, "Chaos")                     # вставка в требуемую позицию
Heresy                                        # ['Horus', 'Heresy', 'Chaos', 'Heretic']
Heresy.pop(0)                                 # удаление элемента по индексу
Heresy                                        # ['Heresy', 'Chaos', 'Heretic']

Heresy = list("God Emperor vs Horus Banhammer")
del Heresy[0]                                 # удаление одного элемента списка
Heresy             
del Heresy[:4]                                # удаление среза
Heresy                                        

Heresy = list("God Emperor vs Horus Banhammer")
Heresy[1:] = []
Heresy                                        # ['G']
Heresy[0:] = []                               # удаление списка с сохранение на него ссылки в сис.таблице 
Heresy                                        # []

Heresy = {}                                         # пустой словарь
Heresy = {"Horus":1, "Emperor":2}                   # словарь из двух элементов
Heresy = {"Horus Heresy":{"Horus":1, "Emperor":2}}  # вложение
Heresy["Horus Heresy"]                              # {'Emperor': 2, 'Horus': 1}

Heresy = dict(name="Horus", status="Heretic")       # альтернативный способ создания словарей
Heresy                                              # {'name': 'Horus', 'status': 'Heretic'}

# именованные аргументы, применение функции zip и списки ключей

Heresy = dict(zip(keyslist, valslist))              # что то непонятное (!)
Heresy = dict.fromkeys(["a", "b"])                  # {'b': None, 'a': None}

Heresy = {"Horus Heresy":{"Horus":1, "Emperor":2}}  
Heresy["Horus Heresy"]                              # доступ к элементу по ключу ["Horus Heresy"]  
Heresy["Horus Heresy"]["Horus"]                     # возвращает - 1
"Emperor" in Heresy                                 # проверка на вхождение, возвращает False
"Horus Heresy" in Heresy                            # True
Heresy.keys()                                # список ключей, возв - dict_keys(['Horus Heresy'])
Heresy.values()                              # список значений dict_values([{'Emperor': 2, 'Horus': 1}])
Heresy.items()                               # dict_items([('Horus Heresy', {'Emperor': 2, 'Horus': 1})])
Heresy.copy()                                # копировани, {'Horus Heresy': {'Emperor': 2, 'Horus': 1}}
Heresy.get(key, default)                     # получение значений по умолчанию, возвр 'key' is not defined
 
Heresy = {"Horus Heresy":{"Horus":1, "Emperor":2}}   
dic = {'anime':'аниме',"ghost":"призрак","shell":"образ"}
Heresy.update(dic)                           # слияние
Heresy                                       # {'shell': 'образ', 'anime': 'аниме', 'Horus Heresy': {'Horus': 1, 'Emperor': 2}, 'ghost': 'призрак'}
Heresy.pop("anime")                          # удаление ключа
Heresy                                       # {'shell': 'образ', 'ghost': 'призрак', 'Horus Heresy': {'Emperor': 2, 'Horus': 1}}
len(Heresy)                                  # длинна - возвращает 3
Heresy["ghost"] = 11                         # добавление, изменение ключей
Heresy                                       # {'Horus Heresy': {'Emperor': 2, 'Horus': 1}, 'ghost': 11, 'shell': 'образ'}
del Heresy["ghost"]                          # удаление ключа
Heresy                                       # {'shell': 'образ', 'Horus Heresy': {'Horus': 1, 'Emperor': 2}}
list(Heresy.keys())                          # представление словарей, возвр - ['Horus Heresy', 'shell']
Heresy.keys()                                # dict_keys(['shell', 'Horus Heresy'])
Heresy = {x: x*2 for x in range(10)}         # генератор словарей (напишет новый словарь вместо старого)
Heresy                                       # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

dic = {'anime':'аниме',"ghost":"призрак","shell":"образ"}
list(dic.keys())                             # ['shell', 'anime', 'ghost']
"anime" in dic                               # True

dic = {"Horus": 2, "Impi": 1, "Kaos": 3}
dic["Horus"]                                 # 2
"Horus" in dic                               # True
dic["Kaos"] = ["Warp", "Chaos", "Evil"]
dic                                          # {'Horus': 2, 'Impi': 1, 'Kaos': ['Warp', 'Chaos', 'Evil']}
del dic["Impi"]
dic                                          # {'Horus': 2, 'Kaos': ['Warp', 'Chaos', 'Evil']}
dic["Impi"] = "Banned Impi"
dic                                          # {'Horus': 2, 'Impi': 'Banned Impi', 'Kaos': ['Warp', 'Chaos', 'Evil']}

dic = {"Horus": 2, "Impi": 1, "Kaos": 3}
list(dic.values())                           #  [2, 1, 3]
list(dic.items())                            #  [('Impi', 1), ('Kaos', 3), ('Horus', 2)]
dic.get("Horus")                             #  2
print(dic.get("anime"))                      #  ключ отсуствует в словаре - возвращает None
dic.get("anime", 501)                        #  501

""" метод .pop() может принимать аргумент в скбоках - что бы удалять элемент списка по позиции"""

Heresy = ["aa", "bb", "cc", "dd"]   
Heresy.pop()                                 # 'dd'
Heresy                                       # ['aa', 'bb', 'cc']
Heresy.pop(1)                                # 'bb'
Heresy                                       # ['aa', 'cc']

Heresy = {"Horus Heresy": "Horus",
        "Holy Terra": "Impi",
        "Anime": "Major",
        "Chaos Heresy": "Slaanesh"}
Heresy
story1 = "Horus Heresy"
creator1 = Heresy[story1]
creator1                                     # 'Horus'
story2 = "Holy Terra"
creator2 = Heresy[story2]
creator2                                     # 'Impi'
story3 = "Anime"
creator3 = Heresy[story3]
story4 = "Chaos Heresy"
creator4 = Heresy[story4]
creator3                                     # 'Major'
creator4                                     # 'Slaanesh'
for x in Heresy:
    print(x, "\t", Heresy[x])
for lang in Heresy:
    print(lang, "\t", Heresy[lang])          # \t это горизонтальная табуляция
for x in Heresy:
    print(x, "\t\\", Heresy[x])              # \t\\ табуляция слешом
for x in Heresy:
    print(x, Heresy[x])                      # так вообще красиво, но хочеться испольщовать форматирование

Heresy = {"Horus Heresy": "Horus",
        "Holy Terra": "Impi",
        "Anime": "Major",
        "Chaos Heresy": "Slaanesh"} 
for name, phone in Heresy.items():
    print('{0:10} ==> {1:10}'.format(name, phone))       # здесь нужно вспомнить нужныt слова 

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}     # очень полезный пример форматирования вывода
for name, phone in table.items():                        # смотреть здесь 
    print('{0:10} ==> {1:10d}'.format(name, phone))      # https://docs.python.org/3/tutorial/inputoutput.html

Heresy = {"Horus Heresy": "Horus",
        "Holy Terra": "Impi",
        "Anime": "Major",
        "Chaos Heresy": "Slaanesh"} 
for x, y in Heresy.items():
    print('{0:15} ==> {1:10s}'.format(x, y))             # выравниваем вывод в первых фигурных скобках {:}

Heresy = {"Horus Heresy": "Horus",
        "Holy Terra": "Impi",
        "Anime": "Major",
        "Chaos Heresy": "Slaanesh"}
Heresy
story1 = "Horus Heresy"
creator1 = Heresy[story1]
creator1                                     # 'Horus'
story2 = "Holy Terra"
creator2 = Heresy[story2]
creator2                                     # 'Impi'
story3 = "Anime"
creator3 = Heresy[story3]
story4 = "Chaos Heresy"
creator4 = Heresy[story4]
creator3                                     # 'Major'
creator4
for x, y in Heresy.items():
    print('{0:15} ==> {1:10s}'.format(x, y)) 

# век живи, век учись, вроде уже прошёл .format а сразу и без подсказки не смог вспомнить как это сделать.

Heresy = []
Heresy[99] = "Horus Heresy"                  # вернёт исключение

Heresy = {}                                  
Heresy[99] = "Horus Heresy"                  # в отлиии от списокв для словаря это допусимая операция. 
Heresy[99]
Heresy                                       # {99: 'Horus Heresy'}

Heresy = {}
Heresy[(2,3,4)] = 88
Heresy[(11,404,501)] = 99
x = 2; y = 3; z = 4                         # символ ; - отделяет инстркции (полезная инфа)
Heresy[(x,y,z)]                             # возвращает 88
Heresy                                      # возвращает {(11, 404, 501): 99, (2, 3, 4): 88}
a = 11; b = 404; c = 501
Heresy[(a,b,c)]                             # возвращает 99
Heresy[(x,y,z),(a,b,c)]                     # вернёт исключение - KeyError: (2, 3, 4, 11, 404, 501)

""" Heresy[(x,y,z),(a,b,c)]  возвращает исключение ибо в системной таблице 2 разные ссылки и два объекта"""

Heresy = {}
Heresy[(2,3,4)] = 88
Heresy[(11,404,501)] = 99
x = 2; y = 3; z = 4                         
Heresy[(x,y,z)]                             
Heresy                                      
a = 11; b = 404; c = 501
Heresy[(a,b,c)]                             
if (2,3,6) in Heresy:                           # простой цикл, который проверяет наличие ключя в словаре
    print(Heresy[(2,3,6)])
else:
    print("Horus Heresy is everything for me")
try:                                            # попытаться обратиться по индексу
    print(Heresy[(2,3,6)])
except KeyError:                                # перехватить исключение и обработать (вижу в первый раз)
    print("Horus Heresy is everything for me")  # по результатам ловит исключение и едет дальше по циклу
Heresy.get((2,3,4), 0)                          # существует, извлекаеться и возвращается - вернёт 88
Heresy.get((2,3,6), 0)                          # отсуствует, возвращает default элемент - 0
Heresy.get((2,3,6), 11)                         # отсуствует, возвращает default элемент - 11

rec = {}
rec["name"] = "Horus"
rec["age"] = "501"
rec["job"] = "Heresy"
print(rec["name"])                             # Horus

Heresy = {"name":"Horus",
        "jobs":["Heresy","Heretic"],
        "web":"www.chaos.net/Horus",
        "home":{"state":"Terra","zip":"501404"}}
Heresy["name"]                                # 'Horus'
Heresy["jobs"]                                # ['Heresy', 'Heretic']
Heresy["jobs"][1]                             # 'Heretic'
Heresy["home"]["zip"]                         # '501404'

{"name": "Horus", "age": 501}                 # традиционное литеральное выражение
Heresy = {}                                   # динамическое присваивание по ключам
Herey["name"] = "Horus"
Heresy["age"] = 501

Heresy = dict(name= "Horus", age= 501)              # форма именованных элементов
Heresy

Heresy = dict([("name", "Horus"), ("age", 501)])    # Кортежи ключ/значение

Heresy = dict.fromkeys(["a", "b"], 0)
Heresy                                       # {'b': 0, 'a': 0}
Heresy = dict.fromkeys(["a", "b"], 11)
Heresy                                       # {'b': 11, 'a': 11}
Heresy = dict.fromkeys(["a", "b", 11], "Horus Heresy")
Heresy                                       # {11: 'Horus Heresy', 'b': 'Horus Heresy', 'a': 'Horus Heresy'}

list(zip(["a", "b", "c"], [1, 2, 3]))        # объеденить ключи и значения
list(zip(["Heresy","Horus","Chaos"],["Horus Heresy","Horus Heretic","Chaos Heresy"]))
Heresy = dict(zip(["Heresy","Horus","Chaos"],["Horus Heresy","Horus Heretic","Chaos Heresy"]))
Heresy               #   {'Chaos': 'Chaos Heresy', 'Heresy': 'Horus Heresy', 'Horus': 'Horus Heretic'}

D = {k: v for (k, v) in zip(["a", "b", "c"], [1, 2, 3])}
D                                            # {'b': 2, 'c': 3, 'a': 1}

Heresy = {x: y for (x, y) in zip(["Heresy","Horus","Chaos"],["Horus Heresy","Horus Heretic","Chaos Heresy"])}
Heresy              #    {'Heresy': 'Horus Heresy', 'Horus': 'Horus Heretic', 'Chaos': 'Chaos Heresy'}

D = {x: x ** 2 for x in [1, 2, 3, 4]}
D                                      # {1: 1, 2: 4, 3: 9, 4: 16}

Heresy = {x: x + 1 for x in [1,2,3,4]}
Heresy                                 # {1: 2, 2: 3, 3: 4, 4: 5}

 
Heresy = {x: x + 1 for x in range(1,5)}
Heresy                                 # {1: 2, 2: 3, 3: 4, 4: 5} 

Heresy = {x: x + 1 for x in range(-1,7)}
Heresy                                 # {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, -1: 0} 
 
Heresy = {x: x * 1 for x in "Heresy"}  #  цикл через интеррируемый объект 
Heresy                                 #  {'r': 'r', 's': 's', 'y': 'y', 'H': 'H', 'e': 'e'}

D = {c.lower(): c + "!" for c in ["Heresy", "CHAOS", "horus"]}
D                                      # {'chaos': 'CHAOS!', 'heresy': 'Heresy!', 'horus': 'horus!'}

Heresy = {a: a + " anime" for a in ["Horus Heresy", "Chaos Heresy"]}
Heresy                                 # {'Horus Heresy': 'Horus Heresy anime', 'Chaos Heresy': 'Chaos Heresy anime'}

Heresy = dict.fromkeys(["a", "b", "Chaos"], 0)
Heresy                                 # {'Chaos': 0, 'a': 0, 'b': 0}

Heresy = {x: 0 for x in ["a", "b", "Chaos"]}
Heresy                                 # {'a': 0, 'Chaos': 0, 'b': 0}

Heresy = {x: "Null heresy" for x in ["a", "b", "Chaos"]}
Heresy                                 # {'a': 'Null heresy', 'b': 'Null heresy', 'Chaos': 'Null heresy'}

Heresy = dict.fromkeys("Horus Heresy")
Heresy      # {'y': None, 'o': None, 'H': None, 's': None, 'e': None, 'r': None, 'u': None, ' ': None}

Heresy = {x: None for x in "Horus Heresy"}
Heresy      # {'e': None, 'u': None, 'r': None, 's': None, 'o': None, ' ': None, 'y': None, 'H': None}

Heresy = dict(Horus = 1, Heresy = 404, Chaos = 505)
Heresy                                 #   {'Heresy': 404, 'Chaos': 505, 'Horus': 1}
Anime = Heresy.keys()
Anime                                  #   dict_keys(['Heresy', 'Chaos', 'Horus'])
list(Heresy)                           #   ['Chaos', 'Horus', 'Heresy']
Story = Heresy.values()                #   команда на просмотр значений словаря 
Story                                  #   dict_values([404, 1, 505])
list(Story)                            #   [404, 505, 1]
list(Heresy.items())                   #   [('Horus', 1), ('Chaos', 505), ('Heresy', 404)]
list(Heresy)[0]                        #   'Chaos'

Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
Heresy                                 # возвращает весь словарь
Anime = Heresy.keys()                  # ключи
Anime                                  # возвращает ключ словаря
list(Heresy)                           # создаёт список из сключей словаря
Story = Heresy.values()                # значения ключей
Story                                  # возвращает значения ключей словаря
list(Story)                            # создание списка из значения ключей словаря
list(Heresy.items())                   # создание спика из объектов словаря - ключей и значений
list(Heresy)[0]                        # обращается по индексу к элементам списка, теряет порядок
list(Heresy)[0:2]                      # извлекает срез из элементов списка, теряет порядок
                           
D = dict(a=1, b=2, c=3)
D      
K = D.keys() 
K                                      # По Лутцу в версии 3.0 возвращает интерируемый объект - <dict_keys object at 0x026D83C0>
list(K) 
V = D.values() 
V                                      # По Лутцу в версии 3.0 возвращает интерируемый объект - <dict_values object at 0x026D8260>
list(V)        
list(D.items())
list(K)[0]
for k in D.keys(): print(k)            # Здесь тоже не сохраняет порядок вывода 
for key in D: print(key)               # Здесь тоже не сохраняет порядок вывода 

D = {"a":1, "b":2, "c":3}
D
K = D.keys()
V = D.values()
list(K)                                 # В 3.0 представления сохраняют оригинальный
list(V)
del D["b"]                              # Изменяет словарь непосредственно
D
list(K)                                 # Изменения в словаре отражаются на объектах представлений
list(V)                                 # Но это не так в версии 2.X!


Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
list(Heresy)                            # не сохраняет порядок

# учимся сортировать содержимое словаря, которое на самом деле внутри словаря храиться в случайном порядке

D = {"a":1, "b":2, "c":3}
D                                      # {'b': 2, 'a': 1, 'c': 3}
K = D.keys()
a = list(K)
a.sort()
a                                      # ['a', 'b', 'c']
V = D.values()
b = list(V)
b.sort()
b                                      # [1, 2, 3]
a[1]                                   # 'b'
b[0:2]                                 # [1, 2]

import collections
Heresy = collections.OrderedDict()
Heresy["Horus"] = "Heresy"
Heresy["Chaos"] = "Chaos Heresy"
Heresy["Crusade"] = "Anti Heresy"
Heresy                                 # OrderedDict([('Horus', 'Heresy'), ('Chaos', 'Chaos Heresy'), ('Crusade', 'Anti Heresy')])
a = Heresy.keys()
b = Heresy.values()
a                                      # odict_keys(['Horus', 'Chaos', 'Crusade'])
b                                      # odict_values(['Heresy', 'Chaos Heresy', 'Anti Heresy'])
x = list(a)
y = list(b)
x[1]                                   # 'Chaos'
y[0]                                   # 'Heresy'


D = {"a":1, "b":2, "c":3}
D                                      # {'a': 1, 'c': 3, 'b': 2}
K = D.keys()
K | {"x": 4}                           # {'a', 'c', 'b', 'x'}
K                                      # dict_keys(['a', 'c', 'b'])

D = {"a":1, "b":2, "c":3}
D.keys() & D.keys()                    # пересеченеи представления ключей, возвращает {'a', 'c', 'b'}
D.keys() & {"b"}                       # Пересечение представления ключей и множества, возвращает {'b'}
D.keys() & {"b": 1}                    # Пересечение представления ключей и словаря, возвращает {'b'}
D.keys() | {"b", "c", "d"}             # Объединение представления ключей и множества - {'d', 'b', 'c', 'a'}


D = {"a":1, "b":2, "c":3}
V = D.values()
V & {"x": 4}                           # вернёт исключение


Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
Anime = Heresy.keys()
Story = Anime & {"Horus Heresy": "Anime Chaos"}
Story                                  # вернёт множество = set()

anime = {"Major": 1, "Ghost": 2, "Complex": 501}
list(anime.items())
anime.items() | anime.keys()          # {'Complex', 'Major', ('Complex', 501), ('Ghost', 2), ('Major', 1), 'Ghost'}
anime.items() | anime                 # {'Major', 'Complex', ('Major', 1), 'Ghost', ('Complex', 501), ('Ghost', 2)}
anime.items() | {("c", 3), ("d", 4)}  # {('c', 3), ('Ghost', 2), ('Major', 1), ('Complex', 501), ('d', 4)}
Heresy = dict(anime.items() | {("c", 3), ("d", 4)}) 
Heresy                                # {'Major': 1, 'c': 3, 'Ghost': 2, 'Complex': 501, 'd': 4}

Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
Ks = Heresy.keys()
Ks = list(Ks)     
for x in Ks: print(x, Heresy[x])

""" возвращает
Major ghost
unit 501
Bato boevik
story 404
Gato enemy
>>>
""" 
 
Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
for x in sorted(Heresy): print(x, Heresy[x])

""" возвращает
Bato boevik
Gato enemy
Major ghost
story 404
unit 501
>>>
""" 

Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
if "c" in Heresy: print("present", Heresy["c"])
else:
    print("no")

Heresy = dict(Major = "ghost", Bato = "boevik", Gato = "enemy", unit = 501, story = 404)
print(Heresy.get("c"))                       # возвращает None
print(Heresy.get("Major"))                   # возвращает ghost
print(Heresy.get("ghost"))                   # возвращает None
if Heresy.get("c") != None: print("present", Heresy["c"])
else:
    print("Lets go to nect chapter of this book")




