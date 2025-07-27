#to do a To Do List using tkinter
import tkinter as tk

tasks = [] #list of tasks
task_position = 80 #starting posiotion for the list

def reposition_Tasks():
    #to reposition the remaining tasks
    global task_position
    current_position = 100
    for task_Widget,task_border,task_text in tasks:
        task_border.place(x=45,y=current_position-5,width = 960,height = 60)
        task_Widget.place(x = 50,y = current_position,width = 950,height = 50)
        current_position += 60

def complete_Task(task_Widget,task_border,task_text):
    #to print the added task in the console
    print(f" Task Completed : {task_text}")
    task_Widget.destroy()
    task_border.destroy()

    #remove from task list
    global tasks
    tasks = [(w,b,t) for w,b,t in tasks if w != task_Widget]
    reposition_Tasks()

def add_Task(task_text):
    global task_position,tasks

    if(len(tasks) == 0):
        task_position = 80

    #creating border
    task_border = tk.Frame(root,bg="gray25",highlightthickness=0)
    task_border.place(x=45,y = task_position -5,width=960,height=60)

    #create radio_button for task
    task_Widget = tk.Radiobutton(root,
                                text = f"  {task_text}",
                                font=("Times New Roman",18),
                                bg="white",
                                fg="black",
                                relief="flat",
                                bd=0,
                                anchor="w",
                                indicatoron=True,
                                selectcolor="bisque")
    
    task_Widget.place(x=50,y=task_position,width=950,height=50)

    #configure the radio button to complete task when it is clicked
    task_Widget.config(command=lambda : complete_Task(task_Widget,task_border,task_text))

    #to append the tasks
    tasks.append((task_Widget,task_border,task_text))

    #move position
    task_position+=70

def create_Entry(root,btn,border):
    #destroy the buttons
    btn.destroy()
    border.destroy()

    #create entry with border
    entry_border = tk.Frame(root,bg="gray25",highlightthickness=0)
    entry_border.place(x=45,y=635,width=960,height=60)

    entry = tk.Entry(root,
                    font=("Times New Roman",20),
                    bg="white",
                    fg="black",
                    insertbackground="black",
                    relief="flat")
    entry.place(x=60,y=640,width=930,height=50)

    def finish_entry(event=None):
        task_text = entry.get()
        if(task_text.strip()):
            print(f"Task added {task_text}")
            add_Task(task_text)
        entry.destroy()
        entry_border.destroy()
        create_Button(root)

    entry.bind('<Return>',finish_entry)
    entry.bind('<FocusOut>',finish_entry)

def create_Button(root):
    border = tk.Frame(root, bg="gray25", highlightthickness=0)
    border.place(x=45, y=635, width=960, height=60) 
    btn = tk.Button(root,
                    text="+ Add Task",
                    font=("Times New Roman",20,"bold"),
                    width="20",
                    height="1",
                    padx = 10,
                    pady=20,
                    bd=0,
                    anchor="w",)
    btn.place(x=50,y=640,width=950,height=50)
    btn.config(command=lambda:create_Entry(root,btn,border))

def create_root(): #for creating the root window
    global root
    root = tk.Tk()
    root.title("To Do List") #sets the title of the window
    root.geometry("800x600") #sets the geometry of the window
    label = tk.Label(root,text="To Do List",bg="lavender blush",fg="black",font=("Times New Roman",30,"bold")) #sets the label
    label.pack()
    root.config(bg="lavender blush")
    create_Button(root)
    root.mainloop()

create_root()
