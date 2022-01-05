class Car:
    color = ''
    count = 0               # 클래스 변수 선언
    
    def __init__(self):
        self.speed = 0
        Car.count += 1      # 클래스 변수
        print(f'현재 총{Car.count}대가 생산되었습니다.')

car1 = Car()
car2 = Car()
car1.speed          # 인스턴스 변수 : 필드
car2.speed

print(Car.count)    # 클래스 변수