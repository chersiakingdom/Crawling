#자동화 소프트웨어 막는 곳에서는 (ex. 네이버 로그인) 자동입력 방지기능이 뜸
# 이 때 execute_script() 함수 사용하면 로그인 할 수 있음.
'''
# 필수 요소, 로그인버튼
id : log.login
#카테고리메뉴버튼
id : menuLink90
#한 게시글의 Xpath
//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a
# 글 내용
div.content.CafeViewer

div
class : se-module.se-module-text
'''

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

link = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(link)

time.sleep(2)

myid = 'id'
mypw = 'pw'

#아이디와 비밀번호 입력, 자바스크립트로 해당 내용을 넘겨주는 함수(우회하여 로그인)
driver.execute_script("document.getElementsByName('id')[0].value = \'" + myid + "\'")
driver.execute_script("document.getElementsByName('id')[0].value = \'" + mypw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

comu = 'https://cafe.naver.com/codeuniv' #그러네 궅이 하나하나 안눌러도 바로 링크타고 가버리면 되네
driver.get(comu)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

'''프레임 전환 : 내가 원하는 정보가 화면에 보이고, HTML 코드에서도 원하는 정보가 나타나지만, 
파이썬으로 찾아보면 없거나 크롤링이 되지않을때. (종종 있음) 네이버카페가 이런 경우임.
이런 경우에는 프레임으로 만들어져있는 부분이 있는지 확인해보아야함.
프레임 : html 안에 또다른 html을 넣어둔 것. 확인은 html 코드를 보면 알 수 있음.
검색창에 iframe 검색해보기. 원하는 정보를 가진 프레임이 선택될때 선택자 확인
'''
#Frame name = cafe_main
#프레임전환

driver.switch_to_frame('cafe_main')
time.sleep(1)
#게시글 클릭
driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)
content = driver.find_element_by_xpath('//*[@id="SE-157802fa-8718-4b10-9ebb-75b12409ed8c"]').text

print(content)

driver.close()




