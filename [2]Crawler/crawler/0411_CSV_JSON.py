import requests
import codecs
import io
import csv
import json
import prettytable


def csv_read():
    ''' 讀取本機的 CSV 方法一 '''
    # data_list = list(csv.reader(codecs.open("2020-04-11.csv", "r", "utf-8")))

    ''' 讀取本機的 CSV 方法二 '''
    with codecs.open("2020-04-11.csv", "r", "utf-8") as f:
        reader = csv.reader(f)
        data_list = list(reader)

    for d in data_list:
        print(d)

def request_get_csv():
    ''' 讀取線上 CSV，並顯示 '''

    url = 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv'
    r = requests.get(url)
    r.encoding = 'utf-8'

    print(r.text)
    print(type(r.text))  # 請求內容 類型 str

def request_get_stringIO_csv():
    ''' 利用 io package 轉 file-stream '''

    url = 'https://od.cdc.gov.tw/eic/NHI_EnteroviralInfection.csv'
    r = requests.get(url)
    r.encoding = 'utf8'

    s = io.StringIO(r.text)  # 字串 轉 檔案串流
    c = list(csv.reader(s))  # 利用 csv.reader() 解析 檔案

    print(type(s))

    for d in c:
        print(*d)

def request_get_stringIO_csv_2():
    ''' 利用 io package 轉 file-stream '''

    url = 'https://data.taipei/api/getDatasetInfo/downloadResource?id=58b4f7b9-d0c5-4de8-aa7f-981fcb625e45&rid=a1c35319-c67d-4c7b-86fe-442874cb3d79'
    r = requests.get(url)
    r.encoding = 'big5'

    s = io.StringIO(r.text)  # 字串 轉 檔案串流
    c = list(csv.reader(s))  # 利用 csv.reader() 解析 檔案

    print(type(s))

    for d in c:
        print(d[1], d[0], d[3], d[4])

def request_get_json():
    t = prettytable.PrettyTable(["學校名稱", "學校地址"], encoding="utf8")

    url = "https://data.taipei/api/getDatasetInfo/downloadResource"
    params_dict = {
        "id": "ac589468-529b-4636-a9b2-ab57ae41cbcb",
        "rid": "24c9f8fe-88db-4a6e-895c-498fbc94df94"
    }
    r = requests.get(url, params=params_dict)
    data = json.loads(r.text)

    for d in data:
        t.add_row([d["o_tlc_agency_name"], d["o_tlc_agency_address"]])

    print(t)

def web_api_json_get():
    '''
        資料網址: https://data.taipei/#/dataset/detail?id=ac589468-529b-4636-a9b2-ab57ae41cbcb

        API 位置:
        	https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=24c9f8fe-88db-4a6e-895c-498fbc94df94
    '''

    t = prettytable.PrettyTable(["學校名稱", "學校地址"], encoding="utf8")

    url = "https://data.taipei/opendata/datalist/apiAccess"
    params_dict = {
        "scope": "resourceAquire",
        "rid": "24c9f8fe-88db-4a6e-895c-498fbc94df94",
        "limit": input("請輸入顯示幾筆資料: ")
    }
    r = requests.get(url, params=params_dict)
    datas = json.loads(r.text)
    data = datas["result"]["results"]

    for d in data:
        t.add_row([d["o_tlc_agency_name"], d["o_tlc_agency_address"]])

    print(t)

web_api_json_get()