from datetime import datetime
import tkinter as tk
from tkinter import ttk


class Display(ttk.Frame):
    def __init__(self, master, file):
        super().__init__()
        self.file = file
        self.frame = ttk.Frame(master, borderwidth=5, padding=20)
        self.task_box = tk.Listbox(self.frame, bd=3, cursor='hand2', height=15, width=40,
                                   activestyle='none', relief='sunken', bg='grey', font=(
                                       "Ariel", 12))
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical', width=10)
        self.scrollbar.grid(row=3, column=4, sticky='ns')

        self.taskbox_item_load(self.task_box, self.file)
        self.task_box.grid(column=3, row=3)
        self.frame.grid(column=0, row=0)
        self.task_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_box.yview)

    def taskbox_item_load(self, t_box, file):
        with open(file, "r") as f:
            for item in f:
                item = item.replace("\n", "")
                t_box.insert("end", item)


class mn_win(ttk.Frame):
    def __init__(self, master, file):
        super().__init__()
        self.file = file
        self.my_Frame = ttk.Frame(master)
        self.my_Frame.pack()
        self.display = Display(self.my_Frame, self.file)
        self.display.pack()


class sm_win():
    def __init__(self, my_listbox, mode, i, entry_text, title):
        self.win = tk.Tk()
        self.win.geometry("230x80")
        self.win.title(title)
        self.frame = ttk.Frame(self.win)
        self.entry = ttk.Entry(self.frame)
        ttk.Style().configure("TButton", relief='sunken', background='black')
        self.entry_text = entry_text
        self.entry.insert('end', self.entry_text)
        self.my_listbox = my_listbox
        self.i = i
        self.mode = mode
        self.ok_bt = ttk.Button(self.frame, text="OK",
                                command=lambda: acceptTask(task=self.entry.get(), li_box=self.my_listbox, ind=i, edi=mode))
        self.cl_bt = ttk.Button(self.frame, text="Cancel", command=lambda: self.win.destroy())
        self.frame.grid()
        self.entry.grid(row=0, columnspan=2, padx=10, pady=5, sticky='ew')
        self.cl_bt.grid(column=0, row=1, padx=20, pady=10)
        self.ok_bt.grid(column=1, row=1, padx=20, pady=10)

        def acceptTask(task, li_box, ind='end', edi=0):
            if edi == 1:
                li_box.delete(ind)
            li_box.insert(ind, task)
            self.win.destroy()

# self.fr_button = ttk.Frame(self.main_frame, padding=30)
# self.fr_button.grid(column=2, row=0)
# self.button_add = ttk.Button(self.fr_button, text="ADD", padding=5, command=addTask)
# self.button_del = ttk.Button(self.fr_button, text="DELETE", padding=5,
#                         command=lambda: self.task_box.delete("anchor"))
# self.button_edit = ttk.Button(self.fr_button, text="EDIT", padding=5, command=eddTask)
# self.button_clear_all = ttk.Button(self.fr_button, text="CLEAR ALL", padding=5,
#                               command=lambda: task_box.delete(0, "end"))
# self.button_save = ttk.Button(self.fr_button, text="SAVE", padding=5, command=save_change)
# self.button_done = ttk.Button(sef.fr_button, text="DONE", padding=5, command=done_task)
# self.button_edit.grid(column=2, row=0, pady=5)
# self.button_del.grid(column=2, row=1, pady=5)
# self.button_add.grid(column=2, row=2, pady=5)
# self.button_clear_all.grid(column=2, row=3, pady=5)
# self.button_save.grid(column=2, row=4, pady=5)
# self.button_done.grid(column=2, row=5, pady=5)
# self.frame.grid(sticky='nesw')
#
# def addTask():
#     sm_win(task_box, 0, entry_text="", i='end', title="Add Task")
# def eddTask():
#     sm_win(task_box, 1, entry_text=task_box.get("anchor"),
#            i=task_box.curselection()[0], title="Edit Task")
#
#
# def save_change():
#     ln = task_box.size()
#     i = 0
#     with open("task.txt", "w+") as file:
#         while i < ln:
#             file.write(task_box.get(i)+'\n')
#             i += 1
# def done_task():
#     task = task_box.get("anchor")
#     with open("complete.txt", "a+") as file:
#         file.write(task+"\n")
#
#     task_box.delete("anchor")


root = tk.Tk()
ttk.Style().configure("TButton", relief='sunken', background='black')
root.title("To do")
root.geometry("600x350")
mn_win(root, "task.txt")
root.mainloop()
