from flask import Flask, request
import os

import pymysql
import pymysql.cursors

app = Flask(__name__)

# Connect to the database


# with connection.cursor() as cursor:
#     # Create a new record
#     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%(email)s, %(password)s)"
#     params = {
#         "email": 'abc@line.me',
#         "password": 'very-secret'
#     }
#     cursor.execute(sql, params)
# connection.commit()

@app.route('/')
def hello():
    connection = pymysql.connect(host=os.environ.get('CLEARDB_DATABASE_HOST'),
                                 user=os.environ.get('CLEARDB_DATABASE_USER'),
                                 password=os.environ.get('CLEARDB_DATABASE_PASSWORD'),
                                 db=os.environ.get('CLEARDB_DATABASE_DB'),
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `email` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('abc@line.me',))
        result = cursor.fetchone()
        print(result)
    return f'Hello, Heroku {result["email"]}!'


if __name__ == 'main':
    app.run()  # 啟動伺服器
