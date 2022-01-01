# 연습문제 1

partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', '길동', '몽룡'}
print('파티에 참석한 모든 사람\n', partyA | partyB)
print('-----------------------------------')
print('2개의 파티에 모두 참석한 사람\n', partyA & partyB)
print('-----------------------------------')
print('파티 A에만 참석한 사람\n', partyA - partyB)
print('-----------------------------------')
print('파티B에만 참석한 사람\n', partyB - partyA)