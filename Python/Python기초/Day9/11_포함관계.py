# 상속관계와 포함관계(has-a)

class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('Hi')
    def __repr__(self):
        return self.name

# 상속관계 (is-a)
class Student(Person):
    def study(self):
        print('Study')

# 포함관계(has-a)
class PersonList:
    def __init__(self):
        self.personList = []

    def appendPerson(self, person):
        self.personList.append(person)
    def printInfo(self):
        for p in self.personList:
            print(p)

personL = PersonList()
nameL = ['Kim', 'Lee', 'Choi']

for i in range(3):
    p = Person(nameL[i])
    # print(p)
    personL.appendPerson(p)

personL.printInfo()