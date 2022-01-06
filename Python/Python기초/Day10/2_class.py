# 다중상속 : 여러클래스에서 상속 받음
class Person:
  def __init__(self, name, age = 0):
    self.name = name
    self.age = age

  def greeting(self):
    print(f'안녕하세요 {self.name}')
  
class University:
  def __init__(self, major = '', grade = ''):
    self.major = major
    self.grade = grade
  
  def manageScore(self):
    print('학점관리')

class Undergraduate(Person, University):
  def study(self):
    print('공부')