import sqlite3 as lite
from kanban import add_task, move_todo_to_doing, move_doing_to_done, list_to_do, list_doing, list_done, list_all_tasks

# creates db - kanban.db if doens't exist
connect = lite.connect('kanban.db')
cursor = connect.cursor()

def check_if_card_exists(task_id):
    # searches record of id = task_id
    cursor.execute("SELECT * FROM tasks WHERE id = ?", ([task_id]))
    result = cursor.fetchall()
    return result#returns fetched record

def move_card_to_done(task_id):
    if len(check_if_card_exists(task_id)) == 1:
        if check_if_card_exists(task_id)[0][2] == 1:
            # check if task is in to-do state, if so reject move
            print("Cannot move task from TODO to DONE directly. Move to DOING state first.")
        elif check_if_card_exists(task_id)[0][2] == 3:
            # cannot move tassk from done to done
            print("Cannot move task from TODO to DONE directly. Move to DOING state first.")
        elif check_if_card_exists(task_id)[0][2] == 2:
            # move if status is doing
            move_doing_to_done(task_id)
            print("Moved task ** {0} ** to DONE state.".format((check_if_card_exists(task_id)[0][1]).upper()))

def move_task_to_doing(task_id):
    # if record with that ID is foind
    if len(check_if_card_exists(task_id)) == 1:
        if check_if_card_exists(task_id)[0][2] == 2:
            # check if task is in doing state i.e. rejects move for same states
            print("Cannot move task from DOING back to DOING directly.")#should only move to done state
        elif check_if_card_exists(task_id)[0][2] == 1:
            # accept move to DOING state for task in TODO state
            move_todo_to_doing(task_id)
            print( "The task named ** {0} ** was successfully moved to DOING state.".format((check_if_card_exists(task_id)[0][1]).upper()))
    else:
        print("The task of id {0} doesnt exist. Type *list_doing* to list all task in TODO state.".format(task_id))
