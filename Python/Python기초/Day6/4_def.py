# 사각형 넓이 반환
def getArea(width, height):
    return width * height

# 입력 받아
def getArea_2():
    width = int(input('가로 : '))
    height = int(input('세로 : '))
    result = width * height
    print(f'사각형 넓이 : {result}')
    return result

# 입력 받아 주문액 계산
def order():
    p = int(input('상품가격 입력 : '))
    q = int(input('주문 수량 입력 : '))
    print('---------------------')
    print(f'상품가격 : {p}원\n주문수량 : {q}개\n주문액 : {p * q}원')
    return p * q
