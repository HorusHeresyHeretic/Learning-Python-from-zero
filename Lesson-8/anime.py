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
import os
os.path.abspath("anime.py")            # возвращает нормализованный абсолютный путь.

# смотри мега ссылку про пути https://pythonworld.ru/moduli/modul-os-path.html   http://itnote.ru/2011/05/25/python-file/





