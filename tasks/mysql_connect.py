import pymysql

def mysql_connect():
    host = '34.81.248.239'
    port = 3306
    user = 'TJR101_2'
    passwd = 'TJR101_2pass'
    db = 'mydb'
    charset = 'utf8mb4'

    conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)

    return conn

