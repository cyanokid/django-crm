#install mysql in your computer
#https://dev.mysql.com/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

#connect Database
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create db
cursorObject.execute("CREATE DATABASE elderco")

print('All Done! ')

#dont forget to migrate after set up all the db