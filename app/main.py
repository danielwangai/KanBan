#!/usr/bin/env python
"""
This example uses docopt with the built in cmd module to demonstrate an
interactive command application.

Usage:
    my_program todo <task_name>
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
from kanban import add_task, move_todo_to_doing, move_doing_to_done, list_to_do, list_doing, list_done, list_all_tasks


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
    intro = 'Welcome, to KanBan Task Manager' \
        + ' (type help for a list of commands.)'
    prompt = '(KanBan) '
    file = None

    @docopt_cmd
    def do_todo(self, arg):
        """Usage: todo <task_name>"""
        task_name = arg['<task_name>']
        add_task(task_name)
        print('The task {0} was successfully added.'.format(task_name))

    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]

Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    KanBan().cmdloop()

print(opt)
