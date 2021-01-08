import mysql.connector

def get_connection():

    db=mysql.connector.connect(
    host="localhost",
    user="root",
    database="cms",
    password="P@ssword123"
    )

    return db
