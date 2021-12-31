kim = [90, 85, 70]
choi = [88, 92, 72]
kang = [100, 95, 100]
lee = [90, 60, 80]
students = [kim, choi, kang, lee]
stu_name = ['kim', 'choi', 'kang', 'lee']

# 학생별 총점과 평균점수 출력
for i, std in enumerate(students):
    stu_tot = sum(students[i])
    print(f'{stu_name[i]} 총점 : ', stu_tot)
    print(f'{stu_name[i]} 평균점수 : {stu_tot/len(students[0]):.2f}')

majors = ['국어', '영어', '수학']
# 과목별 총점과 평균점수 출력
for i in range(len(majors)):
    tot = 0
    for j in range(len(students)):
        tot += students[j][i]
    print(f'{majors[i]} 총점 : {tot}, 평균 점수 : {tot/len(students):.2f}')
