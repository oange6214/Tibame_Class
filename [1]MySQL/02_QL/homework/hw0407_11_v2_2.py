'''
    為上一個作業擴充，
    建置每個會員的電話清單，每個會員可以有多個電話資料，電話資料要可以查看、
    新增跟刪除，需使用到「多資料表聯合搜尋」功能。
'''

import pymysql, os
import prettytable
import colorama


def select_tel():
    # 顯示 會員編號、電話
    select()

    mem_id = input('請選擇要刪除的會員編號: ')
    os.system("cls")

    c.execute(
        "SELECT * FROM `tel` WHERE `tel`.`member_id` = " + mem_id
    )

    table = prettytable.PrettyTable(["編號", "電話"], encoding="utf8")
    table.align["編號"] = "r"
    table.align["電話"] = "m"

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        d = (d[0], d[2])
        table.add_row(d)

    print(table)


def insert_relate():
    # 新增 指定會員的 電話號碼
    select()

    # 新增
    param = {
        "member_id": input('請選擇要添加的會員編號: '),
        "tel": input("請輸入電話: ")
    }
    # 用字典方式帶入，是利用索引方式，其順序就無所謂
    c.execute(
        "INSERT INTO `tel` (`member_id`, `tel`) " +
        "VALUES(%(member_id)s, %(tel)s);"
        , param)

    os.system("cls")


def delete_relate():
    # 刪除 指定會員的電話
    select_tel()

    # 刪除
    param = {
        "id": input('請輸入你要刪除的電話編號: '),
    }
    c.execute(
        "DELETE FROM `tel` WHERE `id` = %(id)s;"
        , param)

    os.system("cls")


def select():
    # 顯示 會員的編號、姓名、生日、地址、電話
    c.execute(
        '''
        SELECT * FROM `member` AS `A` 
        LEFT JOIN `tel` AS `B` 
        ON `A`.`id` = `B`.`member_id`;
        '''
    )

    table = prettytable.PrettyTable(["編號", "姓名", "生日", "地址", "電話"], encoding="utf8")
    table.align["編號"] = "r"
    table.align["姓名"] = "m"
    table.align["生日"] = "m"
    table.align["地址"] = "m"
    table.align["電話"] = "m"

    ''' 根據總筆數，依序抓 '''
    temp = ""
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()

        # 會員的資料重複 只顯示電話
        if temp == d[0]:
            d = ("", "", "", "", f"{colorama.Fore.LIGHTBLUE_EX}{d[6]}{colorama.Fore.RESET}")
        else:
            temp = d[0]
            d = (d[0], f"{colorama.Fore.RED}{d[1]}{colorama.Fore.RESET}", d[2], d[3],
                 f"{colorama.Fore.LIGHTBLUE_EX}{d[6]}{colorama.Fore.RESET}")

        table.add_row(d)

    print(table)


def insert():
    # 新增
    param = {
        "name": input('請輸入會員名稱: '),
        "birthday": input('請輸入會員生日: '),
        "address": input('請輸入會員地址: '),
    }
    # 用字典方式帶入，是利用索引方式，其順序就無所謂
    c.execute(
        "INSERT INTO `member` (`name`, `birthday`, `address`) " +
        "VALUES(%(name)s, %(birthday)s, %(address)s);"
        , param)

    os.system("cls")


def update():
    select()

    # 更新
    param = {
        "id": input('請輸入你要修改的會員編號: '),
        "name": input('請輸入會員名稱: '),
        "birthday": input('請輸入會員生日: '),
        "address": input('請輸入會員地址: '),
    }
    c.execute(
        "UPDATE `member` SET " +
        "`name` = %(name)s, `birthday` = %(birthday)s, `address` = %(address)s " +
        "WHERE `id` = %(id)s;"
        , param)

    os.system("cls")

def delete():
    select()

    # 刪除
    param = {
        "id": input('請輸入你要刪除的會員編號: '),
    }
    c.execute(
        "DELETE FROM `member` WHERE `id` = %(id)s;"
        , param)

    os.system("cls")

if __name__ == "__main__":
    os.system("cls")
    # 初始化 Colorama 函式庫設定
    colorama.init(True)

    while True:
        # 登入
        setting_pass = input("請輸入資料庫的 root 密碼: ")
        setting_port = input("請輸入資料庫的 port: ")

        if setting_port == "":
            setting_port = 3306
        else:
            setting_port = int(setting_port)

        try:
            link = pymysql.connect(
                host='localhost',
                user='root',
                passwd=setting_pass,
                db='python_ai',
                charset='utf8',
                port=setting_port
            )
            os.system("cls")
            break
        except pymysql.err.OperationalError:
            print("連線錯誤\n")

    # 取得指令操作變數
    c = link.cursor()

    # 操作介面
    cmd = "-1"
    while True:
        if cmd == "0":
            break
        elif cmd == "1":
            select()
            link.commit()
        elif cmd == "2":
            insert()
            link.commit()
        elif cmd == "3":
            update()
            link.commit()
        elif cmd == "4":
            delete()
            link.commit()
        elif cmd == "5":
            insert_relate()
            link.commit()
        elif cmd == "6":
            delete_relate()
            link.commit()

        print(f"(0) {colorama.Style.BRIGHT}離開程式")
        print(f"(1) {colorama.Fore.CYAN}顯示會員列表")
        print(f"(2) {colorama.Fore.LIGHTBLUE_EX}新增會員資料")
        print(f"(3) {colorama.Fore.MAGENTA}更新會員資料")
        print(f"(4) {colorama.Fore.RED}刪除會員資料")
        print(f"(5) {colorama.Fore.LIGHTBLUE_EX}新增會員電話")
        print(f"(6) {colorama.Fore.MAGENTA}刪除會員電話")

        cmd = input("\n指令: ")
        os.system("cls")

    # 傳送 操作指令 到 伺服器端。新增、刪除、修改，需要做的

    # 關閉連線，如果到達上限就無法連線。(到時需要重啟資料庫才可以)
    link.close()
