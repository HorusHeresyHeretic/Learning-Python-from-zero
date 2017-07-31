class game:                         
    def __init__(self, date, hostTeam, guestTeam, hostGoals, guestgoals, hostteammembers, questteammembers):             
        self.date = date                               
        self.hostTeam = hostTeam                             
        self.guestTeam = guestTeam
        self.hostGoals = hostGoals
        self.guestgoals = guestgoals
        self.hostteammembers = hostteammembers
        self.questteammembers = questteammembers                               
    def date(self):                  
        return self.date .split()[-1]     
    def hostTeam(self):                 
        return self.hostTeam.split()[-1]    
    def guestTeamt(self, percent):          
        return self.guestTeam.split()[-1]
    def hostGoals(self):
        return self.hostGoals.split()[-1]
    def guestgoals(self):
        return self.guestgoals.split()[-1]
    def hostteammembers(self):
        return self.hostteammembers.split()[-1]
    def questteammembers(self):
        return self.questteammembers.split()[-1]
FirstGame = game("01.01.2017", "AnimeTeam", "EvilTeam", "100500", "0", "Ghost in the shell characters", "Random Evil characters")
LastGame = game("01.04.2017", "AnimeTeam", "EvilTeam", "100500", "0", "Ghost in the shell characters", "Elite Evil characters")
NextGame = game("11.11.2011","EgorTeam", "BratTeam", "0", "11", "Brat Vulture", " Lina Inverse") 
FirstGame.date
FirstGame.hostTeam
FirstGame.guestTeam
FirstGame.hostGoals
FirstGame.guestgoals
FirstGame.hostteammembers
FirstGame.questteammembers
NextGame.hostGoals

a = 3                          # ссылка (a) > (3)
b = a                          # ссылка (b) > (3)
b = "spam"                     # ссылка (b) > ("spam"), ссылка (b) > (3) - разименована
a                              # возвращает 3
b                              # возвращает "spam"

a = 3                          # ссылка (a) > (3)
b = a                          # ссылка (b) > (3)
a = "spam"                     # ссылка (a) > ("spam"), ссылка (a) > (3) - разименована
a                              # возвращает "spam"
b                              # возвращает 3

a = 3                          # ссылка (a) > (3)
b = a                          # ссылка (b) > (3)
a = a + 2                      # ссылка (a) > (a + 2) - a+2 это новый объект и новая ссылка в сис.таблице 
a                              # 5
b                              # 3

L1 = [1,2,3]                   # Создание первой ссылка на объектт (Список - Изменяемый объект)
L2 = L1                        # Создание второй ссылки на тот же самый объект
L1[0] = 24                     # Изменение объекта
L1                             # Переменная L1 изменилась     - возвращает  [24, 2, 3]
L2                             # Но так же изменилась и переменная L2! - возвращает  [24, 2, 3]

L1 = [1,2,3]                   #
L2 = L1[:]                     # создаёться копия списка L1 и как следствие копия сслыки на объект L1
L1[0] = 24                     #
L1                             # [24, 2, 3]
L2                             # [1, 2, 3]


anime = {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"}
import copy                    # извлекаем модуль copy из стандартной библиотеки
a = copy.copy(anime)           # создание "поверхностной копии объект" (anime)
b = copy.deepcopy(anime)       # создание полной копии (копируються все вложенные части)
a                              # возвращает {'Bato': 'Major Friend', '11': 'Crazy Major Friends', 'Godo': 'Evil Enemy', 'Ghost': 'Major'}
b                              # возвращает {'Bato': 'Major Friend', '11': 'Crazy Major Friends', 'Godo': 'Evil Enemy', 'Ghost': 'Major'}

# в чём глубокий Дзен поверхностой копии от полной - пока не ясно. см.главы 8-9

L = [1,2,3]                   
M = L                         # M и L – ссылки на один и тот же объект
L == M                        # True - одно и тоже значение
L is M                        # True - один и тот же объект

L = [1,2,3]
M = [1,2,3]                   # M и L – ссылаються на разные объекты  
L == M                        # True - одно и тоже значение
L is M                        # False - разные объекты 

# однако!

L = 42
M = 42                       #  M и L – ссылаються на разные объекты, но здесь работает кеширование
L == M                       #  True
L is M                       #  True  - кеширование в действии
import sys
sys.getrefcount(L)           #  14 ссылок
sys.getrefcount(M)           #  14 ссылок
sys.getrefcount(42)          #  15 ссылок (15 потому что в системной таблице есть кешируемая ссылка M,L)

# PartVII

anime = ""                  # "" - пустая строка
anime = "Ghost'anime"       # строка в кавычках, возвращает - "Ghost'anime"
anime = "anime\np\ta\x00m"  # экранирование(?) последовательности, возвращает - 'anime\np\ta\x00m'
block = """..."""           # блоки в тройных кавычках, возвращает - '...'
anime = r"\temp\Ghost"      # неформатированные строки, возвращает - '\\temp\\Ghost'
anime = b"Ghost"            # не работает (!) - по Лутцу это строки байтов в версии 3.0, возвращает - b'ghost'
anime1 + anime2             # коннетация - повторение, работает так:

# вспоминаем как правильно коннетировать строки

a = "anime1"                # создать ссылку на объект "anime1"  класса str
b = "anime2"                # создать ссылку на объект "anime2"  класса str
a + b                       # провести операцию коннетации, возвращает -  'anime1anime2'
a * 2                       # повторение, возвращает - 'anime1anime1'

anime[i]                    # обращение к символу строки по индексу [i]

# вспоминаем как правильно работать с индексами

anime = "Ghost in the shell"
anime[4]                    # 't'
anime[4:-1]                 # получение среза, возвращает 't in the shel'
len(anime[4:-1])            # длинна строки (а также длинна среза)

"a %s parrot" % kind        # выражение форматирования строки - как работает до сих пор не понял.
"a {0} parrot".format(kind) # строковый метод форматирования - таже фигня, надеюсь Лутц меня научит.

"Ghost in the shell".find("a")        # вызов строкового метода. поиск, возвращает -1  
"Ghost in the shell".find("s")        # вызов строкового метода. поиск, возвращает -3
"Ghost in the shell".rstrip()         # удаление ведущих и конечных пробельных символов
"Ghost in the shell".replace("s", "x")# замена (str неизменяемый объект), возвращает 'Ghoxt in the xhell'

# объекты класса STR относяться к неизменяемым последовательностям - для их измненения нужен метод(чит).

"Ghost in the shell".split("|")       # в теории это "разделение по символу разделителю", но на практике
"Ghost in the shell".split(",")       # интепритатор  вернул список - ['Ghost in the shell']  (wtf!?)

"Ghost in the shell".isdigit()        # проверка содержимого, возвращает False  (что проверяет не понятно)
"Ghost in the shell".lower()          # преобразование регистра символов, возвращает-'ghost in the shell'
"Ghost in the shell".endswith("x")    # проверка окончания строки, возвращает False
 
"Ghost in the shell".join(strlist)    # сборка строки из списка - что делает и как работает непонятно.

"Ghost in the shell".encode("latin-1")# кодирование строк юникода, возвращает - b'Ghost in the shell'

for s in "Ghost in the shell":        # обход в цикле. работает как часы.
    print(s) 

"Ghost" in "Ghost in the shell"       # проверка на вхождение, возвращает - True

[c * 2 for c in "Ghost in the shell"] # операция дублирования при обходе символов в цикле

map(ord, "Ghost in the shell")        # адрес объекта в памятик, - <map object at 0x00000000032585C0>

"anime" 'anime'                       # кавычки и опострофы одна фигня - возвращает'animeanime'

anime = "Ghost" 'in the' "shell"      # неявная коннетация
anime                                 # возвращает - 'Ghostin theshell'

anime = "Ghost", 'in the', "shell"    # если добавить запятые - интерпретатор возвращает кортеж
anime                                 # возвращает - ('Ghost', 'in the', 'shell')

anime = "Ghost\nb\tc"
anime                                 # возвращает  'Ghost\nb\tc'
print(anime)                          # Ghost 
                                      # b	c
len(anime)                            # 9

anime = "Ghost in the shell\newline"  # игнорируеться (продолжение на новой строке)
print(anime)                          # Ghost in the shell
                                      # ewline

anime = "Ghost in the shell\\"        # Сам символ обратного слеша (остается один символ \)
print(anime)                          # Ghost in the shell\           

anime = "Ghost in the shell\'"        # Апостроф (остается один символ ‘)
print(anime)                          # Ghost in the shell'

anime = "Ghost in the shell\""        # Кавычка (остается один символ “)
print(anime)                          # Ghost in the shell"
  
anime = "Ghost in the shell\a"        # Звонок (?)
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\b"        # Забой
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\f"        # перевод формата
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\n"        # новая строка (перевд строки)
print(anime)                          # Ghost in the shell
                                      #

anime = "Ghost in the shell\r"        # возврат каретки
print(anime)                          # Ghost in the shell
                                      #

anime = "Ghost in the shell\t"        # горизонтальная табуляция
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\v"        # вертикальная табуляция
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\x24"      # Символ с шестнадцатеричным кодом xNN (не более 2 цифр)
print(anime)                          # Ghost in the shell$

anime = "Ghost in the shell\008"      # Символ с восьмиричным кодом 000 (не более 3 цифр)
print(anime)                          # Ghost in the shell 8

anime = "Ghost in the shell\0"        # Символ Null (не признак конца строки)
print(anime)                          # Ghost in the shell

anime = "Ghost in the shell\N{id}"    # Идентификатор ID базы данных Юникода
print(anime)                          # поскольку я не знаю коды Юникода - мне вернуло пару исключений

anime = "Ghost in the shell\u0501"    # 16-битный символ Юникода в шестнадцатеричном представлении
print(anime)                          # Ghost in the shellԁ

anime = "Ghost in the shell\u0005001" # 32-битный символ Юникода в шестнадцатеричном представлении
print(anime)                          # Ghost in the shell001

anime = "Ghost in the shell\other"    # \другое - Не является экранированной последовательностью
print(anime)                          # Ghost in the shell\other 
                                      # (символ обратного слеша сохраняется)

s = "a\0b\0c"                         # судя по всему 2 ну
s                                     # 'a\x00b\x00c'
print(s)                              # a b c

anime = "Ghost\0in\0the\0shell"       # \0 это null 
anime                                 # 'Ghost\x00in\x00the\x00shell'
print(anime)                          # возвращает - Ghost in the shell


myfile = open("C:\new\text.dat", "w") # не правильно - возвращает Invalid argument: 'C:\new\text.dat'
myfile = open(r"C:\new\text.dat", "w")# правильно - возвращает No such file or directory: 'C:\\new\\text.dat' 

myfile = open("C:\\new\\text.dat", "w") # ещё более правильно

path = r"C:\new\text.dat"
path                                  # возвращает 'C:\\new\\text.dat'
print(path)                           # возвращает C:\new\text.dat
len(path)                             # длинна строки 15  

anime = "\\Ghost in the shell\\"      # а если бы в конце было \" - интерпретатор вернул бы исключение  
anime                                 # '\\Ghost in the shell\\'  
print(anime)                          #  \Ghost in the shell\

anime = """Ghost in the shell        
Stand Alone Complex
Major"""
anime                                # возвращает одну строку 'Ghost in the shell\nStand Alone Complex\nMajor'
print(anime)

anime = 1
"""                                  
anime = 2
"""                                  # интерпретатор не будет использовать код между тройными кавычками
ghost = anime + 1
print(ghost)                         # возвращает  2

# также создаёт строку '\nanime = 2\n' 

"Ghost in the shell" + "stand Alone Complex"  #  'Ghost in the shellstand Alone Complex'
"Ghost in the shell" * 4                      #   Ghost in the shellGhost in the shellGhost in the shellGhost in the shell'
len("Ghost in the shell")                     #   18
print("Major" * 10)                           #   MajorMajorMajorMajorMajorMajorMajorMajorMajorMajor

anime = "Ghost in the shell"
for c in anime: print(c, end="")              #   Ghost in the shell
for c in anime: print(c, end="  ")            #   G  h  o  s  t     i  n     t  h  e     s  h  e  l  l  
"l" in anime
"a" in anime

anime = "Ghost in the shell"
anime[0], anime[-2]                           #  ('G', 'l')
anime[1:3], anime [1:], anime[:-1]            #  ('ho', 'host in the shell', 'Ghost in the shel')
anime[:3], anime[:]                           #  ('Gho', 'Ghost in the shell')

anime = "Ghost in the shell"
anime[1:10:2], anime[::2]                     #  ('hs nt', 'Goti h hl')

anime = "Ghost in the shell"
anime[::-1]                     #  обратная последовательность, возвращает 'llehs eht ni tsohG'


anime = "Ghost in the shell"
anime[5:1:-1], anime[5:1:1]     #  (' tso', '')

"Ghost in the shell"[slice(1,3)]

# Slice
    
class example:
    def __getitem__ (self, item):
        if isinstance(item, slice):
            print("You are slicing me!")
            print("From", item.start, "to", item.stop, "with step", item.step)
            return self
        if isinstance(item, tuple):
            print("You are multi-slicing me!")
            for x, y in enumerate(item):
                print("Slice #"), x
                self[y]
            return self
        print("You are indexing me!\nIndex:", repr(item))
        return self
example()[9:20]
example()[2:3,9:19:2]
example()[50]
example()["String index i.e. the key!"]
example()["start of slice":"end of slice"]

class anime:
     def __getitem__ (self, item):
        if isinstance(item, list):
            print(item, "no item")                       # ничего не возвращает - у нас пока списков нет.
        if isinstance(item, str):
            print(item)                                  # возвращает  (str) Ghost in the shell
        if isinstance(item, slice):
            print(slice)                                 # возвращает (slice) host in th
anime()["Ghost in the shell"]
anime()["Ghost in the shell"[1:11]]     

# смысл происходящего в попытке вернуть объект slice фукнцей __getitem__ в рамках методов класса anime

x = int("42")          # преобразование строки в число
type(x)                # <class 'int'>
x = str(42)            # преобразование числа в строку
type(x)                # <class 'str'>
print(x)               # 42
x = repr(42)           # преобразование числа в строку как если бы она была литералом в коде
type(x)                # <class 'str'>
print(x)               # 42
42

# Дзен фнукции repr    - эта штука возвращает нам строку в качестве объекта.

anime = repr(501)
anime + anime          # возвращает '501501'

anime = 501
anime + anime          # возыврвщает 1002

print(str("anime"), repr("anime"))     # возвращает - anime 'anime' ; в кавычках объект

anime = "401"
ghost = 1
anime + str(ghost)    # 4011 - операция коннетации строк
int(anime) + ghost    # 402 - операция сложения чисел

anime = "1.234E-10"
float(anime)          # преобразование строки в число с плавающей точкой через переменную

ord("s")              # возвращает числое значение соотвествующего байта в памяти - 115
chr(115)              # обратное преобразование, возвращает 's'

anime = ("s")
anime = chr(ord("s") + 1)    
anime                 # возвращает 't'

int("5")
ord("5") - ord("0")   # возвращает 5
ord("5") - ord("1")   # возвращает 4

anime = "1101"        # # Двоичные цифры преобразуются в числа с помощью функции ord
i = 0
while anime != "":
    i = i * 2 + (ord(anime[0]) - ord("0"))
    anime = anime[1:]
i

# интересный пример - похоже теперь я знаю как реализовать множественный счётчик.

anime = 501
i = 0
b = 0
while anime < 10000:
    i = i + 1 
    b = b + 1
    anime = anime + (i * b)
    print(anime)     


anime = "anime"
anime = anime + "Ghost"
anime                                    # 'animeGhost'
anime = anime[0] + "Shell" + anime[-1]
anime                                    #  'aShellt'
anime = "Ghost in the shell"
anime = anime.replace("Ghost", "Major")
anime                                    #  'Major in the shell'

# понятное объяснение как работает форматирование строк, через выражение

"Ghost in the %d %s shell" % (501, "anime")   # возвращает 'Ghost in the 501 anime shell'

# через метод

"Ghost in the {0} {1} shell".format (501, "anime")   # возвращает  'Ghost in the 501 anime shell'

anime = "anime"
anime = anime[3] + "XX" + anime[4]
anime                                # 'mXXe'
anime = anime.replace("m", "XX")
anime                                # XXXXe'

"Stand alone complex". replace("a", "Ghost")  #  'StGhostnd Ghostlone complex'
                                     
anime = "Ghost in the shell"
where = anime.find("Ghost")                   # поиск позиции
where                                         # 0
anime = anime[:where] + "Stand Alone Complex" + anime[(where+4):]
anime

anime = "Ghost in the shell"
anime.replace("Ghost", "Stand Alone Complex") # замнить все найденные строки

anime = "Ghost, Ghost in the shell"
anime.replace("Ghost", "Stand Alone Complex", 1)  # заменить одну подстроку.

anime = "Ghost, Ghost in the shell"
a = list(anime)                               # создать ссылку в системной таблице на список (anime)
a                                             # возвращает список
a[3] = "Ghost"
a[4] = "major"
a
anime = "".join(a)
anime                   # работает по Лутцу, возвращает 'GhoGhostmajor, Ghost in the shell'
anime.join(a)                                 # возвращает билиберду - но работает


"Ghost, Ghost in the shell".join(["Stand", "Alone", "Complex"]) # str.join() - очень полезная вещь.

anime = "aaa bbb ccc"
col1 = anime[0:3]
col2 = anime[8:]
col1                               # 'aaa'
col2                               # 'ccc'

anime = "aaa bbb ccc"
cols = anime.split()               # str.split() - разбить строку
cols                               # ['aaa', 'bbb', 'ccc']

anime = "Ghost, Ghost in the, shell"
anime.split(",")                   # ['Ghost', ' Ghost in the', ' shell']

anime = "Ghost, Ghost in the, shell"
anime.split("Ghost")               # ['', ', ', ' in the, shell'] - splitom можно бить строки по строкам 
 
anime = "Ghost in the shell\n"
anime.rstrip()                     # удаляет пробельный символ, возвращает: 'Ghost in the shell'
anime.upper()                      # преобразование регистра, возвращает: 'GHOST IN THE SHELL\n'
anime.isalpha()                    # проверяет содержимое строки, возвращает False
anime.endswith("ll\n")             # проверяет наличие подстроки в конце строки, возвращает True
anime.startswith("Ghost")          # проверяет наличие подстроки в начале строки, возвращает True

anime = "Ghost in the shell\n"
anime.find("in the") != -1         # поиск с использованием вызова метода или выражения, True
"shell" in anime                   # возвращает True
sub = "shell\n"                    # проверку на вхождение можно осуществлять с помощью переменной
anime.endswith(sub)                # возвращает True 
anime[-len(sub):] == sub           # возвращает True

anime = "ghost in the shell"
anime.capitalize()                 # 'Ghost in the shell'
anime.isalnum()                    # False

anime = "Ghost in the %d shell %s" %(501, "Stand Alone Complex")
anime                              # 'Ghost in the 501 shell Stand Alone Complex'
story = "Major story of terrible life in anime story"
title = 'Ghost %s in the 501 shell Stand Alone Complex' % story
title  # 'Ghost Major story of terrible life in anime story in the 501 shell Stand Alone Complex'

"%s -- %s -- %s" % (42, 3.14159, [1, 2, 3])  # '42 -- 3.14159 -- [1, 2, 3]'

x = 1234
res = "integers:...%d ...%-6d...%06d" % (x,x,x)
res                               # возвращает 'integers:...1234 ...1234  ...001234'

x = 1.23456789
x                                 # 1.23456789
"%e, %f, %g" % (x,x,x)            # '1.234568e+00, 1.234568, 1.23457'
"%-6.2f | %05.2f | %+06.1f" % (x, x, x)       # '1.23   | 01.23 | +001.2'
"%s" % x, str(x)                              # ('1.23456789', '1.23456789')
"%f, %.2f, %.*f" % (1/3.0, 1/3.0, 4, 1/3.0)   # '0.333333, 0.33, 0.3333'

anime = "Ghost in the shell"
sub1 = "Stand"
sub2 = "alone"
sub3 = "complex"
anime = "%sGhost %sin the %sshell" %(sub1, sub2, sub3)  # форматировать можно и через переменные
print(anime)                      # возвращает StandGhost alonein the complexshell

x = 501
y = 11
anime = x / y
i = 0
while i < anime:                  # использование цикла для вычисления числа знаков после запятой.
    story = "%f, %f, %.*f" %(x, y, i, i)
    i = i + 1
    print(story)

x = 501
y = 11
anime = x / y
i = 0
while i < 11:                     # использование форматирования для счисления переменных в цикле.
    anime = "%f, %.2f, %.*f" % (x/y, x/y, y, x/y)      
    i = i + 1
    y = y - 1
    print(i, anime)

x = 1
y = 2
"%f, %.10f" % (x, y)              # %.xf - где х число знаков после запятой
"%f, %.10f, %.*f" % (x, y, 20, 11)# 11 это - элемент обязательный для выражения - ну вот так оно работает 

a = "%(n)d %(x)s" % {"n":1, "x":"spam"}      # возвращает - '1 spam'
    
history = {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"}
story = "%(Ghost)s %(Bato)s" % {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"}
story

reply = """                                  # шаблон с замещаемыми параметрами
Greetings...
Hello %(name)s!
Your anime character type is %(type)s
"""
characters = {"name": "Major", "type": "Ghost in the shell"}           #  параметры, которыми замещаем.
print(reply % characters)

history = "Ghost"
story = "Shell"
"%(history)s %(story)s" % vars()            # возвращает 'Ghost Shell'

