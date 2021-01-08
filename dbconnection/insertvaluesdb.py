from dbconnection.dbconnect import *
db=get_connection()
cursor=db.cursor()
sql="insert into faculty(id,name,subject)values('101','vijay','datastructure')"

try:
    cursor.execute(sql)
    db.commit()
    print("query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()
