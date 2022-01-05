# 생성자 : 인스턴스 생성, 필드값 초기화 함수
# 기본생성자 : 생성자에 self만 있고, 다른 매개변수가 없음
# class 클래스명:
#     def __init__(self):   # 인수 x
#         self.top = []


# 디폴트
# 기본값 인수는 제일 뒤에
# 문자열이 먼저.
class Car:
    def __init__(self, color = 'red', speed = 0):
        self.color = color
        self.speed = speed