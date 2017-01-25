import sqlite3 as lite
from kanban import add_task, move_todo_to_doing, move_doing_to_done, list_to_do, list_doing, list_done, list_all_tasks

# creates db - kanban.db if doens't exist
connect = lite.connect('kanban.db')
cursor = connect.cursor()

def check_if_card_exists(task_id):
    # searches record of id = task_id
    cursor.execute("SELECT * FROM tasks WHERE id = ?", ([task_id]))
    result = cursor.fetchall()
    return (len(result) != 0)#returns boolean - True if list contains a fetched record

def move_card_from_todo_to_doing(task_id):
    if check_if_card_exists(task_id) == True:
        move_todo_to_doing(task_id)
        print( "The task of id {0} was successfully moved to DOING state.".format(task_id))
    else:
        return "The task of id {0} doesnt exist. Type *list_doing* to list all task in TODO state.".format(task_id)
