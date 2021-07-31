
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('./chromedriver') 
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)
'''
f = open('./my_papago.csv', 'w', newline ='')
wtr = csv.writer(f)
wtr.writerow(['영단어', '번역결과'])


while True :
    question = input('번역할 영단어 입력 (fin 입력시 종료): ')
     if question == "fin":
        print("번역기를 종료합니다.")
        break
    
    
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click() #인터페이스 넘어가는 시간 기다리기
    time.sleep(1)
    output = driver.find_element_by_css_selector('div#txtTarget').text #이 칸에 나타나는 text를 원하므로..
    
    #번역사전에 저장 및 출력
    #mydic[question] = output

    #csv파일에 영단어, 번역결과 작성
    wtr.writerow([question, output])

    print('번역 결과: ', output) #크롬 창 닫아주는거 잊지 말기!
    #driver.find_element_by_css_selector('#sourceEditArea > button').click()
    #입력칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()
   
driver.close()
f.close()
'''

f = open('./my_papago.csv', 'r')
rdr = csv.reader(f)
next(rdr) #att 건너뜀

my_dict = {}
#딕셔너리에 기존의 영단어, 번역결과 모두 저장
for row in rdr:
    question = row[0]
    korean = row[1]
    my_dict[question] = korean
f.close()
# r 로 파일 불러와서 내용 정리
# 이제 a 로 파일 안에 넣는거 구현하기
f = open('./my_papago.csv', 'a', newline ='')
wtr = csv.writer(f)

while True :
    question = input('번역할 영단어 입력 (fin 입력시 종료): ')
    if question == "fin":
        print("번역기를 종료합니다.")
        break
    
    if question in my_dict.keys():
        print('이미 번역한 영단어 입니다! 뜻은', my_dict[question], '입니다')
    else:
         driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
         driver.find_element_by_css_selector('button#btnTranslate').click() #인터페이스 넘어가는 시간 기다리기
         time.sleep(1)
         output = driver.find_element_by_css_selector('div#txtTarget').text #이 칸에 나타나는 text를 원하므로.
         
         
         wtr.writerow([question, output])
         print('번역 결과: ', output) #크롬 창 닫아주는거 잊지 말기)
         #행에 추가했으니 이제 딕셔너리에도 추가
         my_dict[question] = output

         driver.find_element_by_css_selector('textarea#txtSource').clear()
    #driver.find_element_by_css_selector('#sourceEditArea > button').click()
    
   
driver.close()
f.close()

#dict 쓸때, dict[question] = 번역값 임. raw 는 question/ [dicname].keys 이라고 쓰면 되고..
#question을 dic 에서 부르고 싶을때는 keys 라고 함.
