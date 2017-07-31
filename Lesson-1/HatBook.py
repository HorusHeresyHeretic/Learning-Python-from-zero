# слева переменная = справа данные

Ghost = 2 + 2
print(Ghost)
str(Ghost)    # эти данные записаные через переменную и имею вид строки
print(Ghost)

Ghost_int = 2    # эти данные записаны через переменную и имею вид числа
Ghost_int = Ghost_int * 2
print(Ghost_int)
  
Ghost_int = 1     # Ghost_int - имя переменной   # еденица - данные  #  знак равно присвоил данным переменную Ghost_int
print(Ghost_int)

Ghost_str = "Ghost"
print(Ghost_str)
 
Ghost_str = "Ghost" * 2
print(Ghost_str)

ghost = 404     
kill_day = 5
day = 22
ghost = ghost - kill_day * day
ghost    # эта операция называется - вызов переменной

Ghost = 1
Shell = 2
x = Ghost + Shell         # это фукнция коннетации - соединение строк
print(x) 

var_int = 10       # целое число
var_float = 8.4         #  число с плавающей точкой - дробь
var_str = "No"             #  строка
big_int = var_int * 3.5
var_float = var_float - 1
var_int / var_float
big_int / var_float
var_str = var_str * 2 + "Yes" *2
var_int
var_float
big_int
var_str
  
var_str = "No"
var_str = var_str * 2 + "Yes" *2
var_str
'nono'

_str = "No"
_str = _str * 2 + "Yes" *2
_str
print(_str)

x = 12 - 5 # это не логическая операция, # а операция присваивания переменной x результата выражения 12 — 5
x == 4 # x равен 4
x == 7 # x равен 7
x != 7 # x не равен 7
x != 4 # x не равен 4
x > 5 # x больше 5
x < 5 # x меньше 5
x >= 6 # x больше или равен 6
x <= 6 # x меньше или равен 6

x = 8
y = 13
x == 8 and y < 15 # x равен 8 и y меньше 15
x > 8 and y < 15 # x больше 8 и y меньше 15
x != 0 or y >15 # x не равен 0 или y меньше 15
x < 0 or y >15 # x меньше 0 или y меньше 15

x = 10
y = 101
x == 9 and y > 101
x > y and y < x
x < y and y > x
x > 9 or y > x
x == y or y == x
x < y or y > x
x == y or y < x
x!= y or y != 9

str1 = 'Ghost'
str2 = 'Shell'
str1 < "Solid" and str2 != 'Shell' # в обоих случаях неверно

str1 = 'Ghost'
str2 = 'Shell'
str1 < "Solid" or str2 != 'Shell' # верно в обоих случаях

str1 = 'Ghost'
str2 = 'Shell'
str1 == "Ghost in the Shell" and str2 == 'Shell' # строки не цифры детка - неверно

str1 = 'Ghost'
str2 = 'Shell'
str1 == "Ghost in the Shell" or str2 == 'Shell' # строки не цифры детка - верно

print ('HI')
tovar1 = 50
tovar2 = 52
if tovar1 + tovar2 > 99 :
	print ('Low Money')
else:
	print ('You buy it')
print ('CIA')

Ghost = 44
if Ghost < 0 :
    print ('Big Ghost')
else:
    print ('Small Ghost')

Ghost = 404
kill_day = 5
day = 22
Ghost = Ghost - kill_day * day
x = 204
if Ghost < x :
    print ('Big Ghost')
else:
    print ('Small Ghost')

x = -10
if x > 0 : # false
    print ('1')
elif x < 0 :      # true
    print ('-1')
else :             # сработает если наверху false
    print ('0')
                       
Ghost = "Shell" # на самом деле это неведомая хуйня, Я ПРИСВОИЛ ДАННЫМ "Shell" ИМЯ ПЕРЕМЕННОЙ "Ghost" И теперь обращаюсь к данным в ячейке памяти через имя Ghost
x = 3
if Ghost == 0 :
    x = 0
elif Ghost == 1 :
    x = 1
elif Ghost == 2 :
    x = 2
elif Ghost == 3 :
    x = 3    # True
elif Ghost == 4 :
    x = 5
elif Ghost == 5 :
    x = 5
else :
    print ("Error")
print(Ghost)

result = "no result"
Ghost = 3
if Ghost == 0 :
    result = 0
elif Ghost == 1 :
    result = 1
elif Ghost == 2 :
    result = 2
elif Ghost == 13 : # False
    result = 3    
elif Ghost == 4 :
    result = 5
elif Ghost == 5 :
    result = 5
else :
    print ("Error")
print(result)

Ghost = 5
Shell = 10
if Ghost > Shell:
    x = Ghost - Shell
elif Ghost < Shell:
    x = Ghost + Shell
else:
    x = Ghost
x
print(x) # как отпринтить Х не как Х а как 23??? - нужно использоваться фукнцию print() 
print(Ghost)

Ghost = 'Ghost'
Shell = 'Shell'
Enemy = 'Enemy'
Kill_day = 'Kill_day'
Anime_day = 'Anime_day'
x = 'god1'
y = 'god2'
z = 'god3'
q = 'devil'
Ghost = x 
Shell = y 
Enemy = z 
Kill_day = q
x = 11      # без этой строк всё равботает  и хреновина внизу коннетирует строки до god1god2god3devil - а, с этой строкой хреновина внизу ругаеться на то что нельзя складывать числа и строки
Anime_day = x + y + z + q

Ghost = 'Ghost'
Shell = 'Shell'
Enemy = 'Enemy'
Kill_day = 'Kill_day'
Anime_day = 'Anime_day'
x = 'god1'
y = 'god2'
z = 'god3'
q = 'devil'
Ghost = x 
Shell = y 
Enemy = z
q = x + y + z 
Kill_day = x + y + z
Anime_day = Kill_day and Kill_day != Ghost
if Anime_day == Kill_day:                                 # судя по всему внутри могут быть любые значения не связанная с первоначальной переменной
    Ghost = 404
    kill_day = 5
    day = 22
    Ghost = Ghost - kill_day * day
    x = 204
    if Ghost < x :
        print ('Big Ghost')
    else:
        print ('Small Ghost')
elif Anime_day != Kill_day:  
    Ghost = 404
    kill_day = 6
    day = 22
    Ghost = Ghost - kill_day * day
    x = 204
    if Ghost > x :
        print ('Big Ghost')
    else:
        print ('Small Ghost')
elif Anime_day != Kill_day:
    print(Kill_day)
else:
    print(Python)

x = 1
y = 2
z = 3
Ghost = x + y + z
if Ghost < 0:
    print('Shell')
elif Ghost > 10:
    print(x)
    if Ghost < 10:
        print(y)
elif Ghost != 6:
    print(x)
else:
    print(z)

a = 1
b = 2
if a > b :  # false - ничего не делает: не принтит(а), переходит к следующей строке с функцией elif
    print(a)
elif a != b : # true - исполняет команду: принтит (a + b), завершает алгорит - ниже ничего не читает. 
    print(a + b)
elif a < b : # true - ничего не делает потому что в алгоритме if-elif уже есть true; алгоритм завершился.
    print(a)
if a < b :  # true - исполняет комнаду, на if-elif выше не смотрит потому что наверху работает ветвление.  
    print(b)

str1 = '+'
i = 0
while i < 10:
    print(str1)
    i = i + 1

Ghost1 = 0
Ghost2 = 1
print(Ghost1)
print(Ghost2)
n = 20
i = 0
while i < n:
    Ghost_sum = Ghost1 + Ghost2
    Ghost1 = Ghost2
    Ghost2 = Ghost_sum
    i = i + 2
    if Ghost_sum > 8 and Ghost_sum < 89:   # это промежуточное (неправильное) решение к практической работе по циклу while из учебника, использовавние фукнции if - тру, остально фейл. см.ниже.
        print(Ghost_sum)

Ghost1 = 0
Ghost2 = 1
print(Ghost1)
print(Ghost2)
n = 40
i = 0
while i < n:
    Ghost_sum = Ghost1 + Ghost2
    Ghost1 = Ghost2
    Ghost2 = Ghost_sum
    i = i + 2
    if i > 10 and i < n:    # задаю критерии вывода переменных через if - это правильное решение!
        print(Ghost_sum, end = " ")

Ghost1 = 0
Ghost2 = 1
print(Ghost1)
print(Ghost2)
n = 40
i = 0
while i < n:
    Ghost_sum = Ghost1 + Ghost2
    Ghost1 = Ghost2
    Ghost2 = Ghost_sum
    i = i + 2
    print(Ghost_sum, "start")          # добавляют в принти индекс старт для того что бы разбираться в результатах визуально - очень полезно.
    if i > 10 and i < n:    # задаю критерии вывода переменных через if - это правильное решение!
        print(Ghost_sum, "finish" , end = " ")
    elif i > 10:     # нагло использую ещё один if через elif
         print("stop", end = " ")
         break
        
Ghost1 = 1
Ghost2 = 2
Ghost_sum = Ghost1 + Ghost2
print(Ghost_sum + Ghost_sum, end = " ")     # коррекция результатов алгоритма путём коннетации

(range(10,100,5)) == (range(10,90,5))    # простая и понятная фигня (сравнивает две прогрессии)

Ghost = 1
Shell = 2
if Ghost > Shell:
    print(Ghost in range(1,10,1))
elif Ghost < Shell:
    print(Shell in range(1,10,2))       # взовращает false, почему - пока не знаю.

input() # работает и без ничго - но криво, 

str(input("Ваше любимое аниме:"))  #  добавляет необязательный параметр строчного вида

input("Ghost") # добавляет необязательный строчный параметр ( вроде подсказки за скобочка в принт - когда к длинному ряду чисел добавили индекс )

input(10/5) # работает, возвращает 2.0

int(input('сколько жизней у кошки?')) # оперирует числами

float(input('сколько жизней у кошки?')) #  оперирует дробями

Ghost = input('Name') #  программа оперирует данными которые я ввёл с клавиатуры
Shell = Ghost
print(Shell)

Ghost = input()   # при этом фукнции input() на самом деле пофиг что писать в скобочки
Shell = Ghost
print(Shell)

thisis = input("What is your name")
itis = int(input("How old are you"))
helivein = input("where are you live")
print(thisis, itis, helivein)

x = int(input("4*100-54"))   # я смог в практическую работу: обрати внимание на фунцию int. ## без неё 346 с клавиатуры будет строкой и при сранвнении с Y алгоритм вернёт false (bad) 
y = 346
if x == y:                   # получается что ниже стоящие операторы опередляют тип переменных на входе при использовании input(), если сравниваю числа то на входе должен быть int(input()) 
    print ("good")
else:                        # ФИЧА - конкретной в этой ситуации Питон показал что умеет в сранвнеие str и int переменных, при попытке сравнить строку с числом выдал bad и завершил алгоритм без ошибок.
    print ('bad')


x = int(input("4*100-54"))   
y = 346
while x != y:                   
    print ('bad')      #   без break - получается бесконечный цикл при вводе неправильного ответа юзером,  при этом корректно работает при вводе правильного ответа и возвращает good
else:                        
    print ('good')

x = int(input("4*100-54"))   
y = 346
while x != y:                   
    print ('bad')      #   без break - получается бесконечный цикл при вводе неправильного ответа юзером,  при этом корректно работает при вводе правильного ответа и возвращает good
    break              #   с помощью break алгоритм отрабатывает корректно, но при этом цикл while НЕ отрабатывает на автомате до тех пор пока юзер не введёт правильный ответ с клавы. 
else:                        
    print ('good')     #   в итоге приходиться перезапускать алгоритм ручками для повторных попыток ввода с клавы, потому что break отправил нас ниже к else, решение этой проблемы ниже.  

x = int(input("4*100-54"))   
y = 346
while x != y:                   
    print ('bad')
    x = int(input("4*100-54"))    # чувствую себя паравозиком, который смог - это очень важная строка, она сработала как break но при этом запросила юзера ввести данные с клавы и повторила цикл while.
else:                        
    print ('good')

len('ghost in the shell')         # len() - возвращает число символов в строке: считает буквы и пробелы между ними.

"Ghost" + "Shell" + "Ghost"         # коннетация

"Shell" * 20    # дублирование, выполняет только в случае,  * int  -  дублирует на число указанное после фукнции *

"Ghost"[0]     # [x] - оператор индексирования строки, обращается к строке и извлекает символ указанный в скобках
"Ghost"[1]
"Ghost"[2]

Ghost = "Anime and Major"    #    оператор можно использовать после записи данных через переменную в отношении переменной, т.е 
Ghost[4]                     #    комп знает что переменная Ghost - это строка "Anime and major" и может её проиндексировать.

Ghost = "Anime and Major"    #    оператор можноиспользовать после записи данных через переменную в отношении переменной, т.е 
Ghost[-1]                    #    комп знает что переменная Ghost - это строка "Anime and major" и может её проиндексировать. 
Ghost[-5]                    #    можно работать с конца через минус (начиная с [-1] и делать это можно сколько душе угодно.

x = "Ghost in the Shell"     #    по факту комп видит переменную в формате последовательности символов которые уже были проиндексированы, когда я записал данные через переменную
x[0]
y = x[0]
print(y)
z = x[4]
print(z)

x = "Ghost in the Shell"     #    т.е х = "Ghost in the shell" где  x это данные в формате G[0]H[1]O[2]S[3]T[4] [5]I[6]N[7] [8]T[9]H[10]E[11] [12]S[13]H[14]E[l5]L[16]L[17] итого 18 начиная с 0    
y = x[0]                     #    поскольку эти данные уже существуют - им можно присваивать любые переменные через оператор индексирования.
print(y)
z = x[4]
print(z)

"Ghost in the Shell"[0:4]   #    срез с 0 до 4 символа строки, не включая 4ый символ

"Ghost in the Shell"[:4]    #    срез без указания стартавой позиции - до 4 символа

"Ghost in the Shell"[0:]    #    срез без указания заключительной позиции - до конца строки

"Ghost in the Shell"[0:11:2] #    срез c указанием стартовой и заключительной позиции с шагом  - стартовая позиция 0, заключительная позиция 11, шаг 2.


Ghost = "Warhammer40K"
Ghost[0]                    #     первый с начала
Ghost[-1]                   #     первый с конца
print(Ghost)
Ghost[2]                    #     третий с начала  
Ghost[-3]                   #     третий с конца
len("Warhammer40K")         #     длинна строки

Heresy = "God Emperor Was Banned By The Horus Banhammer"
Heresy[0:8]
len(Heresy)                #      оператор len() также можно использовать по отношению к переменной, возвращает длинную строки (в данном случае 45 символов, 39 букв и 6 пробелов)  
Heresy[21:25]
Heresy[2:45:3]             #      индексы кратные 3 с начала, 3ий индекс.... 45индекс

[1985, -404] + [303, "Ghost", "Shell"]    # внутри скобочек [] находиться список - упорядоченная последовательность, конкретно в этом случае производиться операция коннетации по отношению к 2м спискам 

[404, "anime", 303, "Ghost"] * 2          # операция дублирования списка

x = 1
y = [404, "anime", 303, "Ghost"] * x      #  я супер кодер:  к списку можно обращаться через переменную
print(y) 

anime = ["Ghost", "In", "The", "Shell"]
major = [["Stand"], ["Alone"], ["Complex"]]
story = anime + major
print(story)
len(story)
story[0:-1:2]                 # срез от начала до -1 с шагом два, где -1 это последний индекс, как и в случае с 0:4 - (-1) т.е последний индекс - не будет включён в срез.
story[0:7:2]                  # срез от начала до конца с шагом два


animestr = "GhostInTheShell"
animelist = ['Ghost', 'In', 'The', 'Shell']
animestr[3] = 0                                 # попытка перезаписать данные в строке "GhostInTheShell" в части индекса [3] ( буковки - s ) не прокатит
animelist[3]
animelist[3] = "Major"                          # а вот заменить индекс в списке - не проблема.
print(animelist)
animelist[0:-1] = "Tatikoma"                    # можно заменить срез
print(animelist)
animelist[0:4] = [404,303]                      # всяко можно
print(animelist)
batolist = animelist * 2 + animelist[0:-1]      # новый список по имени Бато
type(animelist)                                 # посмотрел что из себя представляет animelist - это не строка, это список.
type(animelist[0:-1])
type(batolist)
print(batolist)
storylist = animelist                           # новая переменная для списка animelist
print(storylist)
type(storylist)
storylist[0] = 11                               # новые данные для индекса от новой переменной
print(animelist)

# пример попроще

xlist = [1,2,3,4,5,6,7,8,9,10]                  #    записываю в комп список через переменную x
ylist = xlist + xlist                           #    записываю в комп переменную y - которая воспроизводит результат коннетации списков
zlist = ylist                                   #    присваиваю переменной y , которая отвечает за результат коннетации списков ещё одну переменную z
zlist[0] = 11                                   #    вношу измненеия в индекс переменной z - что автоматически приводит к замене индекса в переменной y 
print(ylist)                                    #    все счастливы, все переменные имеют тип list, всё работает

alist = [1,2,3, "Ghost", "Shell"]
blist = [["Bato", "Major", 11], ["Stand", "Alone", "Complex"]]
alist[1]
len(blist)
xlist = blist
xlist[4] = 11               # неправильно указан диапазон - потому что в списке состоящем из списков колличество индексов равно колличеству списков, можно проверить через len()
xlist[1] = 11
print(blist)
slist = alist + blist
print(slist)
len(slist)
animelist = slist[4:7]     # снимаю срез со спика и сразу присваиваю этому срезу переменную animelist
print(animelist)
animelist = animelist + ["Anime", "Heresy"]
print(animelist)
len(animelist)
animelist[5:7] = [56,84]   #  ОБРАТИ ВНИМАНИЕ! - позволяет удлиннять список без операции коннетации: я просто записал значения для индекса, которые указал. 
print(animelist)           #  переменная animelist - это список списков, с длинной в 5, следовтаельно 6 и 7 не существует, однако комп принял это как есть.


# Дзен

anime = [11, "Ghost", "In" , "The", "Shell", "Major", 11]
print(anime)
len(anime)
anime[0:3] = ["Story", "Heresy", "Emperor", "Horus"]     # это просто Дзен питона!
print(anime)
len(anime)
anime[8:11] = ["Heresy", "Heresy", "Heresy"]
print(anime)

{'anime':'аниме',"ghost":"призрак","shell":"образ"}

dic = {'anime':'аниме',"ghost":"призрак","shell":"образ"}         # переменная[ключ]  - оператор обращения к данным словаря
dic["anime"]                                            
dic["shell"]
dic["major"] = "Призрак в доспехах"                               # операция записи новых данных - переменная[ключ] = "данные"
print(dic)
len(dic)                                                          # длинна слова - 4
type(dic)                                                         # тип - "dict"
del(dic["shell"])                                                 # удаление данныех из словаря - del(переменная["ключ"])
print(dic)

dic_anime = {'anime':'аниме',"ghost":"призрак","shell":"образ"} 
dic_heresy = {'heresy':'ересь',"horus":"Хорус","chaos":"хаос"} 
x = dic_anime + dic_heresy                                          #  питон похоже не умеет коннетировать словари друг с другом type: dict + dict = fail 
x = [dic_anime] + [dic_heresy]                                      #  но умеет делать вид, что словарь может быть списком т.е прерващать type: dict в list     
print(x)
type(x)                                                             #  на выходе закономерно получается list а не dict
x = {}
x["Cold"] = "Холод"
print(x)
type(x)    

dic_anime = {'anime':'аниме',"ghost":"призрак","shell":"образ"} 
dic_shell = {"1": "One"}
print(dic_anime)
dic_shell == dic_anime                                                      # можно проверять переменные словарей логическими операциями
dic_shell["11"] = [["Bato", "Major", 11], ["Stand", "Alone", "Complex"]]    # в словарь модно добавлять разные объекты.
print(dic_shell)
type(dic_shell)                                                             # dic_shell - объект типа dict
type(["11"])                                                                # ключ 11 - объект типа list
type([["Bato", "Major", 11], ["Stand", "Alone", "Complex"]])                # Дзен в том что объект типа dict это строка или список неупорядоченного типа, а объекты тип list,str - упорядоченные.

school = {"1a":"22","2b":"21","3a":"23","4x":"11","5a":"18","6a":"16","7b":"9","8a":"39","9n":"20","10a":"50"}
print(school["5a"])
school["1a"] = "100"
school["3a"] = "200"
school["6a"] = "300"
school["2b"] = "Good"
school["3b"] = "Bad"
del(school["10a"]) 
print(school)

anime = [101,202,303,404,505,606,707,808,909]       # это список - у списка есть индексы с 0 по 8
len(anime)                                          # 9 ( 0,1,2,3,4,5,6,7,8)
i = 0                                               # переменная i - по факту условный оператор старта работы с индексом списка, i = 0 равнозначно  "начинам с первого индекса списка т.е с 0"
for element in anime:
    anime[i] = element + 2
    i = i + 1
print(anime)

anime = [101,202,303,404,505,606,707,808,909]       # это список - у списка есть индексы с 0 по 8
len(anime)                                          # 9 ( 0,1,2,3,4,5,6,7,8)
i = 0                                               # не любит варианты больше 0, возвращает list assignment index out of range и билиберду вида [101, 202, 103, 204, 105, 206, 107, 208, 109]
for element in anime:                        # условия алгоритма: " для элементов в списке anime"
    anime[i] = element + 2                   # операция редактирования списка по индексу: " перезаписать данные в списке anime в части индекса [i] " - "присвоить данным в индексе [i] новые значения"
    i = i + 1                                # операция переборы индексов: "перебрать индексы с 0 до конца списка" ( в отличии от while - не теряет берега и не выпадает в бесконечный алгоритм ) 
print(anime)
  
Major = "Ghost In The Shell"
for bukva in Major:                         # видимо питон знает понятие element и bukva
    print(bukva, end = "*")

anime = {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"}
for key in anime:                           # видимо питон знает понятие key в словаре
    anime[key] = anime[key] + "_Me"
print(anime)

animelist = [11,"Ghost","Shell","bato"]
for i in animelist:                         # видимо питон знает что i - это индекс, поэтому команда звучит так: "для индексов в списке animelist"
    print(i)                                # отпринтить все индексы, интересно - попробуем отпринтить все ключи

anime = {"Ghost":"Major","Bato":"Major Friend","11":"Crazy Major Friends","Godo":"Evil Enemy"}
for key in anime:                           # видимо питон знает понятие key в словаре
    print(key)                              # принтит ключи, принтить данные не умеет. (?) # - я пытался заставить его отпринтить данные стоящие справа от : в словаре - не робит.


Major = ["Ghost","Shell","Anime","Bato"]
for i in Major:
    print(i)                               # сильная сторона цикла for в питон в том, что он всё делает последовательно. см . результат.
    for j in i:
        print(j)
        
Major = ["Ghost","Shell","Anime","Bato"]              # список из 4х строк
for i in Major:                                       # для индексов в списке
    for j in i:                                       # для букв в списке
        print(j,end = "-")                            # отпринтить через дефис


Shell = [11,22,33,44,501]
i = 0
for j in Shell:                                      # вместо j может быть любая фигня - в языке питон это не важно, важно что есть команда "для данных в переменной". 
    Shell[i] = float(j)                              # команда звучит так: " для каждого индекса - индекс число с плавающей точкой"
    i = i + 1
print(Shell)

Shell = [11,22,33,44,501]
i = 0
for j in Shell:                                      # вместо j может быть любая фигня - в языке питон это не важно, важно что есть команда "для данных в переменной". 
    Shell[i] = str(j)                                # команда звучит так: " для каждого индекса - индекс является строкой"
    i = i + 1
print(Shell)
      
Shell = [11,22,33,44,501]
i = 0
for j in Shell:                                      # вместо j может быть любая фигня - в языке питон это не важно, важно что есть команда "для данных в переменной". 
    Shell[i] = {}                                    # команда звучит так: " для каждого индекса - индекс является словарём"
    i = i + 1
print(Shell)  

Shell = [11,22,33,44,501]
i = 0
for j in Shell:                                      # вместо j может быть любая фигня - в языке питон это не важно, важно что есть команда "для данных в переменной". 
    Shell[i] = []                                    # команда звучит так: " для каждого индекса - индекс является списком"
    i = i + 1
print(Shell) 

Shell = [11,22,33,44,501]
i = 0
for j in Shell:                                      # вместо j может быть любая фигня - в языке питон это не важно, важно что есть команда "для данных в переменной". 
    Shell[i] = {}                                    # команда звучит так: " для каждого индекса - индекс является словарём"
    i = i + 1
print(Shell)
type(Shell)

a = int(input("Введите первое число"))               # исходная задача cтрока 13, далее оптимизируем код   - нужно сделать 6 операций по вводу даных в 6 разных переменных
b = int(input("Введите второе число"))
if a > b:
    print(a-b)
else:
    print(b-a)

c = int(input("Введите первое число"))
d = int(input("Введите второе число"))
if c > d:
    print(c-d)
else:
    print(d-c)

e = int(input("Введите первое число"))
f = int(input("Введите второе число"))
if e > f:
    print(e-f)
else:
    print(f-e)  

i = 0
while i < 3:
    a = int(input("Введите первое число"))               # исходная задача црока 13, оптимизация через while, делает 6 операций по вводу, но переменных всего 2 
    b = int(input("Введите второе число"))               # при каждом витке цикла преддыдущие данные переменных a b утрачиваеться в процессе перезаписи данных
    if a > b:
        print(a-b)
    else:
        print(b-a)
    i = i + 1                                            # цикл повторяется три раза

def diff():                                              # def - команда на создание фукнции, diff - имя фукнции (может бть любым как и имя переменной)
    m = int(input("Введите первое число"))
    n = int(input("Введите второе число"))
    if m > n:
        print(m-n)
    else:
        print(m-n)
        return m,n                                      #  возвращает  m,n в основную ветку программы с сохранения типа перменной ( число, строка и т.д ) 
a,b = diff()                                            #  начинается основная ветка программы, в которой присуствуют переменные  m,n типа int
c,d = diff()
e,f = diff()


def summ():                                            # функция на вычисление суммы трёх чисел, которые пользовтель вводит с клавиатуры
    a = int(input("Введите первое число"))             # ввод данных в формате int в адрес переменной a, переменная а существует только внутри фукнции и может быть использована в основном алгоритме.
    b = int(input("Введите второе число"))
    c = int(input("Введите третье число"))
    x = a + b + c                                      # операция с данными, которую необходимо провести внутри фукнции; в данном случае сложение чисел, за результат отвечает переменная x
    return x                                           # вывод данных из функции по переменной x  (интересно что можно здесь с этим в основном аглоритме )
a = summ()                                             # присваивание данным фукнции переменной a - для того что бы алгоритм мог к ним обращаться
print(a)

def summ():                                            # def - команда создания функции  summ() - имя фукнции, () - дополнительных условий нет.
    Ghost = 1                                          # здесь и далее - переменные и данные которая обрабатывает фукнция
    Shell = 2
    Anime = 11
    x = Ghost + Shell + Anime                          # алгоритм, который проводит фукнция с данными содержащимся в поле фукнции, результату алгоритма назначенна переменная "x"
    return x                                           # вывод данных содержащихся в переменной "x" в поле основного алгоритма 
x = summ()                                             # присваивание данным содержащимся в фукнции summ() переменной "x"
print(x)                                               # вывод результата на экран.     


def anime():
    """ Anime story"""        # строка домкументации фукнции, задаёться в тройных кавычках, предназначенная для описания фукнции, может быть прочитана комнадой __doc__ Пример "print anime_div.__doc__"
    story = 11
    Major = 1
    ghost = Major * 11
    print(ghost)
anime                         # строка индитификации фукнции - возвращает адрес ячейки памяти, в которой записана фукнция.
type(anime)                   # на данном этапе питон, считает что anime - фукнция
print(anime)                  # принтит адрес фукнции в памяти
x = anime
type(x)                       # - питон считает что Х это фукнция
print(x)                      # - принтит адрес фукнции в памяти
x = anime()
type(x)                       # - питон считает что х это "NoneType"
print(x)                      # - принтит None


def one():
    def two():
        a = int(input("Введите число"))
        return a              # a - локальная переменная функции  two(), возвращаю её в стек фукнции one()
    a = two()                 # присваиваю данным фукнции two() локальную переменную  "a" ( если заменить а на х - работать не будет )
    i = a + 5                 # произвожу действия с переменной "а" в стеке фукнции one()
    print(i)
one()                         # вызываю функцию one() в глобальном алгоритме, она запращивает ввод числа с клавиатуру и добавляет к нему 5. 

                  
def anime():
    """ Anime story"""        # строка домкументации фукнции, задаёться в тройных кавычках, предназначенная для описания фукнции, может быть прочитана комнадой __doc__ Пример "print anime_div.__doc__"
    story = 11
    Major = 1
    def shell():
        x = story - Major                # = 10
        return x                         # возвращаю х в стек фукнции anime()
    x = shell()
    Ghost = Major * story - x            # Ghost = 11 * 1 - 10
    print(Ghost)                         # без этой строки, строка animе() не выведет результат на экран 
anime()                                  # возвращает еденицу


def anime():
    """ Anime story"""        # строка домкументации фукнции, задаёться в тройных кавычках, предназначенная для описания фукнции, может быть прочитана комнадой __doc__ Пример "print anime_div.__doc__"
    story = 11
    Major = 2
    Ghost = Major * 11
    print(Ghost)
    def shell():
        x = story - Major                # = 10
        return x                         # возвращаю х в стек фукнции anime()
    x = shell()
    Ghost = Major * story - x            # Ghost = 11 * 1 - 10
    print(Ghost)                         # без этой строки, строка animе() не выведет результат на экран 
anime()           
anime                         # строка индитификации фукнции - возвращает адрес ячейки памяти, в которой записана фукнция.
type(anime)                   # на данном этапе питон, считает что anime - фукнция
print(anime)                  # принтит адрес фукнции в памяти
x = anime
type(x)                       # - питон считает что Х это фукнция
print(x)                      # - принтит адрес фукнции в памяти
x = anime()
type(x)                       # - питон считает что х это "NoneType"
print(x)                      # - принтит None


def anime():
    """ Anime story"""        # строка домкументации фукнции, задаёться в тройных кавычках, предназначенная для описания фукнции, может быть прочитана комнадой __doc__ Пример "print anime_div.__doc__"
    story = 11
    Major = 2
    Ghost = Major * 11                 # = 22
    print(Ghost, "anime1")
    def shell():
        x = story - Major                # = 9
        return x                         # возвращаю х в стек фукнции anime()
    x = shell()
    Ghost = Major * story - x            #  11 * 2 - 9 = 13
    print(Ghost, "anime2")
    print(x, "shell")                    # без этой строки, строка animе() не выведет результат на экран 
anime()                                  # крутой Дзен - фукнция shell() смога прочитать локальные переменные 'story' и 'major' из фукнции anime(), произвести с ними действия и получить переменную "x"


def calc(a, b):                          # параметр "а" соответствует аргументу num1, параметр "b" соответствует аргументу num2; переменные "a" и "b" являются локальными, основной скрипт их не видит.  
    a = a / 2                            # 10 = 10 / 2
    b = b + 10                           # 5 = 5 + 10
    print(a*b)                           # 5*15 =15
    print(num1 + num2)                   # num1 и num2 - глобальные переменные, их видит и фукнция и основной скрипт.
num1 = 10
num2 = 5
calc(num1, num2)

def anime(shell):
    n = shell * 5
    print(n)
shell = 11                              # глобальная переменная: число
anime(shell)
shell = "Ghost"                         # глобальная переменная: строка
anime(shell)
shell = [11,22,33]                      # глобальная переменная: список
anime(shell)

def anime(shell):
    n = shell * 5
    return [n, shell]                   # WTF!& как это работает?
shell = 9
n = anime(shell)
shell = n
anime(shell)
type(anime(shell))

def anime(n):                          # n - параметр
    if n < 3:                          # если параметр "n" - который соотвествует аргументу "a" меньше 3 
        n = 10*3                       # тогда: параметр "n" - равен 30
    return n                           # вернуть переменную "n" - в стек ( без ретурна b и связанная с ним фукнция anime(a) - "nontype" )
a = 1                                  # a - аргумент
b = anime(a)                           # ВАЖНО: 'b' - это "return n'
a                                      # обратиться к переменной а
b                                      # обратиться к переменной b


       








