import requests
import json


def single_page():
    url = "https://shopee.tw/api/v2/search_items/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
    }
    params = {
        "by": "relevancy",          #
        "categoryids": "72",        # 搜尋條件 編號，可有可無。影響搜尋條件，因為條件很多，需要再分析。
        "keyword": "動物森友會",     # 搜尋的關鍵字
        "limit": "50",              # 限制 顯示筆數 (就是 到哪裡結束)
        "newest": "0",              # 筆數 偏移量 (就是 從哪裡開始)
        "order": "desc",            # 排序方式 asc (由小到大)、desc (由大到小)
        "page_type": "search",      # 頁面類型
        "version": "2",             # 版本
    }

    # 請求 搜尋網頁，分析 json 檔
    r = requests.get(url, headers=header, params=params)
    data = json.loads(r.text) # 將請求的網址原始碼 (事前已經知道是 json 檔)，利用 JSON 解析
    print(type(data)) # 字典類型

    items = data["items"]   # 根據分析 資料包覆在 items 中

    item_index = 1
    for item in items:
        '''
            根據分析，搜尋欄位提供的金額無法解析公式。
            以下是 分析每個產品的網址，取得網址後進行分析。
            最後從 子網址 分析出 正確金額。
            可以檢查網址的正確性、金額正確性
        '''

        url = f"https://shopee.tw/{item['name']}-i.{item['shopid']}.{item['itemid']}"
        print(f"第 {item_index} 筆")
        print("itemid: ", item['itemid'])
        print("shopid: ", item['shopid'])
        print("產品網址: ", url)
        print("產品名稱: ", item["name"])

        # 請求 產品網頁，分析 json 檔
        url = "https://shopee.tw/api/v2/item/get?"
        params = {
            "itemid": item['itemid'],
            "shopid": item['shopid']
        }
        r = requests.get(url, headers=header, params=params)
        data = json.loads(r.text)

        inner_item = data["item"]

        # 取 價格最小、最大、定價
        item_price_min = int(inner_item["price_min"] / 100000)
        item_price_max = int(inner_item["price_max"] / 100000)
        item_price_med = int(inner_item["price"] / 100000)

        # 判斷 價格顯示
        if item_price_min == item_price_max:
            print(f"產品價格: {item_price_med}")
        else:
            print(f"產品價格: {item_price_min} ~ {item_price_max}")

        item_index += 1
        print('-' * 100)


def multi_page(keyword, page=1):
    '''
        根據分析，可以 根據 limit、newest 來抓取 多頁資料
    '''
    # 產品筆數
    item_index = 1

    for p in range(page):
        url = "https://shopee.tw/api/v2/search_items/"
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
        }
        params = {
            "by": "relevancy",
            "categoryids": "",
            "keyword": keyword,
            "limit": 50,
            "newest": p * 50,
            "order": "desc",
            "page_type": "search",
            "version": "2",
        }

        # 請求 搜尋網頁，分析 json 檔
        r = requests.get(url, headers=header, params=params)
        data = json.loads(r.text)

        items = data["items"]

        for item in items:
            url = f"https://shopee.tw/{item['name']}-i.{item['shopid']}.{item['itemid']}"
            print(f"第 {item_index} 筆")
            print("itemid: ", item['itemid'])
            print("shopid: ", item['shopid'])
            print("產品網址: ", url)
            print("產品名稱: ", item["name"])

            # 請求 產品網頁，分析 json 檔
            url = "https://shopee.tw/api/v2/item/get?"
            params = {
                "itemid": item['itemid'],
                "shopid": item['shopid']
            }
            r = requests.get(url, headers=header, params=params)
            data = json.loads(r.text)

            inner_item = data["item"]

            # 取 價格最小、最大、定價
            item_price_min = int(inner_item["price_min"] / 100000)
            item_price_max = int(inner_item["price_max"] / 100000)
            item_price_med = int(inner_item["price"] / 100000)

            # 判斷 價格顯示
            if item_price_min == item_price_max:
                print(f"產品價格: {item_price_med}")
            else:
                print(f"產品價格: {item_price_min} ~ {item_price_max}")

            item_index += 1
            print('-' * 100)

single_page()
# multi_page("NB F80", 1)
