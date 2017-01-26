# KanBan

## Intro

This is a Command Line (CLI) application that manages tasks by shifting tasks between 3 states:-
	- TODO
	- DOING
	- DONE

## Installation and Setup

1. Python Installation
	- Download Python to your computer using the links below.
	    * Windows - [Python for windows](https://www.python.org/downloads/windows/)
	    * Mac OS - [Python for MAC](https://www.python.org/downloads/mac-osx/)
	    * Other distributions - [Python for windows](https://www.python.org/downloads/)
	- if you've installed python on your machine, when you type ```python``` on command line it responds with a python prompt on the shell.
2. Navigate to your preferred directory using terminal.
3. Clone the repository into it by typing ```git clone https://github.com/danielwangai/KanBan```
4. Install required modules
	- On the root of the project, type ```pip install -r requirements.txt``` to install the python dependencies.
5. type ```python app/main.py -i``` to run the application in interactive mode.
6. List of commands:-
	- ```todo <task description>``` - Adds a task
	- ```list_todo``` - lists tasks in the TODO state
	- ```list_doing``` - lists tasks in the DOING state
	- ```list_done``` - lists tasks in the DONE state
	- ```list_all``` - tabulates all tasks according to their states.
	-  ```doing <task_id>``` - moves task from TODO to DOING state.
	-  ```done <task_id>``` - moves task from DOING to DONE state.
