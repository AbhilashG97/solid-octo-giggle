# This python script creates a fruit database that will
# be used by the flask application

import sqlite3
from sqlite3 import Error

def create_connection():
    try:
        connection = sqlite3.connect('mock_ahms.db')
        return connection
    except Error:
        print(Error)

def create_table(connection):
    cursor_obj = connection.cursor()
    cursor_obj.execute('''
        CREATE TABLE ahms(
            student_id integer PRIMARY KEY,
            first_name text,
            last_name text,
            has_stayback integer,
            date text,
            time text,
            faculty_name text,
            reason text
        )
    ''')
    connection.commit()

def insert_values(connection):
    cursor_object = connection.cursor()
    cursor_object.execute('''
        INSERT INTO ahms values 
        (18001, "Jakan", "Hagar", 1, "31-05,-2019", "9:15PM", "Ram Manohar", "HUT Labs"),
        (18002, "July", "Lanister", 0, "31-05,-2019", "", "", ""),
        (18003, "Aemon", "Topiwala", 1, "31-05,-2019", "10:15PM", "Lekshmi Subhash", "Amachi Labs"),
        (18004, "A. Agar", "Hagar", 1, "31-05,-2019", "9:30PM", "Jamie Manohar", "Sports"),
        (18005, "August", "Kalra", 1, "31-05,-2019", "9:45PM", "Ram Mansingh", "Amrita WNA"),
        (18006, "Jakki", "Sonu Singh", 0, "31-05,-2019", "", "", ""),
        (18007, "Guru", "Devi", 1, "31-05,-2019", "9:15PM", "Hydar Ram Nair", "CISCO"),
        (18008, "Lei", "Chi", 0, "31-05,-2019", "", "", "")
    ''')
    connection.commit()

connection = create_connection()

try:
    create_table(connection)
except: 
    print('Ah oh, could not create the table!')

try:
    insert_values(connection)
except:
    print('Error inserting values!')