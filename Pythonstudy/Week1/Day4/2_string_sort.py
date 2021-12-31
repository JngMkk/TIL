# 문자열 정렬 : 정렬 문자 <, >, ^
# 문자 : 왼쪽 정렬, 숫자 : 오른쪽 정렬
# < : 왼쪽 정렬, > : 오른쪽 정렬,, ^ : 가운데 정렬
s = 'python'
print(s)
print('{:<20}'.format(s))
print('{:>20}'.format(s))
print('{:^20}'.format(s))
print('{:-^20}'.format(s))
print('{:-<20}'.format(s))
print('{:->20}'.format(s))
n = 1234
print(n)
print('{:10d}'.format(n))
print('{:010d}'.format(n))

# ljust(), rjust(), center()
print(s.ljust(20))
print(s.rjust(20))
print(s.center(20))