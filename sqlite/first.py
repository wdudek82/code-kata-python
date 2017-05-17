import sys
import sqlite3


def print_db(db_cursor):
    try:
        db_cursor.execute("SELECT * FROM Employees;")
    except sqlite3.OperationalError as e:
        print(e)
    else:
        print([column[0] for column in db_cursor.description])
        result = db_cursor.fetchall()

        for row in result:
            print(row)


with sqlite3.connect("test.db") as db_connect:
    print("Database opened/created")

    cursor = db_connect.cursor()

    db_connect.execute("DROP TABLE IF EXISTS Employees;")
    # db_connect.commit()

    print("Employee tables was deleted")

    try:
        db_connect.execute("CREATE TABLE Employees("
                           "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"
                           "first_name TEXT NOT NULL,"
                           "last_name TEXT NOT NULL,"
                           "age INTEGER NOT NULL,"
                           "address TEXT,"
                           "salary REAL,"
                           "hired_date DATE);")
    except sqlite3.OperationalError as e:
        print(e)
    else:
        db_connect.commit()

        # Or I can use: db_connect.execute(...)
        cursor.execute("INSERT INTO Employees (first_name, last_name, age, address, salary, hired_date)"
                       "VALUES ('John', 'Doe', 25, NULL, 6000000, date('now'));")
        cursor.execute("INSERT INTO Employees (first_name, last_name, age, address, salary, hired_date)"
                       "VALUES ('Mary', 'Jane', 21, NULL, 8000000, date('now'));")
        db_connect.commit()
        print_db(cursor)

    print("Table 'Employee' created")

    cursor.execute("UPDATE Employees "
                   "SET address = 'Cracow, POLAND'"
                   "WHERE id = 1;")

    print("\nUpdated in Employees table row id 1")
    print_db(cursor)

    cursor.execute("DELETE FROM Employees "
                   "WHERE id = 2;")

    print("\nDeleted from Employees row id 1")
    print_db(cursor)

    # Rolls back any changes to the database since the last call to commit()
    db_connect.rollback()
    print("\nRollback deletion")
    print_db(cursor)

    cursor.execute("ALTER TABLE Employees ADD COLUMN 'image' BLOB DEFAULT NULL;")
    db_connect.commit()

    print_db(cursor)

    cursor.execute("SELECT sqlite_version()")
    print("SQLite version: %s" % cursor.fetchone())


    db_connect.row_factory = sqlite3.Row
    cursor2 = db_connect.cursor()
    cursor2.execute("SELECT * FROM Employees;")

    for row in cursor2.fetchall():
        print(row["first_name"])
    print("\n")

    # Creating a dump
    with open("dump.sql", "w") as f:
        for row in db_connect.iterdump():
            print(row)
            f.write("%s\n" % row)

print("\nDatabase closed")
