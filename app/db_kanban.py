import sqlite3 as lite
from datetime import datetime

# creates db - kanban.db if doens't exist
connect = lite.connect('kanban.db')
cursor = connect.cursor()

# create tasks table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task_name TEXT NOT NULL, status INT NOT NULL, create_task_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP, start_time DATETIME, end_time DATETIME)")

def add_task(task_name):#to-do
    # test with dummy data
    status_code = 1#code for todo state
    cursor.execute("INSERT INTO tasks(task_name, status) VALUES(?, ?)", (task_name, status_code))
    # persist changes
    connect.commit()
    # close db connection
    # connect.close()

# generic function to move tasks from todo state to doing
def move_todo_to_doing(task_id):
    # moves dormant task to doing
    doing_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_code = 2#code for doing state
    cursor.execute("UPDATE tasks SET status = ?, start_time = ? WHERE id = ?", (status_code, doing_time, task_id))
    # persist changes
    connect.commit()

# function to to move task from doing state to done(complete)
def move_doing_to_done(task_id):
    # moves task to complete
    completion_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_code = 3#code for done state
    cursor.execute("UPDATE tasks SET status = ?, end_time = ? WHERE id = ?", (status_code, completion_time, task_id))
    connect.commit()

def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = (?)", ([task_id]))
    connect.commit()

# function listing all dormant tasks - not yet began
def list_to_do():
    # lists only dormant tasks
    cursor.execute("SELECT * FROM tasks WHERE status = 1")
    all_to_do = cursor.fetchall()
    # returns a set
    return all_to_do

# lists only tasks in progress but not yet complete
def list_doing():
    cursor.execute("SELECT * FROM tasks WHERE status = 2")
    all_doing = cursor.fetchall()
    # returns a set
    return all_doing

# lists only completed tasks
def list_done():
    cursor.execute("SELECT * FROM tasks WHERE status = 3")
    all_done = cursor.fetchall()
    # returns a set
    return all_done

# lists all tasks in table
def list_all_tasks():
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    # returns a set
    return all_tasks
