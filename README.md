To-Do List Application
Description
A simple and intuitive To-Do List application built using Python's tkinter module. This GUI-based application allows users to add, complete, and manage their daily tasks efficiently.
Features

✅ Add new tasks with a clean text input interface
✅ Mark tasks as complete by clicking the radio button/checkbox
✅ Automatic repositioning of remaining tasks after completion
✅ Simple and user-friendly graphical interface
✅ Real-time task management

Requirements

Python 3.x
tkinter (comes pre-installed with Python)

Installation

Clone this repository:
bashgit clone https://github.com/yourusername/todo-list.git
cd todo-list

Run the application:
bash > python todo_app.py


How to Use

Click the "+ Add Task" button
Type your task in the text field that appears
Press Enter or click outside the text field to add the task
Click the radio button/checkbox next to a task to mark it as complete
Completed tasks are automatically removed from the list

Code Structure
Main Functions:

create_root(): Initializes the main window with all configurations
create_button(): Creates the '+ Add Task' button interface
create_Entry(): Generates a text input field for new tasks
add_Task(task_text): Adds new tasks to the task list
complete_Task(): Removes completed tasks from the list
reposition_Tasks(): Repositions remaining tasks after deletion

Author 
Dharani - Dharani373
