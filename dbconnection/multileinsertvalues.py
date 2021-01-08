from dbconnection.dbconnect import *
db=get_connection()
cursor=db.cursor()

sql="insert into faculty(id,name,subject)values(%s,%s,%s)"
val=[
    ('102','raj','c++'),
    ('103','shiv','computer architecture'),
    ('104','meera','java'),
    ('105','geeta','python')
]
try:
    cursor.executemany(sql,val)
    db.commit()
    print("query executed")
except Exception as e:
    print(e.args)
finally:
    db.close()