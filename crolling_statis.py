import requests
from bs4 import BeautifulSoup

keyword = input("뉴스 검색 키워드 : ")
count = 0

#case 1 
for page in range(1,3): #반드시 page를 str로 바꾸어서 +해줘야함
    link = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=' + str(page)
    raw = requests.get(link)
    soup = BeautifulSoup(raw.text, 'html.parser') #raw 가 아니라 raw.text
    box = soup.find_all('div', {'class' : 'txt_wrap'})
    
    for daye in box:
        count +=1
        title = daye.find('em', {'class':'tit'}).text.strip()
        date = daye.find('span', {'class':'date_time'}).text
        print(count, '-', '[', date, ']', title)


#case 2
for page in range(1,3):
    link = 'https://search.hankyung.com/apps.frm/search.news?query=' + keyword + '&page=' + str(page)
    raw = requests.get(link)
    soup = BeautifulSoup(raw.text, 'html.parser') #raw 가 아니라 raw.text'
    box = soup.find('ul', {'class':'article'})
    alltit = box.find_all('em', {'class':'tit'})
    alldate = box.find_all('span', {'class':'date_time'})
    
    for title,date in zip(alltit,alldate):
        count +=1
        t = title.text #.test 붙여주기, alltit가 아니라 title 로 해야됨
        d = date.text
        print(count, '-', '[', d, ']', t.strip()) #()도 해줘여지 #공백제거
    print()

'''
    #원하는 태그 1개 가져오기 <div id = "example"
    # box.find_all('div')
    # box.find_all(id = 'example') or box.find_all( attrs ={'id':'example'})
    # box.find_all('div', {'id':'example'})
    # 원하는 태그 2개 가져오기 <div id = 'example1><span class = 'example2'>
    # box.find_all(['div', 'span']) 태그는 그냥 쓰면 됨.
    # box.find_all(attrs = { 'id':'example1', 'class':'example2'}) #태그 안써줄땐 attrs=
    print('<' + str(page) + '페이지 뉴스 기사 제목>')
'''