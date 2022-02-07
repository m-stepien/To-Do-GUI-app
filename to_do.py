import tkinter as tk
from tkinter import ttk


class App():
    #core of app
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("To do")
        ttk.Style().configure("TButton", relief='sunken', borderwidth=1)
        mn = mn_win(self.root)
        mn.grid(column=0, row=0)
        self.root.mainloop()


class mn_win(ttk.Frame):
    # main frame where put everything
    def __init__(self, master):
        super().__init__()
        self.display = Display()
        self.option = Option(self.display)
        self.nav = NavBar(self.display)
        self.nav.grid(column=0, row=0, sticky='w', padx=10, pady=5)
        self.display.grid(column=0, row=1)
        self.option.grid(column=1, row=1)


class Option(ttk.Frame):
    #grid of button and every most of functionality of app as method
    def __init__(self, disp, but_pad=10):
        super().__init__()
        self.disp = disp
        self.button_add = ttk.Button(self, text="ADD",
                                     padding=but_pad, command=lambda: disp.addTask())
        self.button_del = ttk.Button(self, text="DELETE",
                                     padding=but_pad, command=lambda: self.disp.task_box.delete("anchor"))
        self.button_edit = ttk.Button(self, text="EDIT",
                                      padding=but_pad, command=lambda: disp.eddTask())
        self.button_clear_all = ttk.Button(
            self, text="CLEAR ALL", padding=but_pad, command=lambda: disp.task_box.delete(0, "end"))
        self.button_save = ttk.Button(self, text="SAVE",
                                      padding=but_pad, command=lambda: disp.save_change())
        self.button_done = ttk.Button(self, text="DONE",
                                      padding=but_pad, command=lambda: disp.done_task())
        self.button_save.grid(column=2, row=0, pady=10, padx=10)
        self.button_done.grid(column=2, row=1, pady=10, padx=10)
        self.button_add.grid(column=2, row=2, pady=10, padx=10)
        self.button_edit.grid(column=2, row=3, pady=10, padx=10)
        self.button_del.grid(column=2, row=4, pady=10, padx=10)
        self.button_clear_all.grid(column=2, row=3, pady=10, padx=10)



class NavBar(ttk.Frame):
    #navigation bar to change what type of task you looking at
    def __init__(self, display):
        super().__init__()
        self.current, self.complete = file_1, file_2
        self.button_task_to_do = ttk.Button(
            self, text="Current", command=lambda: display.open_f(self.current))
        self.button_task_complete = ttk.Button(
            self, text="Complete", command=lambda: display.open_f(self.complete))
        self.button_task_to_do.grid(row=0, column=0)
        self.button_task_complete.grid(row=0, column=1)


class Display(ttk.Frame):
#showing all line of some file can handle changing file
    def __init__(self):
        super().__init__()
        self.configure(borderwidth=5, padding=1)
        self.creating_ls_box(file_1)

    def taskbox_item_load(self, t_box, file):
        with open(file, "r") as f:
            for item in f:
                #need replace in other way \n will be increase after every save
                item = item.replace("\n", "")
                t_box.insert("end", item)

    def creating_ls_box(self, file):
        self.task_box = tk.Listbox(self, bd=3, cursor='hand2', height=15, width=40,
                                   activestyle='none', relief='sunken', bg='grey', font=(
                                       "Ariel", 12))
        self.scrollbar = tk.Scrollbar(self, orient='vertical', width=10)
        self.scrollbar.grid(row=3, column=4, sticky='ns')
        self.taskbox_item_load(self.task_box, file)
        self.task_box.grid(column=3, row=3)
        self.task_box.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_box.yview)

    def open_f(self, f_name):
        self.task_box.forget()
        self.creating_ls_box(f_name)
        def addTask(self):
            sm_win(self.task_box, 0, entry_text="", i='end', title="Add Task")
    def addTask(self):
        sm_win(self.task_box, 0, entry_text="", i='end', title="Add Task")

    def eddTask(self):
        sm_win(self.task_box, 1, entry_text=self.task_box.get("anchor"),
               i=self.task_box.curselection()[0], title="Edit Task")

    def save_change(self):
        ln = self.task_box.size()
        i = 0
        with open(file_1, "w+") as file:
            while i < ln:
                file.write(self.task_box.get(i)+'\n')
                i += 1

    def done_task(self):
        task = self.task_box.get("anchor")
        with open(file_2, "a+") as file:
            file.write(task+"\n")
        self.task_box.delete("anchor")



class sm_win():
#window responsible for adding new task or editing existing one
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


file_1, file_2 = "task.txt", "complete.txt"
app = App()
