# 클래스메서드 : 인스턴스를 통하지 않고 메서드를 클래스에서 바로 호출

# @classmethod를 메서드 위에 붙임 : 메서드내에 인수로 cls를 지정

class Person:
    count = 0       # 클래스변수
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def printCount(cls):
        print(f'{cls.count}명이 태어났습니다')

man1 = Person('Kim')
man2 = Person('Lee')
Person.printCount()