from CreateConnections import Connections
mydb = Connections()

mycursor= mydb.cursor()

sqlform="Insert into movie(name,actor,actress,director,year_of_release) values(%s,%s,%s,%s,%s)"
movies =  [("Hencock","Will Smith","Charlize Theron","Peter Berg", 2008),
 ("IronMan","Robert Downey Jr.","Gwyneth Paltrow","Jon Favreau",2008),
 ("3-Idots","Amir Khan","Kareena Kapoor","Rajkumar Hirani",2009),
 ("Bahubali","Prabhas","Anushka Shetty","S. S. Rajamouli",2015),
 ("Avatar","Jake Sully"," Zoë Saldana","James Cameron",2009)]
mycursor.executemany(sqlform, movies)

mydb.commit()        #save changes from last change in sql statement    