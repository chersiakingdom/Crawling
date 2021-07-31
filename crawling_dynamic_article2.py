# 하나의 탭에서 화면전환X 새로운 탭이 생길때는 소스코드 작성 필요
'''
driver.window_handles : 열린 탭 목록
len(driver.window_handles) : 열린 탭 갯수
driver.window_handles[0] : 첫번째 탭 (기존에 켜져있던탭)
driver.window_handles[1] : 두번째 탭 (새로켜진탭)
driver.window_handles[2] : 세번째탭
driver.window_handles[-1] : 새로켜진탭(마지막에 열린 탭)

driver 변수가 나타내는 것은 기존의 [0] 번째탭임!
새로켜진 [1]번째에서 작업하고자 하려면 새로켜진탭으로 변경 필수

'''
# 1. 새로운탭 켜짐
# 2. driver 변수 새로운 탭으로 전환
# 3. 새로운 탭에서 작업, 새로운 탭 닫음
# 4. 다시 처음 탭으로 전환

from selenium import webdriver
import time

keyword = input('키워드를 입력하세요 : ')

driver = webdriver.Chrome('./chromedriver')
link = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword  + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(link)
time.sleep(2)

arti = driver.find_elements_by_css_selector('em.tit')

count = 0

for ar in arti:
    title = ar.text
    ar.click()
    time.sleep(1)
 # driver.switch_to.window() 랑 무슨 차이야?
    driver.switch_to.window(driver.window_handles[-1])
    
    content = driver.find_element_by_id('articletxt').text
    # 기사 내용을 줄 단위로 분리해서 저장
    sep = content.split('\n')

    count +=1
    print(f'<{count}번 뉴스 - {title}>')

    for sepa in sep:
        if sepa != '':
            # 아무것도 없는 공백 포함될거 제외, sep 사이마다 공백 한칸 삽입 출력
            print(sepa, end = ' ')
    
    print('\n')

    driver.close()

    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)

driver.close()
