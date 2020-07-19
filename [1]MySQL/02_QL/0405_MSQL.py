import pymysql

link = pymysql.connect(
    host='localhost',
    user='root',
    passwd='',
    db='2020-04-05',
    charset='utf8'
)

# 取得指令操作變數
c = link.cursor()


def insert_1():
    title = input('請輸入標題: ')
    source = input('請輸入新聞來源: ')
    create_date = input('請輸入發布日期: ')
    description = input('請輸入新聞描述: ')

    # 傳送 SQL 指令
    c.execute(
        "INSERT INTO `news` (`title`, `source`, `create_date`, `description`) " +
        "VALUES(%s, %s, %s, %s);"
        , (title, source, create_date, description))


def insert_2():
    param = {
        "title": input('請輸入標題: '),
        "source": input('請輸入新聞來源: '),
        "create_date": input('請輸入發布日期: '),
        "description": input('請輸入新聞描述: ')
    }
    # 用字典方式帶入，是利用索引方式，其順序就無所謂
    c.execute(
        "INSERT INTO `news` (`title`, `source`, `create_date`, `description`) " +
        "VALUES(%(title)s, %(source)s, %(create_date)s, %(description)s);"
        , param)


def update():
    param = {
        "id": input('請輸入你要修改的資料 ID: '),
        "title": input('請輸入標題: '),
        "source": input('請輸入新聞來源: '),
        "create_date": input('請輸入發布日期: '),
        "description": input('請輸入新聞描述: ')
    }
    c.execute(
        "UPDATE `news` SET " +
        "`title` = %(title)s, `source` = %(source)s, `create_date` = %(create_date)s, `description` = %(description)s " +
        "WHERE `id` = %(id)s;"
        , param)


def delete():
    param = {
        "id": input('請輸入你要刪除的資料 ID: '),
    }
    c.execute(
        "DELETE FROM `news` WHERE `id` = %(id)s;"
        , param)


def select_1():
    # 指定抓取 id 資料
    param = {
        "id": input('請輸入你要查詢的資料 ID: '),
    }
    c.execute(
        "SELECT `title`, `source` " +
        "FROM `news` " +
        "WHERE `id` = %(id)s;",
        param
    )

    data = c.fetchone()  # 只取結果的第一筆資料
    print(f"Database: {data} ")
    count = c.rowcount  # 總共的資料筆數
    print(f"總筆數: {count} ")


def select_2():
    # 抓取全部資料，顯示 title、source 欄位
    c.execute(
        "SELECT `title`, `source` " +
        "FROM `news` "
    )

    data_all = c.fetchall()  # tuple 格式，每一個值代表一筆資料
    for d in data_all:
        print(d)
    count = c.rowcount  # 總共的資料筆數
    print(f"總筆數: {count} ")


def select_3():
    param = {

    }
    c.execute("SELECT * FROM `news`", param)

    ''' 一次全抓 '''
    # x = c.fetchall()
    # for d in x:
    #     print(d[0], d[3], d[1])

    ''' 一筆一筆抓 '''
    # d = c.fetchone()
    # print(d[0], d[3], d[1])
    #
    # d = c.fetchone()
    # print(d[0], d[3], d[1])

    ''' 根據總筆數，依序抓 '''
    n = c.rowcount
    for i in range(n):
        d = c.fetchone()
        print(d[0], d[3], d[1])


def insert_lastrowid():
    param = {
        "title": input('請輸入標題: '),
        "source": input('請輸入新聞來源: '),
        "create_date": input('請輸入發布日期: '),
        "description": input('請輸入新聞描述: ')
    }
    # 用字典方式帶入，是利用索引方式，其順序就無所謂
    c.execute(
        "INSERT INTO `news` (`title`, `source`, `create_date`, `description`) " +
        "VALUES(%(title)s, %(source)s, %(create_date)s, %(description)s);"
        , param)
    # 與 insert 做搭配
    print("資料 ID: ", c.lastrowid)


insert_lastrowid()

# 傳送 操作指令 到 伺服器端。新增、刪除、修改，需要做的
link.commit()

# 關閉連線，如果到達上限就無法連線。(到時需要重啟資料庫才可以)
link.close()
