class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Vinicius")
print(Person.number_of_people)
p2 = Person("rafael")
print(Person.number_of_people)