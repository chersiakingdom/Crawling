''' from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver') # 가상의 크롬창 자동으로 열리게 도와주는 속성값/행동을 변수에 넣음
# ./chrome~ 은 같은 파일 위치에 있는걸 사용한다 이므로 같은파일에 넣어둬야함.

papago_url = 'https://papago.naver.com/'
driver.get(papago_url) # 'url 주소'

time.sleep(3) #크롤링 행동이 무시되지 않게 1초씩 텀 주기
driver.close() #3초 지난 후 크롬이 자동으로 닫힘.

 [1] find_element_by_??() : find()와 같은 역할. HTML 요소 찾는 함수
주로 ??에는 css_selector('태그 및 선택자'), id(), class_name(), 
xpath#요소를 찾기위한 적당한 id나 class 속성 없을경우. 문서의 특정 부분의 위치를 찾을때 사용.
등이 사용됨)
[2] find_elements_by_??() : find_all() 과 같은 역할. s 붙음!
[3] click() : HTML 요소 클릭하는 함수. ex) find_element_by_css_selector('a#writeFormBtn').click()
[4] send_keys() : HTML 요소에 직접 텍스트 입력하는 함수. ex) ~~selector('~').send_keys('파이썬)

#실전! 나만의 번역 사전 만들기.
필요한 요소 :
testarea#txtSource
button#btnTranslate
div#targetEditArea 운 좋게 세 요소 모두 id 요소를 가진다!
'''

import time
from selenium import webdriver

mydic = {}

driver = webdriver.Chrome('./chromedriver') 
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)
while True :
    question = input('번역할 영단어 입력: ')
    driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
    driver.find_element_by_css_selector('button#btnTranslate').click() #인터페이스 넘어가는 시간 기다리기
    time.sleep(1)
    output = driver.find_element_by_css_selector('div#txtTarget').text #이 칸에 나타나는 text를 원하므로..
    
    #번역사전에 저장 및 출력
    mydic[question] = output
    print(mydic)
    #print('번역 결과: ', output) #크롬 창 닫아주는거 잊지 말기!
    #driver.find_element_by_css_selector('#sourceEditArea > button').click()
    #입력칸 초기화
    driver.find_element_by_css_selector('textarea#txtSource').clear()
    if question == "fin":
        print("번역기를 종료합니다.")
        break
        driver.close()



