from tkinter import *
import psycopg2
from tkinter import messagebox
from PIL import ImageTk
from function_ import resize_custom, get_monitor,get_geometry


class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        get_geometry(self.root)
        get_mon = get_monitor()
        self.root.bind('<Return>', self.login)
        # self.root.geometry("1200x920+0+0")

        self.bg_icon = ImageTk.PhotoImage(file = "template/img/main_bg.jpg")
        self.user_icon = ImageTk.PhotoImage(resize_custom('template/img/login.png', 40, 40))
        self.pass_icon = ImageTk.PhotoImage(resize_custom('template/img/padlock.png', 44, 44))
        self.logo_icon = ImageTk.PhotoImage(resize_custom('template/img/logo.png', 150, 150))

        self.name_ = StringVar()
        self.pass_ = StringVar()

        # bg_lbl = Label(self.root, image = self.bg_icon).pack() #Показ main_bg
        bg_lbl = Label(self.root, image = self.bg_icon).pack() #Показ main_bg

        title = Label(self.root, text = "Добро пожаловать!", font = ("Times New Roman", 40 ), bg = "#444345", fg = "white", bd = 10)
        title.place(x = 0, y = 0, relwidth = 1)

        Login_Frame = Frame(self.root, width = 1000)
        Login_Frame.config(bg = "white")
        # Login_Frame.pack(fill=None, expand=False)
        x_width = get_mon[0]
        x_heigth = get_mon[1]
        Login_Frame.place(relx=.5, rely=.45, anchor="c")
        # Login_Frame.place(x = x_width/2 - 290, rely = 0.28)
        Logolbl = Label(Login_Frame, image = self.logo_icon, bd = 5, bg = "white").grid(row = 0, columnspan = 2, pady = 20)

        # lbluser = Label(Login_Frame, text = "Логин", image = self.user_icon, compound = LEFT, font = ("Times New Roman", 16), bg = "white").grid(row = 1, column = 0, padx = 20, pady = 10)
        lbluser = Label(Login_Frame, text = " Логин ", image = self.user_icon, compound = LEFT, font = ("Times New Roman", 16), bg = "white").grid(row = 1, column = 0, padx = 20, pady = 10,sticky = "w")
        txtuser = Entry(Login_Frame, textvariable = self.name_, bd = 2, font = ("", 15))
        txtuser.grid(row = 1, column = 1, padx = 20, sticky = "w")
        txtuser.focus_set()

        lblpass = Label(Login_Frame, text = " Пароль", image = self.pass_icon, compound = LEFT, font = ("times new roman", 16), bg = "white").grid(row = 2, column = 0, padx = 20, pady = 10,sticky = "w")
        txtpass = Entry(Login_Frame, show = '*', textvariable = self.pass_, bd = 2, font = ("", 15))
        txtpass.grid(row=2, column=1, padx=20, sticky = "w")

        btn_log = Button(Login_Frame, text = "Войти", command = self.login, width = 15, font = ("Times New Roman", 14, "bold"), bg = "#444345", fg = "white")
        btn_log.grid(row = 3, columnspan = 2, pady = 10 )

        def tap_login(event):
            self.login()
            txtpass.delete(0, END)
        txtpass.bind('<Return>', tap_login)

    # def login(self):
    #     if self.name_.get() == "" or self.pass_.get() == "":
    #         messagebox.showerror("Error", "Заполните форму входа!")
    #     elif psycopg2.connect(dbname="stm", user=str(self.name_.get().lower()), password=str(self.pass_.get()),
    #                           host="localhost"):
    #         # messagebox.showinfo("Successfull", f"Добро пожаловать {self.name_.get()}")
    #         self.root.destroy()
    #         import student
    #         student.Student()
    #     else:
    #         messagebox.showerror("ErrorLog", "Логин или пароль неправильный!")
    def login(self):
        if self.name_.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "Заполните форму входа!")
        elif psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost"):
            # messagebox.showinfo("Successfull", f"Добро пожаловать {self.name_.get()}")
            self.root.destroy()
            import student
            student.Student()
        else:
            messagebox.showerror("ErrorLog", "Логин или пароль неправильный!")
root = Tk()
# root.overrideredirect(True)
obj = Login_System(root)
root.mainloop()