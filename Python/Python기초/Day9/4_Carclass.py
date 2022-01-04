# Car class
"""

기능(동작)
- 메소드(함수) : speedUp(), speedDown()

속성(상태, 값)
- 변수(필드) : color, speed

"""

# 클래스 정의(선언)
class Car:
    def __init__(self, color):
        self.color = color
        self.speed = 0
    def speedUp(self, num):
        self.speed += num
        return self.speed
    def speedDown(self, num):
        self.speed -= num
        return self.speed

# 객체 생성
car1 = Car('Red')
car2 = Car('Black')

# 객체(인스턴스) 사용
car1.speedUp(50)

# 특정한 클래스의 인스턴스인지 확인 : isinstance(인스턴스명, 클래스명)
print(isinstance(car1, Car))        # True

# 파이썬의 기본 클래스 : int, float, str, bool, list, dict, set, tuple, ...