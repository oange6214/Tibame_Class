'''
    作業：
        1. 用Python搭配MySQL製作一個會員管理系統，須具備新增、 刪除和修改會員的功能。
        2. 會員的資料欄位至少需要包含姓名、 生日、 地址等三個欄位
'''

import pymysql, os
import prettytable
import colorama


def select():
    table = prettytable.PrettyTable(["Id", "name", "birthday", "address"], encoding="utf8")
    table.align["Id"] = "m"
    table.align["name"] = "m"
    table.align["birthday"] = "m"
    table.align["address"] = "m"

    c.execute("SELECT * FROM `member`")

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        table.add_row(d)

    print(table)


def insert():
    # 新增
    param = {
        "name": input('請輸入名稱 (name): '),
        "birthday": input('請輸入生日 (birthday): '),
        "address": input('請輸入地址 (address): '),
    }
    # 用字典方式帶入，是利用索引方式，其順序就無所謂
    c.execute(
        "INSERT INTO `member` (`name`, `birthday`, `address`) " +
        "VALUES(%(name)s, %(birthday)s, %(address)s);"
        , param)


def update():
    # 更新
    param = {
        "id": input('請輸入你要修改的資料 ID: '),
        "name": input('請輸入名稱 (name): '),
        "birthday": input('請輸入生日 (birthday): '),
        "address": input('請輸入地址 (address): '),
    }
    c.execute(
        "UPDATE `member` SET " +
        "`name` = %(name)s, `birthday` = %(birthday)s, `address` = %(address)s " +
        "WHERE `id` = %(id)s;"
        , param)


def delete():
    # 刪除
    param = {
        "id": input('請輸入你要刪除的資料 ID: '),
    }
    c.execute(
        "DELETE FROM `member` WHERE `id` = %(id)s;"
        , param)


'''
    程式需求: 
        1. 清除畫面
        2. 登入
        3. 顯示 資料庫
        4. 使用者操作介面 (0)離開 (1)顯示 (2)新增 (3)更新 (4)刪除
        5. 每次操作，畫面清除一次
'''

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
    cmd = "1"
    while True:
        if cmd == "0":
            break
        elif cmd == "1":
            select()
        elif cmd == "2":
            insert()
        elif cmd == "3":
            update()
        elif cmd == "4":
            delete()

        print(f"(0) {colorama.Style.BRIGHT}離開程式")
        print(f"(1) {colorama.Fore.CYAN}顯示會員列表")
        print(f"(2) {colorama.Fore.LIGHTBLUE_EX}新增會員資料")
        print(f"(3) {colorama.Fore.MAGENTA}更新會員資料")
        print(f"(4) {colorama.Fore.RED}刪除會員資料")

        cmd = input("\n指令: ")
        os.system("cls")

    # 傳送 操作指令 到 伺服器端。新增、刪除、修改，需要做的
    link.commit()
    # 關閉連線，如果到達上限就無法連線。(到時需要重啟資料庫才可以)
    link.close()