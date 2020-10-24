#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                     user="root",  # your username
                     passwd="root",  # your password
                     db="binomotron")  # name of the data base

print("Connection réussie")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE3 (
   FIRST_NAME  CHAR(20) NOT NULL,
   LAST_NAME  CHAR(20),
   AGE INT,  
   SEX CHAR(1),
   INCOME FLOAT )"""

cursor.execute(sql)

db.close()
