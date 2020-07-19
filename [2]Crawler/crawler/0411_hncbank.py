import requests
import codecs

def api_get():
    '''
        分析 華南銀行分行位置, 因為動態載入, 所以 要抓 API 的網址
    '''

    url = "https://www.hncb.com.tw/hncb/XML/Taiwan.xml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
    }

    r = requests.get(url, headers=headers)

    with codecs.open("2020-04-11.xml", "w", "utf-8") as f:
        f.write(r.text)

api_get()