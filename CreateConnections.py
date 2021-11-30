import mysql.connector

def Connections():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="",database="movie")
    return mydb
    

if __name__ == "__main__":
    if(Connections()):
        {
            print("connection Established")
        }
    else:
        {
            print("Falied")
        }
