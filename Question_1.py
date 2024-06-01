import mysql.connector
from mysql.connector import Error

from connect_mysql import connect_database
#Task 1
conn = connect_database()

def add_member(id, name, age, trainer_id):
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_member = (id, name, age, trainer_id)

            query = 'insert into members (id, name, age, trainer_id) values (%s, %s, %s, %s)'

            cursor.execute(query, new_member)
            conn.commit()

            print("Member successfully added")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# add_member(5, "James Connor", 17, 2)


#Task 2
def add_workout_session(member_id, date, duration_minutes, calories_burned):
    if conn is not None:
        try:
            cursor = conn.cursor()

            new_session = (member_id, date, duration_minutes, calories_burned)

            query = 'insert into workoutsessions (member_id, session_date, session_time, calories_burned) values (%s, %s, %s, %s)'

            cursor.execute(query, new_session)
            conn.commit()

            print("Session successfully added")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# add_workout_session(1, '2024-04-02', 60, 300)

#Task 3
def update_member_age(member_id, new_age):
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = 'update members set age = %s where id = %s'

            cursor.execute(query, (new_age, member_id))
            conn.commit()

            print("Age successfully updated")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# update_member_age(1, 23)

#Task 4
def delete_workout_session(session_id):
    if conn is not None:
        try:
            cursor = conn.cursor()

            query = 'delete from workoutsessions where session_id = %s'
            
            cursor.execute(query, session_id)
            conn.commit()

            print("Session successfully deleted")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            cursor.close()
            conn.close()

# delete_workout_session(1)