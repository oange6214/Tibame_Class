import pymysql

link = pymysql.connect(
    host='localhost',
    user='root',
    passwd="",
    db='python_ai',
    charset='utf8',
    port=3306
)
# 取得指令操作變數
c = link.cursor()


def select():
    # 顯示
    c.execute("SELECT * FROM `member`")

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[1], d[2], d[3])


def select_02():
    # 將 python_ai 資料庫的 member 資料表 與 tel 資料表 建立關聯
    # 顯示所有欄位
    c.execute(
        ''' SELECT * FROM `member` 
            INNER JOIN `tel` 
            ON `member`.`id` = `tel`.`member_id`;'''
    )

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[1], d[2], d[3])


def select_03():
    # 建立別名 member 設定為 A，tel 設定為 B
    # 顯示 id、name 欄位
    c.execute(
        ''' SELECT `A`.`id`, `A`.`name`, `B`.`tel` FROM `member` AS `A` 
            INNER JOIN `tel` AS `B` 
            ON `A`.`id` = `B`.`member_id`;'''
    )

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[1])


def select_04():
    # 顯示 關聯左邊資料表
    # 顯示 id、name 欄位
    c.execute(
        ''' SELECT `A`.`id`, `A`.`name`, `B`.`tel` FROM `member` AS `A` 
            LEFT JOIN `tel` AS `B` 
            ON `A`.`id` = `B`.`member_id`;'''
    )

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[1])


def select_05():
    # 顯示 關聯右邊資料表
    # 顯示 id、name 欄位
    c.execute(
        ''' SELECT `A`.`id`, `A`.`name`, `B`.`tel` FROM `member` AS `A` 
            RIGHT JOIN `tel` AS `B` 
            ON `A`.`id` = `B`.`member_id`;'''
    )

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[1])


select_05()

# 傳送 操作指令 到 伺服器端。新增、刪除、修改，需要做的
link.commit()

# 關閉連線，如果到達上限就無法連線。(到時需要重啟資料庫才可以)
link.close()
