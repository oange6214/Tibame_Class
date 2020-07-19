from bs4 import BeautifulSoup
import requests
import colorama
import codecs
import prettytable

# 初始化 Colorama 函式庫設定
colorama.init(True)

url = "https://www.taiwan.net.tw/m1.aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}
params = {
    "sNo": "0001001",
    "page": 1
}

def title_date(url, headers, params):
    r1 = requests.get(url, headers=headers, params=params)

    html = BeautifulSoup(r1.text, "html.parser")

    title = html.find_all("a", {"class": "columnBlock-title"})
    for d in title:
        print(d.text)

    date = html.find_all("span", {"class": "date"})
    for d in date:
        print(d.text)

def title_date_multi(url, headers, params):
    t = prettytable.PrettyTable(["日期", "標題"], encoding="utf8")

    for p in range(1, 6):
        r1 = requests.get(url, headers=headers, params=params)

        html = BeautifulSoup(r1.text, "html.parser")
        data_table = html.find_all('div', "columnBlock-info")

        print(f"{colorama.Fore.BLUE}第 {p} 頁{colorama.Fore.RESET}")
        for data in data_table:
            title = data.find("a", class_="columnBlock-title").text
            date = data.find("span", class_="date").text

            t.add_row([date, f"{colorama.Fore.RED}{title}{colorama.Fore.RESET}"])

        print(t)

def html_title_date_href(url, headers, params):

    r1 = requests.get(url, headers=headers, params=params)

    html = BeautifulSoup(r1.text, "html.parser")
    data_table = html.find_all('div', "columnBlock-info")

    for data in data_table:
        title = data.find("a", "columnBlock-title")
        date = data.find("span", "date")

        print(title.attrs['href'], end='\t')
        print(date.text, end='\t')
        print(title.text)

def taiwan_net_save():
    url = "https://www.taiwan.net.tw/"
    last_url = "m1.aspx?sNo=0001001"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    r1 = requests.get(url + last_url, headers=headers)

    html = BeautifulSoup(r1.text, "html.parser")
    data_table = html.find_all('div', "columnBlock-info")

    fn = 1
    for data in data_table:
        title = data.find("a", "columnBlock-title")
        date = data.find("span", "date")

        last_url = title.attrs['href']

        # 判斷 是否正常子網址路徑
        if last_url.find("m1.aspx") != -1:
            child_page = requests.get(url + last_url, headers=headers)
            child_html = BeautifulSoup(child_page.text, "html.parser")

            content = child_html.find('div', 'content')
            articles = content.find_all("p")

            # print(date.text, end='\t')
            # print(title.text)
            # for article in articles:
            #     print(article.text)
            # print('-' * 100)

            with codecs.open('html/' + str(fn) + ".txt", 'w', 'utf-8') as f:
                f.write(f"{title.text} \r\n")
                f.write(f"{date.text} \r\n\r\n")
                for article in articles:
                    f.write(f"{article.text}")

                fn += 1

taiwan_net_save()