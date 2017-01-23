import sqlite3 as lite

# creates db - kanban.db if doens't exist
connect = lite.connect('kanban.db')
cursor = connect.cursor()

# create tasks table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT NOT NULL, status INT NOT NULL, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# close db connection
connect.close()
