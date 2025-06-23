import tkinter as tk
from tkinter import messagebox

todolist = []

def add_task():
    task = task_entry.get()
    if task:
        todolist.append(task)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def update_list():
    listbox.delete(0, tk.END)
    for task in todolist:
        listbox.insert(tk.END, task)

def remove_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        task = todolist.pop(index)
        update_list()
        messagebox.showinfo("Removed", f"Task '{task}' removed")
    else:
        messagebox.showwarning("Warning", "Please select a task to remove")

# Main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("300x400")

# Task Entry
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=5)

# Task List
listbox = tk.Listbox(root, width=35, height=15)
listbox.pack(pady=10)

# Run App
root.mainloop()
