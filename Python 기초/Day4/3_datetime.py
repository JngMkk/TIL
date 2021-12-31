from datetime import date, datetime, timedelta

today = date.today()
yr = today.year
mon = today.month
day = today.day
print(f'연도 : {yr}, 월 : {mon}, 일 : {day}')

current_time = datetime.now().time()    # 시간만
print(current_time)
hr = current_time.hour
min = current_time.minute
sec = current_time.second
microsec = current_time.microsecond

# 날짜 계산
# timedelta()
print(today + timedelta(days = -1))
print(today + timedelta(days = 1))
print(today + timedelta(days = -7))
print(today + timedelta(days = 7))

current = datetime.now()    # 연월일 포함
print(current + timedelta(hours = -1))
print(current + timedelta(days = 1, hours = 2))

# strftime() 함수 : 날짜 형식을 문자열로 변환
# H : 24시간, I : 12시간 (%p 붙혀서 am인지 pm인지)
# m : month
# M : minute
print(today.strftime('%Y-%m-%d %H:%M:%S'))
print(today.strftime('%Y-%m-%d %I:%M:%S %p'))
print(type(today))
print(type(current_time))
print(type(current))

# strptime() 함수 : 문자열을 날짜형식으로 반환
td = '2021-03-05 18:30:44'
trans_td = datetime.strptime(td, '%Y-%m-%d %H:%M:%S')
print(trans_td)
print(type(trans_td))

# datetime.today().weekday()
# 월: 0 ~ 일 : 6
weekday = datetime.today().weekday()
print(weekday)