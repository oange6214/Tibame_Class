import requests
import json
import os


def method1():
    url = "https://crsreports.congress.gov/search/results"

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0"
    }
    params = {
        "term": "",
        "orderBy": "Date",
        "navids": "4294960490",
        "navids": "4294967262",
        "pageNumber": "0",
    }

    font_url = "https://crsreports.congress.gov/product/pdf/download/"

    for page in range(3):
        params["pageNumber"] = page
        r = requests.get(url, headers=header, params=params)

        if r.status_code == 200:
            data = json.loads(r.text)
            result = data["SearchResults"]

            print(f"第 {page} 頁")
            for i, d in enumerate(result):
                download_url = f"{font_url}/{d['ProductTypeCode']}/{d['ProductNumber']}/{d['ProductNumber']}.pdf/"
                full_name = f"{d['ProductNumber']}.pdf"
                file_path = f"./pdf/{page}/"

                if not os.path.exists(file_path):
                    os.mkdir(file_path)

                file = file_path + full_name

                if os.path.exists(file):
                    print(f'{full_name} 以下載')
                else:
                    r = requests.get(download_url, stream=True)
                    print(f'第 {i + 1} 個檔案')
                    if r.status_code == 200:
                        print(f'{full_name} 下載中')

                        with open(file, 'wb') as f:
                            for chunk in r.iter_content(chunk_size = 128):
                                f.write(chunk)

                            print(f'{full_name} 下載完成')

                    else:
                        print('無法下載')
        else:
            print("網頁錯誤")


method1()