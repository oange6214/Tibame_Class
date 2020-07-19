import pymysql

# 連結 MySQL
link = pymysql.connect(
    host="localhost",
    user="root",
    passwd="",
    db="2020-03-31",
    charset="utf8"
)

# 取得指令操作變數
c = link.cursor()

def insert():
    # 傳送 SQL 指令, INSERT
    param = {
        "title": input('請輸入標題: '),
        "source": input('請輸入新聞來源: '),
        "create_date": input('請輸入發布日期: '),
        "description": input('請輸入新聞描述: ')
    }
    c.execute(
        "INSERT INTO `news` (`title`, `source`, `create_date`, `description`) " +
        "VALUES(%(title)s, %(source)s, %(create_date)s, %(description)s);",
        param)

def update():
    # 傳送 SQL 指令, UPDATE
    param = {
        "id": input('請輸入你要修改的資料 ID: '),
        "title": input('請輸入標題: '),
        "source": input('請輸入新聞來源: '),
        "create_date": input('請輸入發布日期: '),
        "description": input('請輸入新聞描述: ')
    }
    c.execute(
        "UPDATE `news` SET " +
        "`title`=%(title)s, `source`=%(source)s, `create_date`=%(create_date)s, `description`=%(description)s " +
        "WHERE `id`=%(id)s;",
        param)

def delete():
    # 傳送 SQL 指令, DELETE
    param = {
        "id": input('請輸入你要刪除的資料 ID: '),
    }
    c.execute(
        "DELETE FROM `news` " +
        "WHERE `id`=%(id)s;",
        param)

def select():
    # 傳送 SQL 指令, SELECT
	# 
    param = {
        "id": input('請輸入你要查詢的資料 ID: '),
    }
    c.execute(
        "SELECT `title`, `source` " + 
        "FROM `news` " + 
        "WHERE `id`=%(id)s;", 
        param)

select()
data = c.fetchone()
print(f"Database: {data} ")

# 送出
link.commit()
# 關閉 MySQL 連線
link.close()
