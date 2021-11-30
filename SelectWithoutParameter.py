from CreateConnections import Connections
mydb = Connections()

mycursor= mydb.cursor()

mycursor.execute("Select * from movie ")
myresult = mycursor.fetchall() 

for row in myresult:
    print("Movie Name "+row[0])
    print("Actor "+row[1])
    print("Actress "+row[2])
    print("Director "+row[3])
    print("Year of Release "+ str(row[4]))
    print("________________________________")

mydb.close()


