# 변수 => 메모리 내의 기억 장소
# id() : 메모리 주소 반환
# 1) 레퍼런스 : 값이 저장된 위치 참조
# 2) 변수 선언이 필요 없음 ex) java -> int x
# 3) 동적 타이핑
# 4) 이름이 있다
# 5) 객체가 저장된 주소값이 저장
# 6) 값 변경 가능

# 화씨 온도를 섭씨 온도로 변환
fTemp = 90
cTemp = (fTemp - 32) * 5 / 9
print('%.2f' % cTemp)
print(format(cTemp, '.2f'))

# 온도 변환 혼자 만들어 봄
class ChangeTemp:
    def __init__(self):
        self.temp = 0
    def FtoC(self, Ftemp):
        self.temp = self.temp + Ftemp
        Ctemp = (Ftemp - 32) * 5 / 9
        print('화씨(%.2f) -> 섭씨(%.2f)' % (Ftemp, Ctemp))
    def CtoF(self, Ctemp):
        self.temp = self.temp + Ctemp
        Ftemp = 9 / 5 * Ctemp + 32
        print('섭씨(%.2f) -> 화씨(%.2f)' % (Ctemp, Ftemp))
        
temp = ChangeTemp()
temp.FtoC(90)
temp.CtoF(32)

print('name : {} , phone : {}'.format('중모', '010-2134-4578'))
print('name : {1} , phone : {0}'.format('010-2134-4578', '중모'))
print('{0:d}, {1:d}'.format(100, 123))
print('{1:d}, {0:d}'.format(100, 123))
print('{0:d}, {1:5d}'.format(100, 123))
print('%d %5d %10d' % (123, 123, 123))

