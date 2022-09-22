class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old')

    def speak(self):
        print("I don't know what i say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print('Meow')

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old and i am {self.color}')

class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


v = Pet('Corujinha', 5)
v.show()
v.speak()
c = Cat("Bill", 34, "black")
c.show()
c.speak()
c = Dog('Vinicius', 28)
c.show()
c.speak()
c = Fish("Nemo", 7)
c.show()
c.speak()