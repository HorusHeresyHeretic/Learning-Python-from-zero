"Ghost in the shell"            # юникод - такой юникод. помни о майоре и всё будет ок.

a = None                        # инициализация переменной через нулевое значение
b = 1
a = b + 1
a

a = 3                           # создание переменной a. значение переменно 3
b = 4                           # создание переменной a. значение переменно 4 
a + b, a - b                    # # возвращает (7, -1)
a + 1, a - 1                    # возвращает (4, 2)
b * 3, b / 3                    # возвращает (12, 1.3333333333333333)
a * b, b / a                    # умножение и деление, возвращает (12, 1.3333333333333333)
a % 2, b ** 2                   # деление по модулю(остаток), возведение в степень, возвращает 1, 16)
2 + 4.0, 2.0 ** b               # смешивание типов, выполняет преобразование, возвращает (6.0, 16.0)
b / 2 + a                       # ((4 / 2) + 3), возвращает  5.0
print(b / (2.0 + a))            # (4 / (2.0 + 3)), возвращает 0.8
b // 2 + a                      # возвращает 5   - целочисленное деление

num = 1 / 3.0
num                             # автоматический вывод возвращает 0.3333333333333333 (по Лутцу 0....31)
print(num)                      # фукнция принт выполняет округление, возвращает 0.3333333333333333
"%e" % num                      # вывод с использованием выражения форматирования строк: '3.333333e-01'
"%4.2F" % num                   # альтернативный формат представления вещественных чисил: '0.33'
"{0:4.2F}". format(num)         # метод форматирования строк, возвращает '0.33'
repr(num)                       # судя по всему в 3.0 одна фигня, вовзаращет  '0.3333333333333333'
str(num)                        # судя по всему в 3.0 одна фигня, вовзаращет  '0.3333333333333333'

1 < 2                           # меньше чем - возвращает True
2.0 >= 1                        # больше или - равно возвращает True
2.0 == 2.0                      # равенство - возвращает True
2.0 != 2.0                      # неравенство - возвращает False

x = 2
y = 4
z = 6
x < y < z                       # возвращает True  - перед нами составная операция сранвнения
x < y and y < z                 # возвращает True
x < y > z                       # возвращает False - которая проверяет принадлежность к диапазону
x < y and y > z                 # возвращает False
1 < 2 < 3.0 < 4                 # возвращает True
1 > 2 > 3.0 > 4                 # возвращает False

1 == 2 < 3                      # тоже что и 1 == 2 and 2 < 3 возвращает False, потому что 1 не равно 2 
1 == 2 and 2 < 3                # но не тоже самое что и False < 3 (что означает утверждение 0 < 3, которое истинно)
 
a = 10
b = 4                           
a / b                           # возвращает 2.5
a // b                          # возвращает 2 ( округляет вниз)
10 / 4.0                        # возвращает 2.5
10 // 4.0                       # возвращает 2 ( округляет вниз)

import math                     # ниже - встроенная функция целочисленного интеграла
math.floor(2.5)                 # возвращает 2   (фукнция интеграла "<=x" округляет влево) 
math.floor(-2.5)                # возвращает -3  (возвращает -3 потому что -3 <= -2.5 возвращает True) 
math.trunc(2.5)                 # возвращает 2   (фукнция интеграла "->" округляет вправо) 
math.trunc(-2.5)                # возвращает -2  (возвращает -2 потмоу что -2 > -2.5 возвращает True)
  
5 / 2, 5 / -2                   # (2.5, -2.5)
5 // 2, 5 // -2                 # (2, -3)    Округление вниз: результат 2.5 округляется до 2, -2.5 до -3
5 / 2.0, 5 / -2.0               # (2.5, -2.5)
5 // 2.0, 5 // -2.0             # (2.0, -3.0)  Округление вниз: результат 2.5 округляется до 2, -2.5 до -3

import math
5 / -2                          # -2.5 сохранит дробную часть
5 // -2                         # -3 округлит результат вниз 
math.trunc(5 / -2)              # -2 вместо округления будет выполнено усечение
5 / 2                           #  2.5
5 // 2                          #  2
math.trunc(5 / 2)               #  2
math.floor(5 / 2)               #  2
math.floor(5 / -2)              # -3

2 ** 200                        #  1606938044258990275541962092341162602522202993782792835301376

1 + 1j                          # (1+1j)
1j + 1j                         # 2j
1j * 1j                         # (-1+0j)
2 + 1j * 3                      # (2+3j)
(2 + 1j) * 3                    # (6+3j)

anime = complex(11, 404)
print(anime)                    # (11+404j)
major = complex(11, 501)
print(major)                    # (11+501j)
Ghost = anime + major
print(Ghost)                    # (22+905j)
Shell = anime * major
print(Shell)                    # (-202283+9955j)
Bato = anime / major
print(Bato)                     # (0.8064805154466753-0.004248930798575989j)
print(anime.conjugate())        # сопряженное число (11-404j)
print(anime.imag)               # мнимания часть 404.0
print(anime.real)               # действительная часть 11.0
print(anime == Ghost)           # Комплексные числа нельзя сравнить, Но можно проверить на равенство - False
abs(11+404j)                    # модуль комплексного числа 404.149724730823
abs(11+501j)                    # модуль комалексного числа 501.1207439330366
pow(11-404j, 2)                 # возведение в степень (-163095-8888j)

oct(404), hex(404), bin(404)    # возвращает ('0o624' - 8ое, '0x194'- 16ое, '0b110010100' -2ое) число
int("64"), int("100", 8)        # возвращает (64, 64) - второй аргумент == основания системы счисления
int("40", 16), int("1000000", 2)# возвращает (64, 64) ( int("100000", 2) - вернёт 32)
int('0b110010100', 2)           # возвращает 404, что бы работало надо указывать систему счисления (2)
int('0o624', 8 )                # возвращает 404, что бы работало надо указывать систему счисления (8)
int('0x194', 16)                # возвращает 404, что бы работало надо указывать систему счисления (16)

eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000')               # возвращает (64, 64, 64, 64)

"{0:o}, {1:x}, {2:b}".format(64, 64, 64)              # возвращает '100, 40, 1000000'
"%o, %x, %X" % (64, 255, 255)                         # возвращает  '100, ff, FF'

0o1, 0o20, 0o377                                      # возвращает (1, 16, 255)

x = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF
x
oct(x)                                                # возвращает десятичное значение
hex(x)                                                # возвращает восьмиричное значение
bin(x)                                                # возвращает двоичное значение

x = 1                         # 0001
bin(x)                        # '0b1'
int(0b1)                      # 1
int("0b1", 2)                 # 1
x << 2                        # возвращает 4 - это сдвиг влево на два бита: 0100
y = x << 2                    # проверяем через новую переменную - y
bin(y)                        # возвращает '0b100'
int(y)                        # возвращает 4
x | 2                         # побитовое ИЛИ, возвращает 3 - 0011
x & 1                         # побитовое И, возвращает 1 - 0001
z = y | 2
print(z)                      # возвращает 6
bin(z)                        # возвращает '0b110'
bin(z), z.bit_length()        # возвращает ('0b110', 3) 
bin(z), x.bit_length()        # возвращает ('0b110', 1) 

# bin(name), name.bit_length() - точечная нотация для встроенной фукнции, которая который возвращает
# количество битов, необходимых для представления числа в двоичном виде. Name - переменная или число.

x = 404
bin(x), x.bit_length()       # ('0b110010100', 9)
bin(404), (404).bit_length() # ('0b110010100', 9)

import math
math.pi, math.e              # (3.141592653589793, 2.718281828459045) - константы
math.sin(2 * math.pi / 180)  # 0.03489949670250097 - синус,косинус, тангенс
math.sqrt(404), math.sqrt(11)# (20.09975124224178, 3.3166247903554) - квадратный корень 
pow(3, 9), 3 ** 9            # (19683, 19683) - возведение в степень.
abs(-404.0), sum((1,4,11))   # (404.0, 16) - абсолютнае значение, сумма
min(11, 4, 404, 2)           # 2
max(11, 4, 303, 501)         # 501

import math
math.floor(2.567), math.floor(-2.567)        # (2, -3) округление вниз, до ближайщего наименьшего целого.
math.trunc(2.567), math.trunc(-2.567)        # (2, -2) усечение - отбрасывание дробной части
int(2.567), int(-2.567)                      # (2, -2) усечение - преобразование в целое число
round(2.567), round(2.467), round(2.567, 2)  # (3, 2, 2.57) округление 
"%.1f" % 2.567, "{0:.2f}".format(2.567)      # ('2.6', '2.57') округление при отображении (‘2.6’, ‘2.57’)

round(100 / 33, 1), round(100 / 33, 10)      # возвращает (3.0, 3.0303030303)  
# round(x / y, z) == x - делимое, y - делитель, z - число знаков после запятой

(1 / 5), round(1 / 5, 2), ("%.2f" % (1/ 5))  # возвращает (0.2, 0.2, '0.20')
(1 / 5), round(1 / 5, 2), ("%.2f" % (1/ 6))  # возвращает (0.2, 0.2, '0.17')

("%.3F" % (1/ 3))                            # возвращает '0.333'
# "%.XF" % (Y/ Z)) == Y - делимое. Z - делитель. X - число знаков после запятой.
# по факту мы сначал задаём формат форматирование, а уже потом что форматируем.

import random
random                      # ХМ! <module 'random' from 'J:\\HiEnd\\Ghost in the Shell\\lib\\random.py'>
random.random()             # 0.9813273589330282
random.random()             # 0.8377182577273734
random.randint(1, 10)       # 2
random.randint(1, 10)       # 10

import random
random.choice(["Ghost in the Shell", "Stand Alone Complex", "Anime", "Solid State"])
random.choice(["Ghost in the Shell", "Stand Alone Complex", "Anime", "Solid State"])

from decimal import Decimal                                                # в introIV 336 не так(!) 
data = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.4")   # это конструктор: d_D
data + 1                                                                   # Decimal('0.9')
  
import decimal                      
data = decimal.Decimal("3.141")      
data + 1  
data = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.4")   # NameError: name 'Decimal' is not defined
data
 
# внимательно читай PartV 555 - модуль обработки чисел с фиксированной точностью не пашет без конструктора  
# нужно применять Дзен - всё простое лучше сложного, конструктор пашет через переменные - остальное фейл.

from decimal import Decimal
data = Decimal("11.404") - Decimal("0.3")                    
print(data)                                                  # 11.104
major = data + Decimal("0.1")
print(major)                                                 # 11.204
anime = Decimal("0.1") + Decimal("0.101") + Decimal("0.10") - Decimal("0.00004")
print(anime)                                                 # 0.30096

import decimal                                               # запуск модуля
decimal.getcontext().prec = 4                                # точности после запятой - (4)
decimal.Decimal(1) / decimal.Decimal (3)                     # возвращает Decimal('0.3333')

import decimal   
decimal.Decimal(1) / decimal.Decimal (7)                     # возвращает 28 знаков после запятой
decimal.getcontext().prec = 14  
decimal.Decimal(1) / decimal.Decimal (7)                     # возвращает 14 знаков после запятой

import decimal    
decimal.Decimal.from_float(1.25)                             # создать объект класса decimal из float
# читается как - в модуле decimal соглсано конструктору модуля Decimal создать объект из числа с точкой.

1999 / 1.33                                                  # разделить 1999 рублей на рубль 33 копейки 
import decimal                                               # запускаем модуль 
decimal.getcontext().prec = 5                                # ставим точность (5 знаков в результате)
pay = str(decimal.Decimal(1999) / decimal.Decimal (1.33))    # преобразуем результат в строку
pay                                                          # возвращает  '2000.330000'
 
import decimal
decimal.Decimal("1.0") / decimal.Decimal("3.01")             # Decimal('0.3322259136212624584717607973')
with decimal.localcontext() as anime:                        # Лутцу надо было сразу с with начинать.
    anime.prec = 2                                           # задаём точность, возвращает Decimal('0.33')
    decimal.Decimal("1.0") / decimal.Decimal("3.01")
decimal.Decimal("1.0") / decimal.Decimal("3.01")             # Decimal('0.3322259136212624584717607973')


print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal
Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")


x =  0.1 + 0.1 + 0.1 - 0.3                                   # Питон думает что это какая то хуета.
x                                                            # 5.551115123125783e-17
int(x)                                                       # 0
float(x)                                                     # 5.551115123125783e-17

from decimal import Decimal
x = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
x                                                            # Decimal('0.0')

from fractions import Fraction
x = Fraction(1, 3)                                           # числитель 1 - знаменатель 3
y = Fraction(4 , 6)                                          # Будет упрощено до 2, 3 с помощью функции gcd
x                                                            # Fraction(1, 3)
y                                                            # Fraction(2, 3)
print(y)                                                     # 2/3
x + y                                                        # Fraction(1, 1)
x - y                                                        # Fraction(-1, 3)
x / y                                                        # Fraction(1, 2)

from fractions import Fraction
Fraction(".25")                                              # 0.25 = 1\4
Fraction("1.25")                                             # 1.25 = 5 частей из 1 \ 4
Fraction(".25") + Fraction("1.25")                           # Fraction(3, 2)

# следовательно

from fractions import Fraction       # рациональные числа - числитель и знаменатель
data = Fraction(2,3)                 # 2 числитель - 3 знаменатель
data + 2                             # data + x = 2 + 3 * x
data                                 # возвращает Fraction(8, 3) 2 знаменателя = 6 ( 1 = 3, 3 = 9 и т.д)
data + Fraction(1,1)                 # возвращает Fraction(5, 3)  (!моя не понимает это!)

# data + Fraction(1,1) следует читать как (2,3) + (1,1) где (1,1) это = 1 / 1 что соотвествует выражению
# data + 1 которое в этом контексте равнозначно data + x = 2 + 3 * x  где х = 1 - что даёт результат (5.3)

a = 1 / 3.0
b = 4 / 6.0
a                                    # 0.3333333333333333
b                                    # 0.6666666666666666
a + b                                # 1.0
b - a                                # 0.3333333333333333
a * b                                # 0.2222222222222222
from decimal import Decimal          #
a = Decimal("1.0") / Decimal("3.0")  #
a                                    # Decimal('0.3333333333333333333333333333')
b = Decimal("4.0") / Decimal("6.0")  #
b                                    # Decimal('0.6666666666666666666666666667')
c = a + b                            #
c                                    # Decimal('1.000000000000000000000000000')
x = b - a                            #
x                                    # Decimal('0.3333333333333333333333333334')
y = a * b                            #
y                                    # Decimal('0.2222222222222222222222222222')

# я смог в эту херь - во истину Явное лучше неявного а простое лучше сложного!
# достаточно один раз описать объекты класса decimal в коде через переменные. 

a = 1 / 3.0
b = 4 / 6.0
a                                    # 0.3333333333333333
b                                    # 0.6666666666666666
a + b                                # 1.0
b - a                                # 0.3333333333333333
a * b                                # 0.2222222222222222
from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
x + y                               # Fraction(1, 1)
x - y                               # Fraction(-1, 3)
x * y                               # Fraction(2, 9)

0.1 + 0.1 + 0.1 - 0.3               # должен быть получен 0 - близко, но не точно
from decimal import Decimal
x = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
x
from fractions import Fraction
x = Fraction(1,10) + Fraction(1,10) + Fraction(1,10) - Fraction(3,10)
x 

1 / 3                               # 0.3333333333333333
from fractions import Fraction
Fraction(1,3)
import decimal
decimal.getcontext().prec = 2
decimal.Decimal(1) / decimal.Decimal(3)

(1 / 3) + (6 / 12)                  # 0.8333333333333333
from fractions import Fraction
Fraction(6,12)                      # упрощает автоматически до Fraction(1, 2)
Fraction(1,3) + Fraction(6,12)    # Fraction(5, 6)
import decimal
x = decimal.Decimal(str(1/3)) + decimal.Decimal(str(6/12))
x                                   # Decimal('0.8333333333333333')

1000.0 / 1234567890                 # 8.100000073710001e-07
from fractions import Fraction
Fraction(1000, 1234567890)          # Fraction(100, 123456789)

(2.5).as_integer_ratio()            # метод объекта типа float, возвращает (5, 2)  - тоже самое что и 2,5
f = 2.5                             # задаём переменную f для инструкции преобразования ниже
from fractions import Fraction      
z = Fraction(*f.as_integer_ratio()) # преобразование float > fraction
z                                   # Fraction(5, 2)
x = Fraction(1,3)
x + z                               # Fraction(17, 6)
float(x)                            # 0.3333333333333333
float(z)                            # 2.5
float(x + z)                        # 2.8333333333333335
17 / 6                              # 2.8333333333333335


from fractions import Fraction      # альетрнативный метод преобразования float>fraction без операнда
Fraction.from_float(1.75)           # Fraction(7, 4)
Fraction(*(1.75).as_integer_ratio())# Fraction(7, 4)

from fractions import Fraction 
x = Fraction(1,3)
x + 2                               # Fraction + int -> Fraction == Fraction(7, 3)
x + 2.0                             # Fraction + float -> float == 2.3333333333333335
x + (1./3)                          # Fraction + float -> float == 0.6666666666666666
x + (4./3)                          # Fraction + float -> float == 1.6666666666666665
x + Fraction(4,3)                   # # Fraction + Fraction -> Fraction == Fraction(5, 3)

4.0 / 3                             # возвращает 1.3333333333333333
(4.0 / 3).as_integer_ratio()        # потеря точности, возвращает (6004799503160661, 4503599627370496)
from fractions import Fraction 
x = Fraction(1,3)
y = x + Fraction(*(4.0 / 3).as_integer_ratio())
y                                   # Fraction(22517998136852479, 13510798882111488)
y.limit_denominator(10)             # x.limit_denominator(10) - упростить х до ближайщего рац.числа. 
b = 22517998136852479 / 13510798882111488
b                                   # возвращает 5.3 или близкое к нему 1.6666666666666665
5.0 / 3                             # нихуя себе потеря точности, 5 вместо 4, возвращает 1.6666666666666667

set([1,2,3,4,5])                    # задать множество
set("spam")                         # помимо цифр - можно использовать буквы
x = set("Ghost int he shell [11,501] Stand Alone Complex")  # также возможен полный хаос и ересь Хоруса
x
type(x)                             #  <class 'set'>

x = set("abcde")
y = set("bdxyz")
x                                   # {'c', 'e', 'a', 'd', 'b'}
y                                   # {'z', 'y', 'd', 'x', 'b'}
"e" in x                            # проверка вхождения в множесто, возвращает True
"e" in y                            # проверка вхождения в множесто, возвращает False
x - y                               # разница множеств - возвращает {'a', 'e', 'c'}
x | y                               # объединение множеств {'y', 'c', 'd', 'b', 'x', 'a', 'e', 'z'}
x & y                               # пересечение множеств, возвращает {'b', 'd'} 
x ^ y                               # симметрическая разность, возвращает {'y', 'z', 'x', 'e', 'a', 'c'}
x > y                               # надмножество, возвращает False
x < y                               # подмножество, возвращает False
z = x.intersection(y)               # То же, что и выражение x & y
z                                   # возвращает {'d', 'b'}
b = x & y                           # всё явное - лучше не явного
b                                   # всё простое - лучше сложного
z.add("Ghost in the shell")         # добавить один элемент в множество
z                                   # {'b', 'Ghost in the shell', 'd'}
z.update(set("bx"))                 # объединение множеств
z                                   # {'x', 'd', 'b', 'Ghost in the shell'}
z.update(set(['X', 'Y']))
z                                   # {'X', 'Ghost in the shell', 'x', 'd', 'b', 'Y'}
z.update(set(['x', 'y']))
z                                   # {'X', 'Ghost in the shell', 'x', 'd', 'b', 'Y', 'y'}
z.remove("d")                       # удалить один элемент
z                                   # {'x', 'Ghost in the shell', 'b', 'y', 'Y', 'X'}
for item in z: print(item*3)        # возаращает шикарный результат
for item in x: print(item, "+1")
len(z)                              # 6


anime = set([1,2,3])
anime | set([3,4])                  # возвращает {1, 2, 3, 4}
anime | [11,501]                    # исключение  unsupported operand type(s) for |: 'set' and 'list'

anime = set([1,2,3])
anime | set([3,4])
anime.union([11,501])              # возвращает  {11, 1, 2, 3, 501}
anime.union({"Ghost":"Shell"})     # возвращает  {'Ghost', 1, 2, 3}
type(anime)                        # <class 'set'>
print(anime)
anime.intersection([1,100])        # возвращает {1}  (возвращает все элементы во всех множества в качестве нового множества)
anime                              # возвращает {1, 2, 3}
anime.issubset(range(-5,5))        # возвращает True (сообщает входит ли множество в заданное в () множество)

# ползеная инфа; прогресс в версиях языка - ближе к 3хх они пришли в логике множеств как словарей.
                  
set([1,2,3,4,5])                   # {1, 2, 3, 4, 5}
{1,2,3,4,5}                        # {1, 2, 3, 4, 5}

anime = {"g","h","o","s","t"}      # фича версии 3.0++
anime                              # возвращает {'g', 'o', 't', 's', 'h'} 

anime = set("ghost")               # старое, доброе, ечное от 2.6
anime                              # {'o', 'h', 't', 's', 'g'}

# через set имхо удобнее

anime = set("ghost")   
anime.add("in the shell")
anime                              # {'g', 't', 'o', 'in the shell', 'h', 's'}
anime.remove("in the shell")
anime
ghost = set("in the shell")
anime.union(ghost)                 # {'t', 'e', ' ', 'l', 'i', 'n', 'o', 'g', 's', 'h'}

S1 = {1,2,3,4}
S1 & {1,3}                         # объединение {1, 3}
{11,501} | S1                      # пересечение {1, 2, 3, 4, 501, 11}
S1                                 # возвращает  {1, 2, 3, 4} - ведь множества неизменяемы (наверху новое)
S1 - {1,3,4}                       # разность {2}
S1 > {1,3}                         # надмножество, возвращает True
S1 - {1,2,3,4}                     # set()

S = set()
type(S)
type({})                           # <class 'dict'>
S.add(1)
S                                  # {1}

{1, 2, 3} | {3, 4}                 # {1, 2, 3, 4}
{1, 2, 3} | [3, 4]                 # вернёт исключение - разный тип объектов, используй фукнции множеств
{1, 2, 3}.union([3, 4])            # {1, 2, 3, 4}
{1, 2, 3}.union({3, 4})            # {1, 2, 3, 4}
{1, 2, 3}.union(set([3, 4]))       # {1, 2, 3, 4}
{1, 2, 3}.intersection((1, 3, 5))  # {1, 3}
{1, 2, 3}.issubset(range(-5, 5))   # True

anime = set(1.23)                  # вернёт исключение - использую встроенные фукнции множеств для этого

anime = set()
anime.add(1.23)
anime                              # {1.23}
anime.add([1,2,3,])                # вернёт исключение - unhashable type: 'list' (объекты разных классов)
anime.add({"a":1})                 # вернёт исключение - unhashable type: 'dict' (объекты разных классов)
anime.union({"a":1})               # можно обойти через union - вернёт {1.23, 'a'}

# Python не может добавить во множество anime объект типы список - потому что список это изменяемый объект.

anime = set()
anime.add(1.23)
anime.add((1,2,3,))
anime                              # с кортежами проблем нет - возвращает  {1.23, (1, 2, 3)}
anime | {(4, 5, 6), (1, 2, 3)}     # то же, что и S.union(...) , возвращает {1.23, (4, 5, 6), (1, 2, 3)}
(1,2,3) in anime                   # Членство: выявляется по полным значениям , возвращает True
(1,4,3) in anime                   # Членство: выявляется по полным значениям , возвращает False

anime = set("Ghost in the shell")
ghost = frozenset("Stand Alone Complex")
anime.update(ghost)
anime                             # {' ', 'S', 's', 'l', 'o', 't', 'x', 'A', 'e', 'h', 'p', 'C', 'G', 'd', 'm', 'a', 'i', 'n'}

anime = set("Ghost in the shell")
ghost = frozenset("Stand Alone Complex")
anime.union(ghost)                # {'e', 'G', 'S', 'o', 'n', 's', 'x', 'm', ' ', 'l', 'i', 'd', 'A', 'p', 't', 'C', 'h', 'a'}

anime = set("Ghost in the shell")
ghost = frozenset("Stand Alone Complex")
anime.add(ghost)                 
anime                             # {'l', 'h', 'i', frozenset({'l', 'o', 'C', 'a', 'p', 't', 'm', ' ', 'd', 'x', 'A', 'S', 'n', 'e'}), 'o', 't', ' ', 's', 'G', 'n', 'e'}

anime = set("Ghost in the shell")
ghost = frozenset("Stand Alone Complex")
shell = anime & ghost           
shell                            # {' ', 'e', 'o', 'n', 't', 'l'}

{x ** 2 for x in[1,2,3,4]}       # генератор множеств - возвращает {16, 1, 4, 9}

{anime ** 3 for anime in[11,404,501]}  # возвращает {65939264, 1331, 125751501}

{x for x in "spam"}              #  тоже что и set("spam") - возвращает {'s', 'm', 'p', 'a'}
{x for x in "Ghost"}             #  тоже что и set("Ghost") - возвращает {'s', 't', 'o', 'h', 'G'}

{c * 4 for c in "spam"}          # - возвращает {'pppp', 'mmmm', 'aaaa', 'ssss'}

{anime * 2 for anime in "Ghost in the shell"}   #  возвращает {'ss', 'ee', '  ', 'nn', 'ii', 'll', 'tt', 'GG', 'oo', 'hh'}

anime = {x * 2 for x in "Stand alone complex"}  # генератор множества через переменную для работы с ним
anime | {"Ghost"}               # {'aa', 'll', 'cc', 'oo', '  ', 'ee', 'Ghost', 'xx', 'mm', 'dd', 'nn', 'tt', 'pp', 'SS'}
anime                           # {'aa', 'll', 'cc', 'oo', '  ', 'ee', 'xx', 'mm', 'dd', 'nn', 'tt', 'pp', 'SS'}

anime = {x * 2 for x in "Stand alone complex"}   #  можно использовать if
shell = anime | {"Ghost"}            
anime
shell
if anime == shell:
    print("Yes")
else:
    print("no")
  
anime = {x * 2 for x in "Stand alone complex"}  #  можно использовать while
shell = anime | {"Ghost"}            
anime
shell
i = 0
while i < 10:
    print(anime)
    i = i + 1
    if i == 10:
        print(shell)

# а как умножить x внутри генератора множеста через while  и получить 10 разных множеств - я пока не знаю
 
anime = [1,2,3,4,2,1,5]
set(anime)                       # возвращает множество {1, 2, 3, 4, 5}
anime = list(set(anime))         
anime                            # возвращает список [1, 2, 3, 4, 5]

engineers = {"Alex", "Stan", "Bato", "Ghost"}
managers = {"Alex", "Ghost"}
"Alex" in engineers               # Alex инженер? - True
engineers & managers              # кто одновременно является инженером и менеджером? - {'Alex', 'Ghost'}
engineers | managers              # все сотрудники обеих категорий - {'Alex', 'Ghost', 'Stan', 'Bato'}
engineers - managers              # инженеры не являющиеся менеджерами - {'Stan', 'Bato'}
managers - engineers              # возвращает set() - по Лутцу результат другой см.страницу 189
engineers > managers              # возвращает True - по Лутцу результат другой см.страницу 189
{"Alex", "Ghost"} < engineers     # оба сотрудника инженеры? (используем подмножество) - True
(managers | engineers) > managers # множество всех сотрудников является надмножеством менеджеров? - True
managers ^ engineers              # сотрудники принадлежащие к одной категории - {'Bato', 'Stan'}
(managers | engineers) - (managers ^ engineers)  # пересечение -  {'Alex', 'Ghost'}

# спустя 3 часа и одного старшего брата который испортил мне настроение - я поняшл что знаю и могу в цикл
# если черех параметр (y) программа возвращает {'eeee', 'cccc', 'aaaa', 'mmmm', 'tttt', 'dddd', '    ', 'pppp', 'xxxx', 'SSSS', 'nnnn', 'oooo', 'llll'}:

y = 2
anime = {(x * 2) * y for x in "Stand alone complex"}
anime               

# то реализация цикла while внутри генератора множеств с использованием параметра должна выглядеть вот так:

i = 0
while i < 10:
    i = i + 1
    anime = {(x * 2) * i for x in "Stand alone complex"}
    print(anime)

# возвращает 10 множеств возрастающей длинны, параметр (i) работает как часы увеличивая (х) на шаг (+1)

type(True)               #  <class 'bool'> - True == 1
isinstance(True, int)    #  True
True == 1                #  True
False == 0               #  True
True is 1                #  False - это разные объекты
True or False            #  True - тоже самое что 1 or 0 
1 or 0                   #  возвращает 1
True + 4                 #  возвращает 5 - потому что "гибкость" = консоль решила что так надо.

import math
math.sqrt(3)             #  1.7320508075688772
pow(11,2)                #  121



















 







