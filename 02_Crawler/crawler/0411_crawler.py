import requests
import time

def html_login():
    # 登入
    url = "http://teaching.bo-yuan.net/"
    data_dict = {
        "ex[class]": "5e81f839475de",
        "ex[username]": "11林柏翰",
        "ex[password]": "d1028b"
    }
    headers_dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cookie": "PHPSESSID=o8m2c0o7bg21lv19goqvvgtl57",
        "Referer": "http://teaching.bo-yuan.net/"
    }
    params_dict = {
        "uid": "5e9455efeed60"
    }

    r1 = requests.post(url, data=data_dict, headers=headers_dict, params=params_dict)


def html_login_check():
    # 登入並檢查成功與否
    url = "http://teaching.bo-yuan.net/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
        "Accept-Language": "zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Cookie": "PHPSESSID=o8m2c0o7bg21lv19goqvvgtl57",
        "Referer": "http://teaching.bo-yuan.net/"
    }
    data = {
        "ex[class]": "5e81f839475de",
        "ex[username]": "11林柏翰",
        "ex[password]": "d1028b"
    }
    params = {
        "uid": "5e9eb07690d90"
    }
    r1 = requests.post(url, data=data, headers=headers, params=params)
    r2 = requests.get(url, headers=headers)
    r2.encoding = "utf-8"

    if r2.text.find("?ac1=member") != -1:
        print("登入成功")
    else:
        print("登入失敗")

html_login_check()