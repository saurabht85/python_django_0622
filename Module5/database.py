import sqlite3

try:
    conn = sqlite3.connect("test.db")
    print("Opened Database for operation")
    cursor = conn.cursor()

    # cursor.execute('''
    # create table students (ID PRIMARY KEY NOT NULL,
    # NAME VARCHAR2(50) NOT NULL, AGE INT, COURSE VARCHAR2(10))
    # ''')
    # print("Table created successfully")
    # cursor.execute('''
    # INSERT INTO students values (1, "Sam", 23, "CS")
    # ''')
    # cursor.execute('''
    # INSERT INTO students values (2, "Priya", 24, "ME")
    # ''')
    #name = input("Enter the name you want to delete")
    # course = input("Enter the new course")
    # cursor.execute('''
    # UPDATE students set course = ? where name = ?''', (course, name)
    # )
    #cursor.execute("DELETE from students where name = ?", (name,))
    #conn.commit()
    data = cursor.execute("SELECT * from students")
    for row in data:
       print(row)
    conn.close()
    print("Records Updated")
except Exception as e:
    print(e)
    print("Failed try again")