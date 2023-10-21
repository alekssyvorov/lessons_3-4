import random

x = ' '


class Student:
    def __init__(self, name=None):
        self.name = name
        self.hapiness = 50
        self.grade = 0
        self.day = 0
        self.alive = True

    def std(self):
        print('School time')
        self.grade += 1
        self.hapiness -= 5
        self.day += 1

    def slp(self):
        print('Sleep time')
        self.hapiness += 2
        self.day += 1

    def chl(self):
        print('Chilling time')
        self.hapiness += 5
        self.grade -= 0.6
        self.day += 1

    def check(self):
        if self.hapiness <= 1:
            print(f'{x * 4}Depression')
            print('Game over')
            self.alive = False
        if self.grade >= 5:
            print(f'{x * 4}You gradueted!')
            print('Game over')
            self.alive = False
        if self.grade <= -1:
            print(f'{x * 4}You failed')
            print('Game over')
            self.alive = False

    def fin(self):
        print(f'Hapiness: {self.hapiness}')
        print(f'Grade: {round(self.grade, 2)}')

    def live(self):
        s = f'Day {self.day} of {self.name}'
        print(f'{s:=^40}')
        rndom = random.randint(1, 3)
        if rndom == 1:
            self.std()
        elif rndom == 2:
            self.slp()
        elif rndom == 3:
            self.chl()
        self.fin()
        self.check()


chrc = input('Students name: ')
stud = Student(name=chrc)
for day in range(365):
    if stud.alive == False:
        stud.fin()
        break
    stud.live()
