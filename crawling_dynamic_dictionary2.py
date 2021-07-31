import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver') 
papago_url = 'https://papago.naver.com/'
driver.get(papago_url)
time.sleep(3)
mydic = {}

def get_papago_result():
        question = input('번역할 영단어 입력: ')
        driver.find_element_by_css_selector('textarea#txtSource').send_keys(question)
        driver.find_element_by_css_selector('button#btnTranslate').click() #인터페이스 넘어가는 시간 기다리기
        time.sleep(1)
        output = driver.find_element_by_css_selector('div#txtTarget').text #이 칸에 나타나는 text를 원하므로..
        mydic[question] = output
        driver.find_element_by_css_selector('textarea#txtSource').clear()
        return mydic

for i in range(5):
    get_papago_result()        
print(mydic)
driver.close()




'''
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

'''
