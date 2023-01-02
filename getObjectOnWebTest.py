import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=IThome&oq=IThome'
resp = requests.get(url)
print(resp.text)
# soup = BeautifulSoup(resp.text, 'html5lib')

# link = soup.find('a', class_='qa-list__title-link')
# print(link['href'].strip())