import mysql.connector
from mysql.connector import Error


def connect_database():
    db_name = 'fitness_center'

    user = 'root' 

    password = '654U7jsv'

    host = 'localhost'

    try:
        conn = mysql.connector.connect(database = db_name, user = user, password = password, host = host)
        
        print('Connected to MySQL database successfully')

        return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None