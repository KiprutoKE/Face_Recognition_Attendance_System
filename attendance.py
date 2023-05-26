import mysql.connector
import mysql


mydb = mysql.connector.connect(
    
    host = 'localhost',
    user = 'frank',
    password = '',
    db = 'attendance'    
) 

a = mydb.cursor()
#a.execute("CREATE DATABASE ATTENDANCE ")
#a.execute("CREATE TABLE UserAttendance (Date VARCHAR (30), USERNAME VARCHAR (255), DateTime VARCHAR (255), PRIMARY KEY(Date, USERNAME))")


#sql = "DROP DATABASE attendance"
#a.execute (sql)


mydb.commit()
mydb.close()
