import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, pwd,dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = pwd,
            database = dbname
        )
        print("success")
    except Error as e:
        print("the error occured at : ", e)
    return connection

con = create_con('cis3368classdb.cuu5dov2ewb1.us-east-1.rds.amazonaws.com','admin','Sponge1010?','cis3368db')
                                                                    #Endpoint, username, password, DB NAME IN SQL
cursor = conn.cursor(dictionary = True)
sql = 'select * from users'
cursor.execute(sql)
rows = cursor.fetchall()
for user in rows:
    print(user)
    print('first name : ', user['firstname'])