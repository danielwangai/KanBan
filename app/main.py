#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    my_program todo <task_name>
    my_program doing <task_id>
    my_program done <task_id>
    my_program list todo
    my_program list_doing
    my_program list_done
    my_program status
    my_program (-i | --interactive)
    my_program (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from db_kanban import add_task, move_todo_to_doing, move_doing_to_done, list_to_do, list_doing, list_done, list_all_tasks
from interactive import move_card_to_done, move_task_to_doing


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class KanBan(cmd.Cmd):

    def intro():
        print('------------------------------------------------------------------------------')
        print('------------------------------------------------------------------------------')
        print('                     _______')
        print('                        |       /\     _____  |   /')
        print('                        |      /  \    |____  |__/')
        print('                        |     /____\    ____| |  \ ')
        print('                        |    /      \         |   \ ')
        print('** A simple Command Line application to add, display tasks in all stages, and ')
        print('shifts them from one stage to another.**')
        print('------------------------------------------------------------------------------')
        # display list of commands here
        print("                     LIST OF COMMANDS       ")
        print("         type - todo <name of task> - to add a task.     ")
        print("         type - list_doing - to display all tasks in DOING state.        ")
        print("         type - list_done - to display all tasks in DONE state.      ")
        print("         type - list todo - to display all tasks in TODO state.      ")
        print("         type - list_all - to display all tasks in TODO state.      ")
        print("         type - doing <id of task> - to move task from TODO state to DOING state.        ")
        print("         type - done <id of task> - to move task from DOING state to DONE state.     ")
        print('------------------------------------------------------------------------------')


    # intro = 'Welcome, to KanBan Task Manager' \
    #     + ' (type help for a list of commands.)'
    intro = intro()
    prompt = '(KanBan) '
    file = None

    @docopt_cmd
    def do_todo(self, args):
        """Usage: todo <args>..."""
        task_name = " ".join(args['<args>'])
        add_task(task_name)
        print('The task {0} was successfully added.'.format(task_name))

    @docopt_cmd
    def do_doing(self, arg):
        """Usage: doing <task_id>"""

        task_id = arg['<task_id>']
        move_task_to_doing(task_id)

    @docopt_cmd
    def do_done(self, arg):
        """Usage: done <task_id>"""

        task_id = arg['<task_id>']
        move_card_to_done(task_id)

    @docopt_cmd
    def do_list(self, arg):
        """Usage: list todo"""
        print('---------------------------------------------------------------')
        print('-----------------------List of All TODOs-----------------------')
        print('---------------------------------------------------------------')
        print('---ID---|---------Task Description---------|---Start Date------')
        print('---------------------------------------------------------------')
        todo = list_to_do()
        for i in todo:
            print('   {0}   |         {1}         |      {2}      '.format(i[0], i[1], i[3]))
        print(todo)

    @docopt_cmd
    def do_list_doing(self, arg):
        """Usage: list_doing"""
        print('---------------------------------------------------------------')
        print('------------------List of All Tasks inprogress-----------------')
        print('---------------------------------------------------------------')
        print('---ID---|---------Task Description---------|---Start Date------')
        print('---------------------------------------------------------------')
        doing = list_doing() #a list of sets from querying
        for i in doing:
            print('   {0}   |         {1}         |      {2}      '.format(i[0], i[1], i[3]))

    @docopt_cmd
    def do_list_done(self, arg):
        """Usage: list_done"""
        print('---------------------------------------------------------------')
        print('-----------------------List of All Completed projects----------')
        print('---------------------------------------------------------------')
        print('---ID---|---------Task Description---------|---Start Date------')
        print('---------------------------------------------------------------')
        done = list_done() #a list of sets from querying
        for i in done:
            print('   {0}   |         {1}         |      {2}      '.format(i[0], i[1], i[3]))

    @docopt_cmd
    def do_list_all(self, arg):
        """Usage: list_done"""
        print('---------------------------------------------------------------')
        print('-----------------------List of All Completed projects----------')
        print('---------------------------------------------------------------')
        print('---ID---|---------Task Description---------|---Start Date------')
        print('---------------------------------------------------------------')
        all_tasks = list_all_tasks() #a list of sets from querying
        # for i in doing:
        #     print('   {0}   |         {1}         |      {2}      '.format(i[0], i[1], i[3]))
        todo = []
        doing = []
        done = []
        for i in all_tasks:
            if i[2] == 1:
                todo.append(i)
            elif i[2] == 2:
                doing.append(i)
            elif i[2] == 3:
                done.append(i)

        print("----------------------Tasks in TODO----------------------------\n\n")
        for i in todo:
            print("{0}".format(i[1]))

        print("----------------------Tasks in Progress----------------------------\n\n")
        for i in doing:
            print("{0}".format(i[1]))

        print("----------------------Tasks in Complete----------------------------\n\n")
        for i in done:
            print("{0}".format(i[1]))


    @docopt_cmd
    def do_status(self, arg):
        """Usage: status"""
        print("Tasks have 3 states:-")
        print("     *TODO - accessed by number 1")
        print("     *DOING - accessed by number 2")
        print("     *DONE - accessed by number 3")

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    KanBan().cmdloop()

print(opt)
