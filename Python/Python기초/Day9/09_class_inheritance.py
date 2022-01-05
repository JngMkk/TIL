class Car:
    def __init__(self, speed, color):
        self.speed = speed
        self.color = color
    def drive(self):
        print(f'{self.speed}로 주행합니다.')

class Truck(Car):
    def __init__(self, speed, color, load):
        super().__init__(speed, color)
        self.load = load
    def drive(self):
        print(f'{self.speed}로 {self.load} 주행합니다.')
    def loading(self):
        print(f'{self.load} ? ? ? ')

truck1 = Truck(10, 'Blue', 1000)
truck1.drive()

class Vehicle(Car):
    def __init__(self, speed, color, seat):
        super().__init__(speed, color)
        self.seat = seat
    
    # 메소드 재정의 (오버라이딩)
    def drive(self):
        print(f'{self.speed}로 {self.seat}인의 사람이 타고 주행합니다.')

