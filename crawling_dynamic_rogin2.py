
from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver')

link = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
driver.get(link)

time.sleep(2)

myid = 'rlaek4793'
mypw = 'cutyjw5110'

driver.execute_script("document.getElementsByName('id')[0].value = \'" + myid + "\'")
driver.execute_script("document.getElementsByName('id')[0].value = \'" + mypw + "\'")
time.sleep(1)

driver.find_element_by_id('log.login').click()
time.sleep(1)

comu = 'https://cafe.naver.com/codeuniv' 
driver.get(comu)
time.sleep(1)

driver.find_element_by_id('menuLink90').click()
time.sleep(1)

driver.switch_to_frame('cafe_main')
time.sleep(1)
art = driver.find_elements_by_css_selector('#main-area > div:nth-child(6) div.board-list')

count = 0 
k = 2

#게시글 누르기

for arti in art:
    if count == 20:
        break
    elif count/15 == 1:
        k +=1
        driver.find_element_by_css_selector('#main-area > div.prev-next > a:nth-child(' + str(k) + ')'.click()
    
    title = arti.text
    arti.click()
    time.sleep(1)
    content = driver.find_element_by_xpath('//*[@id="SE-157802fa-8718-4b10-9ebb-75b12409ed8c"]').text
    count +=1
    print(f' < {count} 번 문서 > - {title}')
    print(content, end = ' ')
    print('\n')
    driver.back()
        

driver.close()
