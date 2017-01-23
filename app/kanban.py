import sqlite3 as lite

# creates db - kanban.db if doens't exist
connect = lite.connect('kanban.db')
cursor = connect.cursor()

# create tasks table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT NOT NULL, status INT NOT NULL, start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, doing_time TEXT, end_time TEXT)")

def add_task(task_name, status_code):#to-do
    # test with dummy data
    cursor.execute("INSERT INTO tasks(task_name, status) VALUES(?, ?)", (task_name, status_code))
    # persist changes
    connect.commit()
    # close db connection
    connect.close()

# generic function to move tasks from todo state to doing
def move_todo_to_doing(status_code, doing_time, task_id):
    # moves dormant task to doing
    cursor.execute("UPDATE tasks SET status = ?, doing_time = ? WHERE id = ?", (status_code, doing_time, task_id))
    # persist changes
    connect.commit()

# function to to move task from doing state to done(complete)
def move_doing_to_done(status_code, completion_time, task_id):
    # moves task to complete
    cursor.execute("UPDATE tasks SET status = ?, end_time = ? WHERE id = ?", (status_code, completion_time, task_id))
    connect.commit()

# function listing all dormant tasks - not yet began
def list_to_do():
    # lists only dormant tasks
    cursor.execute("SELECT * FROM tasks WHERE status = 1")
    all_to_do = cursor.fetchall()
    # returns a set
    return all_to_do
