from CreateConnections import Connections
mydb = Connections()

mycursor= mydb.cursor()

mycursor.execute("Select name, director from movie where year_of_release BETWEEN %s and %s",(2008,2009))
myresult = mycursor.fetchall() 
for data in myresult:
    print("Name Of Movie: ",data[0])
    print("name of Movie Director: ", data[1])
    print("_____________________________")

mycursor.execute("Select actor, actress from movie where name in (%s,%s)",('Hencock', 'Avatar'))
# mycursor.execute("SELECT * FROM movie ORDER BY name")
myresult = mycursor.fetchall() 
for data in myresult:
    print(data)
    print("Name Of Actor: ",data[0])
    print("name of Actress: ", data[1])
    print("_____________________________")