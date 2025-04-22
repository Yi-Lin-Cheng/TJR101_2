import pymysql 

host = 'host.docker.internal'
port = 3306
user = 'root'
passwd = 'password'
db = 'TESTDB'
charset = 'utf8mb4'

conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
print('Successfully connected!')

cursor = conn.cursor()

