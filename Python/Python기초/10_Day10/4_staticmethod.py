# 정적메서드
# 인스턴스를 통하지 않고 클래스에서 바로 호출하여 사용
# 메서드에 self를 넣지 않음 (인스턴스 변수, 인스턴스 메서드가 필요없을 때)
# 순수하게 함수로 만들어서 사용할 때
class Calc:
  @staticmethod
  def add(a, b):
    return a + b
  
  @staticmethod
  def mul(a, b):
    return a * b

print(Calc.mul(3, 2))