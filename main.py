class Student:
    # Атрибуты уровня класса
    group = "C2016"
    counter = 0

    # дандро методы или волшебные методы
    def __init__(self, age, height, name=None):
        # Атрибуты уровня объекта
        self.name = name
        self.age = age
        self.height = height
        Student.counter += 1
        print("Объект был создан")
    def grow(self, height=1):
        self.height += height

    def __str__(self):
        return f"I'm name {self.name}. My age is {self.age}"
    def __del__(self):
        print("Удален объект")

print(Student.group)

nick = Student(16, 165, 'Nick')
print(nick)
# print(nick.age)
# print(nick.height)
# print(nick.name)
# print(nick.group)
# kate = Student(17, 175, "Ekaterina")
# print(kate.age)
# print(kate.height)
# print(kate.name)
# print(kate.group)
# print(Student.counter)
# elena = Student(18, 155, "Elena")
# print(Student.counter)
# print("Height Nick", nick.height)
# nick.grow(25)
# print("Height Nick", nick.height)
# kate.grow(30)