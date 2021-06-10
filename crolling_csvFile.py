import csv
'''
f = open('./example.csv', 'w', newline = '') #파일 생성해 변수f에 저장
wtr = csv.writer(f) #파일 작성하는 객체변수 생성. w ~ writer
wtr.writerow(['이름', '나이', '언어']) #열 생성

#데이터 생성
aname = ['길동', '철수', '영희']
aage = [10, 20, 30]
alan = ['파이썬', 'C','자바']

#각 행에 데이터 작성
#주의, row 를 한 묶음으로 넣어줘야함!!
for i in range(3):
    name = aname[i]
    age = aage[i]
    lan = alan[i]
    wtr.writerow([name, age, lan])

wtr.writerow(['다예', '23', 'R'])

f.close()


f = open('./example.csv', 'r')

rdr = csv.reader(f) #csv 파일 모든 변수 rdr에 저장, r ~ reader

next(rdr) # 열 제목 필요하지 않을때 하나 건너뛰어줌.

for row in rdr:
    print(row)

f.close()
'''

f = open('./example.csv', 'a', newline ='')
wtr = csv.writer(f)

wtr.writerow(['바둑', 40, '파이썬'])
wtr.writerow(['오목'. 50, 'c'])

f.close()

# Q.그러면 row를 삭제하고 싶거나 row의 일부를 수정하고 싶을땐?



