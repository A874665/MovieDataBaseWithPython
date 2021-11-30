import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="")
mycursor= mydb.cursor()
mycursor.execute("Create database movie")  #create database
mycursor.execute("Show databases")  # for execution

for db  in mycursor:
    print(db)