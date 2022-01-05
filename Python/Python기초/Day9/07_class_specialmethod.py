# 특별한 메서드
# __메서드이름__() : 미리 정의되어 있는 메서드

"""

__ge__ : >=

__gt__ : >

__lt__ : <

__le__ : <=

__ne__ : !-

__eq__ : ==

__init__ : 생성자

__repr__ : 인스턴스 print()문으로 출력

__add__ : +

__del__ : 소멸자, 인스턴스를 삭제

"""

class Line:
    def __init__(self, length = 0):
        self.length = length
    
    def __add__(self, other) -> int:
        return self.length + other.length
    def __gt__(self, other) -> bool:
        return self.length > other.length
    def __lt__(self, other) -> bool:
        return self.length < other.length
    def __le__(self, other) -> bool:
        return self.length <= other.length
    def __eq__(self, other) -> bool:
        return self.length == other.length
    def __ne__(self, other) -> bool:
        return self.length != other.length
    
    def __del__(self):                      # 삭제
        return self.length
    def __repr__(self) -> str:
        return '선의 길이 :' + str(self.length)

class Dog:
    def __init__(self, size, age):
        self.age = age
        if size == 'Small':
            self.size = 1
        elif size == 'Medium':
            self.size = 2
        else:
            self.size = 3
    def __eq__(self, other):
        print(self.size, other.size)
        return self.size == other.size
    def __gt__(self, other):
        print(self.size, other.size)
        return self.size > other.size
    def __lt__(self, other):
        print(self.size, other.size)
        return self.size < other.size
    def __add__(self, ohter):
        return self.age + ohter.age
    def __mul__(self, other):
        return self.age * other.age
    def __sub__(self, other):
        return self.age - other.age
    def __div__(self, other):
        return self.age / other.age
    def __str__(self):
        return self.age