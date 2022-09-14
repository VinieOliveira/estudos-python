
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d = Dog ("Vinie", 4)
d.set_age(3)
print(d.get_name(), d.get_age())
d2 = Dog('Bill', 5)
print(d2.get_name(), d2.get_age())
