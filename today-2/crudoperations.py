#install mysql.connector that is why you have the yellow line
import mysql.connector
import creds


from mysql.connector import Error
from sql import create_connection
from sql import execute_query
from sql import execute_read_query

#create connection to mysql database
myCreds = creds.Creds() # getting from creds.py file
connection = create_connection(myCreds.connectionstring, myCreds.username, myCreds.passwd, myCreds.dataBase)

#CRUD - Create, Read, Update and Delete

#create a new entry into users table
query = "insert into users(firstname, lastname, email) values ('test','testlastname','test@uh.edu')"
execute_query(connection, query)

#additional options with create new data 
fname = 'abc'
lname = 'pqr'
myemail = 'xyz@uh.edu'

query = "insert into users(firstname, lastname, email) values ('%s','%s','%s')" % (fname, lname, myemail)
execute_query(connection, query)

#read all users data in users table
query = "select * from users"
users = execute_read_query(connection, query)

for user in users:
    print(user['firstname'], ' ', user['lastname'])

#update a user in user table
uid = 2
query = "update users set email='testlast@uh.edu' where id = %s" % (uid)

execute_query(connection, query)

#delete one user from user table
uid = 2
query = "delete from users where id = %s" % (uid)
execute_query(connection, query)

#additional options with delete
deletetable_query = "drop table users"
execute_query(connection, deletetable_query)






































# import mysql.connector
# from mysql.connector import Error
# import creds #to use the class in this file you have to import it

# from sql import create_con
# from sql import execute_myquery
# from sql import execute_read_myquery

# from sql import create_con #create_con is a function that is part of the sql file that you created (sql.py)

# #connection to database
# mycreds = creds.creds()

# con = create_con(mycreds.hostname, mycreds.username, mycreds.password, mycreds.database)

# #CRUD operations - Create, Read, Update, Delete
# #create a new entry in database
# sql = "insert into users(firstname, lastname, email) values('myclass','lastnamemyclass','myclass@uh.edu')" #your information may be different for this part
# execute_myquery(con,sql)

# #update row information in the table of database
# userid = 8
# sql = "update users set email='mycode@uh.edu' where id=%s" % (userid) #%s= this says where would you like to place a value it is a placeholder
# #you are saying above go to this id number and update the id number with userid that is how you update it
# execute_myquery(con,sql) #once you click run, the terminal should say something like query successful and then you should see the rows and new changes in your sql terminal
# #to delete a row from Database
# userids = 10
# sql = "delete from users where id=%s"% (userids)
# execute_myquery(con,sql)

# #read rows from database
# sql = "select * from users"
# tablerows = execute_read_myquery(con,sql)
# print(tablerows)