from datetime import datetime
import tkinter as tk
from tkinter import ttk


class NavBar(ttk.Frame):
    def __init__(self, master, display):
        super().__init__()
        self.nav_frame = ttk.Frame(master)
        self.nav_frame.grid(row=0, column=0)
        self.display = display
        self.button_task_to_do = ttk.Button(
            self.nav_frame, text="Task", command=lambda: app.open_task())
        self.button_task_complete = ttk.Button(
            self.nav_frame, text="Complete", command=lambda: app.open_complete())
        self.button_task_statistic = ttk.Button(self.nav_frame, text="Statistic")
        self.button_task_to_do.grid(row=0, column=0)
        self.button_task_complete.grid(row=0, column=1)
        self.button_task_statistic.grid(row=0, column=2)


class Statistic(ttk.Frame):
    def __init__(self, master, file):
        super().__init__()
        self.data_sel = ttk.Combobox(self.frame, width=27)
        self.frame = ttk.Frame(master, borderwidth=5, padding=1)
        self.button_next = ttk.Button(self.frame, text=">", command=lambda: self.next_fn())
        self.button_back = ttk.Button(self.frame, text="<", command=lambda: self.back_fn())


class Display(ttk.Frame):
    def __init__(self, master, file):
        super().__init__()
        self.file = file
        self.frame = ttk.Frame(master, borderwidth=5, padding=1)
        self.task_box = tk.Listbox(self.frame, bd=3, cursor='hand2', height=15, width=40,
                                   activestyle='none', relief='sunken', bg='grey', font=(
                                       "Ariel", 12))
        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical', width=10)
        self.scrollbar.grid(row=3, column=4, sticky='ns')

        self.taskbox_item_load(self.task_box, self.file)
        self.task_box.grid(column=3, row=3)
        self.frame.grid(column=1, row=1)
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
        self.display = Display(self.my_Frame, self.file)
        self.option = Option(self.my_Frame, self.display)
        self.nav = NavBar(self.my_Frame, self.display)
        self.nav.grid(column=0, row=0)
        self.display.grid(column=0, row=1)
        self.option.grid(column=1, row=2)
        self.my_Frame.grid(column=0, row=0)

    def open_task(self):
        self.display = Display(self.my_Frame, "task.txt")

    def open_complete(self):
        # nie podoba mi się
        self.option.save_change()
        self.display = Display(self.my_Frame, "complete.txt")

    def open_statistic(self):
        self.option.save_change()
        self.display = Statistic()


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


class Option(ttk.Frame):
    def __init__(self, master, dis, but_pad=5):
        super().__init__()
        self.master = master
        self.dis = dis
        self.option_frame = ttk.Frame(master, padding=30)
        self.option_frame.grid(column=2)
        self.button_add = ttk.Button(self.option_frame, text="ADD",
                                     padding=but_pad, command=lambda: self.addTask())
        self.button_del = ttk.Button(self.option_frame, text="DELETE",
                                     padding=but_pad, command=lambda: self.dis.task_box.delete("anchor"))
        self.button_edit = ttk.Button(self.option_frame, text="EDIT",
                                      padding=but_pad, command=lambda: self.eddTask())
        self.button_clear_all = ttk.Button(
            self.option_frame, text="CLEAR ALL", padding=but_pad, command=lambda: self.dis.task_box.delete(0, "end"))
        self.button_save = ttk.Button(self.option_frame, text="SAVE",
                                      padding=but_pad, command=lambda: self.save_change())
        self.button_done = ttk.Button(self.option_frame, text="DONE",
                                      padding=but_pad, command=lambda: self.done_task())
        self.button_edit.grid(column=2, row=0, pady=5)
        self.button_del.grid(column=2, row=1, pady=5)
        self.button_add.grid(column=2, row=2, pady=5)
        self.button_clear_all.grid(column=2, row=3, pady=5)
        self.button_save.grid(column=2, row=4, pady=5)
        self.button_done.grid(column=2, row=5, pady=5)
        self.option_frame.grid(sticky='nesw')

    def addTask(self):
        sm_win(self.dis.task_box, 0, entry_text="", i='end', title="Add Task")

    def eddTask(self):
        sm_win(self.dis.task_box, 1, entry_text=self.dis.task_box.get("anchor"),
               i=self.dis.task_box.curselection()[0], title="Edit Task")

    def save_change(self):
        ln = self.dis.task_box.size()
        i = 0
        with open("task.txt", "w+") as file:
            while i < ln:
                file.write(self.dis.task_box.get(i)+'\n')
                i += 1

    def done_task(self):
        task = self.dis.task_box.get("anchor")
        with open("complete.txt", "a+") as file:
            file.write(task+"\n")
        self.dis.task_box.delete("anchor")


root = tk.Tk()
ttk.Style().configure("TButton", relief='sunken', background='black')
root.title("To do")
root.geometry("600x350")
app = mn_win(root, "task.txt")
app.grid()
root.mainloop()
