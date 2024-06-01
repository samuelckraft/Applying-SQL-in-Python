import mysql.connector
from mysql.connector import Error

from connect_mysql import connect_database
#Task 1
conn = connect_database()

def get_members_in_age_range(start_age, end_age):
    if conn is not None:
        try:
            cursor = conn.cursor()


            query = 'select * from members where age between %s and %s'

            cursor.execute(query, (start_age, end_age))

            for row in cursor.fetchall():
                print(row)

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

get_members_in_age_range(0,50)