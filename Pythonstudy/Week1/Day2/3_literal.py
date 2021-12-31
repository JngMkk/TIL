# 상수
# 값이 변하지 않음
pi = 3.141592

# 원의 둘레와 면적 계산
radius = 10
area = radius * radius * pi
print(area)

# 이자 계산
RATE = 0.03
deposit = 100000
interest = deposit * RATE
balance = deposit + interest
print(int(balance))
print(format(int(balance), ','))

# 정수 리터럴
# 0b로 시작하면 2진수
# 0o로 시작하면 8진수
# 0x로 시작하면 16진수
# (10진수) 123 = 1*10^2 + 2*10^1 + 3*10^0
# (2진수) 1010 = 1*2^3 + 1*2^1
# (16진수) 93 = 9*16^1 + 3*16^0
# (8진수) 223 = 2*8^2 + 2*8^1 + 3*8^0
# 10진수 진수 변환 : bin(), oct(), hex()
a = 49
b = 0b110001
c = 0o61
d = 0x1f2c  # 0b0001111100101100
e = 0x31
print(a, b, c, d, e)

print('2진수 변환 : bin()')
print(bin(11))
print(bin(0o03))
print(bin(0xff))
print('8진수 변환 : oct()')
print(oct(11))
print(oct(0b11011))
print(oct(0xff))
print('16진수 변환 : hex()')
print(hex(0b10101))
print(hex(0x3d))

print(int('1010', 2))
print(int('1010', 8))
print(int('1010', 10))
print(int('1010', 16))

# 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 1.234e5
f4 = 1.234e-5
print(f1, f2, f3, f4)