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
