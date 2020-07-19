import requests
import codecs

def html_status_save_html():
    r1 = requests.get(
        "https://www.taiwan.net.tw/m1.aspx",
        params={
            "sNo": "0001001",
            "page": 1
        }
    )

    print("網頁狀態代碼: ", r1.status_code)

    print("網頁回傳的標題: ")
    for k in r1.headers.keys():
        print(k, ":", r1.headers[k])

    print("編碼: ", r1.encoding)

    # 讀取內容 (以純文字型態讀取，會自動做編碼的轉換)
    # print(r1.text)

    # 利用 codecs 將 文字 轉 HTML
    # with codecs.open("2020-04-07.html", "w", "utf8") as f:
    #     #     f.write(r1.text)


def save2html():
    for page in range(1, 6):
        r1 = requests.get(
            "https://www.taiwan.net.tw/m1.aspx",
            params={
                "sNo": "0001001",
                "page": page
            }
        )
        with codecs.open(f"taiwan.net.tw/{page}.html", "w", "utf8") as f:
            f.write(r1.text)

# html_status_save_html()
save2html()