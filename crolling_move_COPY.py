from selenium import webdriver
import time

keyword = input('뉴스 검색 키워드 : ')

driver = webdriver.Chrome('./chromedriver')
news_url = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&mediaid_clust=HKPAPER,HKCOM'
driver.get(news_url)
time.sleep(2)

ten_articles = driver.find_elements_by_css_selector('em.tit')

# 단순히 뉴스마다 번호를 붙여주기 위한 변수
count = 0

# 10개 뉴스 기사를 대상으로 반복문 실행
for article in ten_articles:

		# 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, text는 제목을 나타냄
    title = article.text

		# 'article'은 뉴스 기사 제목을 나타내는 HTML 요소이므로, 클릭하면 뉴스 기사 본문을 확인할 수 있음
    article.click()
		# 시간적 여유 원하는 만큼
    time.sleep(1)

		# 'driver'를 새로운 탭 (뉴스 기사 본문)으로 전환
    driver.switch_to.window(driver.window_handles[-1])

		# 기사 본문을 'content' 변수에 저장
    content = driver.find_element_by_id('articletxt').text

		# 기사 본문 출력
    count += 1
    print(f'< {count}번 뉴스 - {title} >')
    print(content)

		# 새로운 탭 (뉴스 기사 본문)에서 작업을 다 했으므로, 새로운 탭은 닫아줌
    driver.close()

		# 다시 'driver'를 맨 처음 탭으로 전환
    driver.switch_to_window(driver.window_handles[0])

		# 시간적 여유 원하는 만큼
    time.sleep(1)

# 크롬 창 닫기
driver.close()