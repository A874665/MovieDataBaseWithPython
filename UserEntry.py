from CreateConnections import Connections
mydb = Connections()
mycursor= mydb.cursor()

def UserInput():

    Moviename = input("Enter Name of movie: ")
    MovieActor = input("Enter Name of Movie Actor: ")
    MovieActress = input("Enter Name of Movie Actress: ")
    MovieDirector = input("Enter Name of Movie Director: ")
    MovieReleased = input("Enter Year of MovieReleased: ")

    sqlform="Insert into movie(name,actor,actress,director,year_of_release) values(%s,%s,%s,%s,%s)"
    values =  [(Moviename,MovieActor,MovieActress,MovieDirector,MovieReleased)]

    mycursor.executemany(sqlform, values)

    mydb.commit() 

if __name__ == "__main__":
    UserInput()