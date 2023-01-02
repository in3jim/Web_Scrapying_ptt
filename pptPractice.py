import requests
import json
from bs4 import BeautifulSoup

article_list = []

def get_resp(url):
    cookies = {
        'over18': '1'
    }
    resp = requests.get(url, cookies=cookies)
    if resp.status_code != 200:
        return 'error'
    else:
        return resp

def get_articles(resp):
    soup = BeautifulSoup(resp.text, 'html5lib')
    arts = soup.find_all('div', class_='r-ent')
    for art in arts:
        title = art.find('div', class_='title').getText().strip()
        if not title.startswith('(本文已被刪除)'):
            link = 'https://www.ptt.cc' + \
                art.find('div', class_='title').a['href'].strip()
        author = art.find('div', class_='author').getText().strip()
        article = {
            'title': title,
            'link': link,
            'author': author
        }
        article_list.append(article)
        # print(f'title: {title}\nlink: {link}\nauthor: {author}')
    # 利用 Css Selector 定位下一頁網址
    next_url = 'https://www.ptt.cc' + \
        soup.select_one(
            '#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)')['href']
    return next_url

# 當執行此程式時成立
if __name__ == '__main__':
    # 第一個頁面網址
    url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
    # 先讓爬蟲爬 10 頁
    for now_page_number in range(5):
        resp = get_resp(url)
        if resp != 'error':
            url = get_articles(resp)
        print(f'======={now_page_number+1}/5=======')
    # 將存放所有文章資訊的串列存於 JSON 檔案中
    with open('ptt-articles.json', 'w', encoding='utf-8') as f:
        json.dump(article_list, f, indent=2,
                  sort_keys=True, ensure_ascii=False)