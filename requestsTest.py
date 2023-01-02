import requests

url = 'https://www.google.com' #先將欲發出 GET 請求的網址先存在 url
res = requests.get(url) #對 url 發出 GET 請求，並將 Response 包成回傳物件存在 res
print(type(res), res) #Output: <class 'requests.models.Response'> <Response [200]>

############################################################################
# HTTP 的狀態碼 #
#200 OK：一切正常。
#301 Moved Permanently：永久搬家，會重新導向到新 url。
#302 Found（Moved Temporarily）：暫時移到新位置。
#400 Bad Request：明顯的用戶端錯誤，伺服器無法處理這個 Request。
#401 Unauthorized：未授權，請求需攜帶憑證。
#403 Forbidden：沒有權限。
#404 Not Found：找不到資源。
#418 I’m a teapot：我是一個茶壺，不會泡咖啡。(愚人節彩蛋)
#500 Internal Server Error：伺服器端錯誤。
#502 Bad Gateway：通常是伺服器的某個服務沒有正確執行。
#503 Service Unavailable：伺服器臨時維護或是快掛了，暫時無法處理請求(臨時流量過大)。
#504 Gateway Timeout：伺服器上的服務沒有回應。
############################################################################

# 第一種取得網址方法 (參數放到 url)
url1 = 'https://www.google.com/search?q=IThome&oq=IThome'
res1 = requests.get(url1)
print(res.url, res1)

# 第二種取得網址方法 (參數另外放)
url2 = 'https://www.google.com/search'
params = {'q':'IThome','oq':'IThome'}
requests.get(url2, params=params) #Output: https://www.google.com/search?q=IThome&oq=IThome <Response [200]>

