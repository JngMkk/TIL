# 구구단
dan = int(input('구구단 단 입력: '))
for n in range(1, 10):
    print('%2d x %2d = ' % (dan, n), dan * n)

dan = int(input('구구단 단 입력: '))
n = 1
while n < 10:
    print('%2d x %2d = ' % (dan, n), dan * n)
    n += 1

# 클래스
class Car:
    def __init__(self, color, speed = 0):   # 생성자 함수
        self.color = color      # 데이터 멤버 color 정의 및 초기화
        self.speed = speed      # 데이터 멤버 speed 정의 및 초기화
    
    def speedUp(self):
        self.speed += 10
    def speedDown(self):
        self.speed -= 10
    def __eq__(self, carB):     # 비교 연산자
        return self.color == carB.color
    def __str__(self):
        return 'color = %s, speed = %d' % (self.color, self.speed)

# 테스트
car1 = Car('hi', 20)
car2 = Car('bye', 30)
car3 = Car('hi', 70)
print(car1 == car2)
print(car2 == car3)
print(car1 == car3)
print(car2)

# 상속
class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        super().__init__(color, speed)  # 부모(Car)클래스의 생성자 호출
        self.bTurbo = bTurbo
    """ 메소드의 재정의 """
    def setTurbo(self, bTurbo = True):
        self.bTurbo = bTurbo
    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()   # 일반 자동차의 가속 메소드 호출
    def __str__(self):
        if self.bTurbo:
            return '[%s] [speed = %d] 터보모드' % (self.color, self.speed)
        else:
            return '[%s] [speed = %d] 일반모드' % (self.color, self.speed)

# 테스트
s1 = SuperCar('Gold', 0, True)
s2 = SuperCar('White', 0, False)
s2.setTurbo(True)
s1.speedUp()
s2.speedUp()
print(s1)
print(s2)