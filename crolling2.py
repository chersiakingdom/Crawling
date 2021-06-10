import requests
from bs4 import BeautifulSoup

link = 'https://www.linkareer.com/list/activity'
raw = requests.get(link)
sour = BeautifulSoup(raw.text, "html.parser")
print(sour)