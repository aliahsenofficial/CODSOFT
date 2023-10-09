import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def on_entry_click(event):
    if entry.get() == "Write your task":
        entry.delete(0, tk.END)
        entry.config(fg='black')

def on_entry_leave(event):
    if entry.get() == "":
        entry.insert(0, "Write your task")
        entry.config(fg='grey')

def add_task(event=None):
    task = entry.get()
    if task and task != "Write your task":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        entry.insert(0, "Write your task")
        entry.config(fg='grey')
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_list():
    listbox.delete(0, tk.END)

def save_list():
    tasks = listbox.get(0, tk.END)
    with open("todo.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")
    messagebox.showinfo("Info", "To-Do List saved successfully!")

def load_list():
    try:
        with open("todo.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        messagebox.showwarning("Warning", "No saved To-Do List found.")

# Create the main application window
root = tk.Tk()
root.title("To-Do List")

# Create a styled frame
frame = ttk.Frame(root, padding=10)
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create input field with placeholder using a regular tk.Entry widget
entry = tk.Entry(frame, width=40)
entry.insert(0, "Write your task")
entry.grid(row=0, column=0, columnspan=2, pady=5)

entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_entry_leave)
entry.bind('<Return>', add_task)  # Bind the Return key to add_task

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=2, pady=5, padx=(0, 5))

delete_button = ttk.Button(frame, text="Delete Task", command=delete_task)
delete_button.grid(row=0, column=3, pady=5, padx=5)

clear_button = ttk.Button(frame, text="Clear List", command=clear_list)
clear_button.grid(row=0, column=4, pady=5, padx=5)

save_button = ttk.Button(frame, text="Save List", command=save_list)
save_button.grid(row=0, column=5, pady=5)

load_button = ttk.Button(frame, text="Load List", command=load_list)
load_button.grid(row=0, column=6, pady=5)

# Create the task list with scrollbar and border
listbox_frame = ttk.Frame(frame)
listbox_frame.grid(row=1, column=0, columnspan=7, sticky=(tk.W, tk.E, tk.N, tk.S))
listbox_border = ttk.Frame(listbox_frame, borderwidth=1, relief="solid")
listbox_border.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)
listbox_scrollbar = ttk.Scrollbar(listbox_border, orient=tk.VERTICAL)
listbox = tk.Listbox(listbox_border, width=100, selectmode=tk.SINGLE, yscrollcommand=listbox_scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)
listbox_scrollbar.config(command=listbox.yview)
listbox_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Start the Tkinter main loop
root.mainloop()
