class Dog:
    def __init__(self, breed, size, color, age = 0):
        self.__breed = breed
        self.size = size
        self.color = color
        self.age = age
    
    def getBreed(self):
        return self.__breed
    def setBreed(self, breed):
        self.__breed = breed
    def getSize(self):
        return self.size
    def setSize(self, size):
        self.size = size
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color
    def getAge(self):
        return self.age
    def setAge(self, age):
        self.age = age
    def eat(self):
        print('Eat!')
    def sleep(self):
        print('zzZ')
    def sit(self):
        print('Sit!')
    def run(self):
        print('Run!')
    def getInfo(self):
        return 'Breed : %s, Size : %s, Color : %s, Age : %2d' % (self.__breed, self.size, self.color, self.age)