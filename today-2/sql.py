import mysql.connector
from mysql.connector import Error

#create a connection function
def create_con(hostname, uname, pwd, dbname):
    connection = None

    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = uname,
            password = pwd,
            database = dbname
        )
        print('Connection successful')
    except Error as e: #e is like a variable that you can use like x in algebra
        print('connection unsuccesful, error is: ', e)
    return connection

def execute_query(connection, query): #this function will only execute your code. In order to actually retrieve the rows use the fetchall method
    cursor = connection.cursor()
    try: 
        cursor.execute(query)
        connection.commit()
        print("Query completed successfully")
    except Error as e:
         print('Error occured is: ', e)
#execute a query to read from database (select statement)
def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary = True) 
    rows = None
    try:
        cursor.execute(query)
        rows = cursor.fetchall() #lines 27-37 fetch each row from sql and turn them into dictionaries
        return rows
    except Error as e:
        print('Error occurred is: ', e)

            
    
    
        