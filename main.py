import sqlite3

DB_NAME = 'SQLite_db.db'

with sqlite3.connect(DB_NAME) as sqlite_con:
    sql_req = "SELECT * FROM courses"
    sql_cursos = sqlite_con.execute(sql_req)
    # for record in sql_cursos:
    # print(record)
    # print(record[2])
    records = sql_cursos.fetchall()
    print(records)

with sqlite3.connect(DB_NAME) as sqlite_con:
    sql_req = "SELECT * FROM courses WHERE reviews_qty >= 100"
    sql_cursos = sqlite_con.execute(sql_req)
    # for record in sql_cursos:
    # print(record)
    # print(record[2])
    records = sql_cursos.fetchall()
    print(records)


# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_con:
#     sqlite_req = """CREATE TABLE IF NOT EXISTS courses(
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     students_qty integer,
#     reviews_qty integer
#     );"""
#     sqlite_con.execute(sqlite_req)

# Add Records to the course table
# courses = [
#     (29, "Python Course by BS", 200, 45),
#     (61, "Docker Course by BS", 570, 100),
#     (46, "Git&GitHub Course by BS", 450, 130),
#     (81, "Django Course by BS", 150, 30)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_con:
#     sql_req = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     for course in courses:
#         sqlite_con.execute(sql_req, course)
#     sqlite_con.commit()
