# Магическое методы __len__ и __abs__


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


class Otrezok:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)

    def __abs__(self):
        return abs(self.x2 - self.x1)
