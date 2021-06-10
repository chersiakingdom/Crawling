# 필요한 라이브러리 가져오기
import requests
from bs4 import BeautifulSoup

#url을 link에 저장, get 함수로 text파일 가져와서 BeautifulSoup이용해 html문서로 저장
link = 'https://dhlottery.co.kr/gameResult.do?method=byWin'
raw = requests.get(link)
soup = BeautifulSoup(raw.text, 'html.parser')

# 큰 박스를 추출하고, 그 안의 원하는 요소를 모두 추출함
box = soup.find('div',{'class':'nums'})
num = box.find_all('span')

#num 에 저장된걸 하나씩 정리하여 출력하고, 문장 중 text 형태인것만 출력
for number in num:
    print(number.text)

   