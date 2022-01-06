# 생성자 : 인스턴스 생성, 필드값 초기화 함수
# 기본생성자 : 생성자에 self만 있고, 다른 매개변수가 없음
# class 클래스명:
#     def __init__(self):   # 인수 x
#         self.top = []

class Dog:
    # # init을 선언하지 않고 생성 가능 -> 나중에 선언
    # breed = ''
    # size = ''
    # age = 0
    # color = ''

    # _ : 변수에 특별한 이름을 부여하지 않고 사용하려 할 때
    # __ : 특수한 예약함수, 변수에 사용
    def __init__(self, breed, size, age, color):    # self : 클래스에서 생성된 인스턴스에 접근(인스턴스 자신)
        self.breed = breed
        self.size = size
        self.age = age
        self.color = color
    
    def Eat(self):
        pass
    def Sleep(self):
        pass
    def Sit(self):
        pass
    def Run(self):
        pass
    def __str__(self):
        return 'Breed : %s, Size : %s, Age : %2d, Color : %s' % (self.breed, self.size, self.age, self.color)

dog1 = Dog('Neapolitan Mastiff', 'Lage', 5, 'Black')
dog2 = Dog('Maltese', 'Small', 2, 'White')
dog3 = Dog('Chow Chow', 'Medium', 3, 'Brown')