import requests
from bs4 import BeautifulSoup

url = 'https://ithelp.ithome.com.tw/users/20134430/ironman/4307'
#發送 GET 請求到 url，並將回應物件放到 resp
resp = requests.get(url)
# 將 resp.text 也就是 HTML 資料定義到 BeautifulSoup 物件內，並用 html5lib 解析 HTML 內容
soup = BeautifulSoup(resp.text, 'html5lib')

# 輸出網頁的 title
print(soup.title.getText())

#輸出第一個尋找到的 <li> 元素的文字
print(soup.li.getText())

#輸出第一個尋找到的 <li> 元素的文字(相同效果)
print(soup.find('li').getText())

#尋找全部 <li> 元素的文字
lis = soup.find_all('li')
for li in lis:
    print(li.getText())