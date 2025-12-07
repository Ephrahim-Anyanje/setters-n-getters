"""
a cpass can be assoicated with an entire table
class attributes are now asscoiated with table columns
The classes instances are the rows in the table
"""
#builtin sqlite3 module
import sqlite3
#create a database connection to our db
conn=sqlite3.connect('students.db')
#create a cursor to execute SQL commands
cursor=conn.cursor()


class Student:
    TABLE_NAME = 'students'

    def __init__(self, name, email, age, id=None):
        self.id = id
        self.name = name
        self.email = email
        self.age = age

    #instance method to save a student to the database
    def save(self):
        #prepared statement ->prevents SQL injection attacks
        sql = f"INSERT INTO {self.TABLE_NAME} (name, email, age) VALUES (?, ?, ?)"
        cursor.execute(sql, (self.name, self.email, self.age))
        self.id = cursor.lastrowid
        conn.commit()
        print("Student created.")

    @classmethod
    def get_all(cls):
        sql = f"SELECT * FROM {cls.TABLE_NAME}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return [cls(name=row[1], email=row[2], age=row[3], id=row[0]) for row in rows]

    @classmethod
    def create_table(cls):
        # SQL command to create the students table
     sql=f"""
        CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age INTEGER NOT NULL
        )"""
     
     #use the cursor to execute the SQL command
     cursor.execute(sql)
     #commit the changes to the database
     conn.commit()

     print("Table created successfully.")

Student.create_table()

student1=Student("Ephraim","ephraim@gmail.com",17)
student1.save()
