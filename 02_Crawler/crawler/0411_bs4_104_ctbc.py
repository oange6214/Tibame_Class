from bs4 import BeautifulSoup
import requests
import prettytable
import colorama as cm
import json

cm.init(True)


def search_104():
    keyword = input("請輸入你要搜尋的職缺關鍵字: ")

    url = "https://www.104.com.tw/jobs/search/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    params = {
        "ro": "0",
        "keyword": keyword,
        "order": "12",
        "asc": "0",
        "page": "1",
        "mode": "s",
        "jobsource": "2018indexpoc"
    }

    t = prettytable.PrettyTable(["公司名稱", "職缺名稱"], encoding="utf8")

    for page in range(1, 3):
        params["page"] = page

        r1 = requests.get(url, headers=header, params=params)

        if r1.status_code == 200:
            html = BeautifulSoup(r1.text, "html.parser")
            info = html.find_all('article', "job-list-item")

            for p in info:
                add = [p.attrs['data-cust-name'], f"{cm.Fore.RED}{p.attrs['data-job-name']}{cm.Fore.RESET}"]
                t.add_row(add)
        else:
            print('連線失敗')

    print(t)


def ctbcbank():
    url = "https://www.ctbcbank.com/IB/api/adapters/IB_Adapter/resource/preLogin"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0",
        "X-Channel-Id": "EBMW_WEB_O",
    }
    json_dict = {
        "resource": "/twrbo-general/qu002/010",
        "rqData": {"pageNo": 1},
        "trackingIxd": "986a599a-f719-44c0-ad4b-498cf01ffed3",
    }

    rd_index = 1
    for page in range(3):
        json_dict["rqData"]["pageNo"] = page + 1

        r1 = requests.post(url, headers=header, json=json_dict)
        datas = json.loads(r1.text)
        serviceLocationModels = datas["rsData"]["serviceLocationModels"]

        for location in serviceLocationModels:
            print(f'第 {rd_index} 家')
            print(location['bhName'], location['bhNameEn'])
            print(location['bhAddr'])
            print(location['bhAddrEn'])
            print(location['bhBTime'], '\t',location['phoneNumber'])
            print('-' * 100)

            rd_index += 1


ctbcbank()
