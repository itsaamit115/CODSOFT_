import tkinter as tk
from tkinter import messagebox
def addTask():
    task = taskEntry.get()
    if task != "":
        taskListbox.insert(tk.END, task)
        taskEntry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty")
def deleteTask():
    try:
        selected = taskListbox.curselection()[0]
        taskListbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task")
def updateTask():
    try:
        selected = taskListbox.curselection()[0]
        newTask = taskEntry.get()
        if newTask != "":
            taskListbox.delete(selected)
            taskListbox.insert(selected, newTask)
            taskEntry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty")
    except:
        messagebox.showwarning("Warning", "Select a task")
def clearAll():
    taskListbox.delete(0, tk.END)
root = tk.Tk()
root.title("To Do List")
root.geometry("400x400")
root.config(bg="lightblue")
titleLabel = tk.Label(root, text="My To Do List", font=("Arial", 18, "bold"), bg="lightblue")
titleLabel.pack(pady=10)
taskEntry = tk.Entry(root, width=40, font=("Arial", 12))
taskEntry.pack(pady=10)
btnFrame = tk.Frame(root, bg="lightblue")
btnFrame.pack(pady=5)
addBtn = tk.Button(btnFrame, text="Add Task", width=12, command=addTask)
addBtn.grid(row=0, column=0, padx=5)
updateBtn = tk.Button(btnFrame, text="Update Task", width=12, command=updateTask)
updateBtn.grid(row=0, column=1, padx=5)
deleteBtn = tk.Button(btnFrame, text="Delete Task", width=12, command=deleteTask)
deleteBtn.grid(row=1, column=0, padx=5, pady=5)
clearBtn = tk.Button(btnFrame, text="Clear All", width=12, command=clearAll)
clearBtn.grid(row=1, column=1, padx=5, pady=5)
taskListbox = tk.Listbox(root, width=50, height=10, font=("Arial", 12))
taskListbox.pack(pady=10)
root.mainloop()
