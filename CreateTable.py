from CreateConnections import Connections
mydb = Connections()

mycursor= mydb.cursor()

mycursor.execute("Create table Movie(name varchar(100),actor varchar(100),actress varchar(100),director varchar(100), year_of_release int(4))")

mycursor.execute("Show tables")
for table in mycursor:
    print(table)
