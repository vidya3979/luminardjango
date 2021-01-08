import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@ssword123"
)
cursor=db.cursor()
sql="SELECT VERSION()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)
