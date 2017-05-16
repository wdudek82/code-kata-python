import sys
import sqlite3


with sqlite3.connect("test.db") as db_connect:
    print("Database opened/created")

    cursor = db_connect.cursor()
    try:
        db_connect.execute("""CREATE TABLE Employees(
                                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                                  first_name TEXT NOT NULL,
                                  last_name TEXT NOT NULL,
                                  age INTEGER NOT NULL,
                                  address TEXT,
                                  salary REAL,
                                  hire_date DATE);""")
        db_connect.commit()
    except sqlite3.OperationalError as e:
        print(e)

    print("Table 'Employee' created")

print("Database closed")
