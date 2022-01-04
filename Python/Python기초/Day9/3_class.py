"""

객체지향 프로그래밍

함수처럼 어던 기능을 함수 코드에 묶어 두는 것이 아니라, 객체에 기능을 정의하는 것
객체라고 하는 코드에 그런 기능을 묶은 하나의 단일 프로그램을 넣어
다른 프로그래머가 재가용할 수 있도록 함

객체 : 함수와 변수를 함께 가지고 있는 단위

컴퓨터 공학의 오래된 프로그래밍 기법 중 하나

파이썬의 기본 클래스 : int, float, str, bool, list, dict, set, tuple, ...

"""

str1 = 'Hello World'    # 문자열 객체
print(str1)
print(str1.split())

# Class : 객체를 만들어 내는 틀(설계도)
# Instance : 클래스로부터 생성된 객체

class Carculator:
    def __init__(self):
        self.result = 0
    def adder(self, num):
        self.result += num
        return self.result

a = Carculator()
print(type(a))
print(a.adder(14))
print(a.adder(50))
