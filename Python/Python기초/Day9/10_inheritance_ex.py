class Animal:
    def __init__(self, age, leg, color, breed):
        self.age = age
        self.leg = leg
        self.color = color
        self.breed = breed

    def talk(self):
        return 'Hi!'
    def eat(self):
        return 'Eat!'
    def sleep(self):
        return 'zzZ'
    def __str__(self):
        return 'Age : %2d, Leg : %d, Color : %s, Breed : %s' % (self.age, self.leg, self.color, self.breed)

# 상속
class Dog(Animal):
    def talk(self):
        return 'Bark!'

# 상속
class Cat(Animal):
    def talk(self):
        return 'Meow~'

# 다형성(polymorphism) : 같은 이름의 메서드가 다른 기능을 할 수 있도록 한 것
animals = [Cat(1, 4, 'White', 'A'), Cat(3, 4, 'Black', 'B'), Dog(6, 4, 'Orange', 'AA')]

for animal in animals:
    print(animal.talk())