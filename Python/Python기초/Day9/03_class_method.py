# 필드 이용 메서드

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
    
    # 필드값 반환 메소드
    def getModel(self):
        return self.model

    # 필드값 지정 메소드
    def setModel(self, model):
        self.model = model
    
    def getSpeed(self):
        return self.speed

    def setSpeed(self, speed):
        self.speed = speed
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

car1 = Car(0, 'black', 'k9')
print(car1.getColor())
car1.setModel('Audi')
print(car1.getModel())
