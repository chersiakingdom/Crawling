
# 경로 잘 보기. 진짜 무조건 하나 하면 time.sleep 쓰기. 하...... 진짜..

from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(login_url)

time.sleep(2)

my_id = 'id'
my_pw = 'pw'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_id + "\'")
time.sleep(1)
driver.execute_script("document.getElementsByName('id')[0].value = \'" + my_pw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)



comu = 'https://cafe.naver.com/codeuniv' 
driver.get(comu)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

driver.switch_to.frame('cafe_main')
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-area"]/div[4]/table/tbody/tr[1]/td[1]/div[2]/div/a').click()
time.sleep(1)

count = 0

for i in range(1,21):
    content = driver.find_element_by_css_selector('div.article_viewer').text
    count +=1
    print(f'< {count} 번 문서 >\n')
    print(content, end = ' ')
    print('\n')
    time.sleep(1)
    driver.find_element_by_css_selector('a.BaseButton.btn_next.BaseButton--skinGray.size_default').click()
    time.sleep(1)

    # x path는 위치를 나타내주는거라 위치가 바뀌면 바뀜... 위치가 바껴도 괜찮아야하면 seletor 써야돼



driver.close()
