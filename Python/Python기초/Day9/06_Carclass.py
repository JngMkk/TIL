class Car:
    def __init__(self):
        self.speed = 0
    def speedUp(self, num):
        self.speed += num
        return self.speed
    def speedDown(self, num):
        if self.speed > 0:
            self.speed -= num
            if self.speed <= 0:
                self.speed = 0
                print('정지')
