from tasks import mysql_connect

cursor = mysql_connect().cursor()

sql = """ 
    select 名稱,評論數 from test1;
    """

cursor.execute(sql)

print(cursor.fetchall())