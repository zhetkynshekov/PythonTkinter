from functools import partial
from tkinter import *
from tkinter import ttk
import psycopg2
from tkinter import messagebox
from PIL import ImageTk
from function_ import get_geometry, get_monitor

class Student:
    get_mo = get_monitor()
    width_manage_frame = get_mo[0] * 0.234  # Ширина Manage frame
    height_manage_frame = get_mo[1] * 0.9  # Высота Manage frame
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        get_geometry(self.root)


        self.link = psycopg2.connect(dbname = "stm", user = "postgres", password = "askarova180774", host = "localhost") #пытался подключение сделать одниой переменной, не вышло, не принимает его

        self.bg_icon = ImageTk.PhotoImage(file = "template/img/main_bg.jpg") #общий фон для этого окна
        # bg_lvl = Label(self.root, image = self.bg_icon).pack()
        bg_lvl = Label(self.root, image = self.bg_icon).pack()
        # bg_lvl = Label(self.root, bg = "silver").pack()

#Manage, Detail, Table Frame Backgrounds
        # bg_frame = "#3b4045" #Общий цвет фона для frame-ов
        bg_frame = "#535454" #Общий цвет фона для frame-ов
        # bg_frame = "orange"
        bg_frame_b = "#444345"  # Общий background для BUTTONS
        fg_b = "white"  # Общий цвет текста для BUTTONS

        fg_frame = "white" #Общий цвет текста для frame-ов

        font_all_3 = "" #Стиль текста во всем документе например bold, italic
        font_all_1 = "Times New Roman" #Стиль текста во всем документе например Times New Roman, Courier

        title = Label(self.root, text = "Система управления студентами", font = (font_all_1, 36, font_all_3), bg = "#444345", fg ="white", bd = 10)
        # title.pack(side = TOP, fill = X)
        title.place(x=0, y=0, relwidth=1)
# All variables for db*******************************************************************************************************************
        self.roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()


# Manage Frame*******************************************************************************************************************


        self.Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg= bg_frame)
        self.Manage_Frame.place(x=20, y=90, width=self.width_manage_frame, height=self.height_manage_frame)
# Add Frame on Manage frame------------------------------------------------------------------------------------------------
        self.Add_frame = Frame(self.Manage_Frame, bg=bg_frame)
        self.Add_frame.place(y=70, width=self.width_manage_frame - 8, height=self.height_manage_frame / 4)
        Add_txt = Label(self.Add_frame, text = "Добавить:", bg= bg_frame, fg = fg_frame, font = (font_all_1, 20, font_all_3))
        Add_txt.grid(row=0, column = 0, pady=13, padx=50)
        Add_frame_button = Frame(self.Add_frame, bg=bg_frame)
        Add_frame_button.place(x = self.width_manage_frame/2, y = 5, width = self.width_manage_frame/2-8, height = self.height_manage_frame/4-8)
        add_with_arg = partial(self.show_manage_frame, "add")
        add_student_1 = Button(Add_frame_button, text = "Студента", width = 20, height = 2, bg = bg_frame_b, fg = fg_b, command = add_with_arg,
                               font = (font_all_1, 10, ""))
        add_student_1.grid(row = 0, column = 0, padx = 5, pady = 10)
        update_with_arg = partial(self.show_manage_frame, "update")
        add_student_2 = Button(Add_frame_button, text = "Учителя", width=20, height = 2, bg=bg_frame_b, fg=fg_b, command = update_with_arg,
                               font = (font_all_1, 10, ""))
        add_student_2.grid(row=1, column=0, padx=5, pady=10)
        add_student_3 = Button(Add_frame_button, text = "Персонал", width=20, height = 2, bg=bg_frame_b, fg=fg_b,
                               font = (font_all_1, 10, ""))
        add_student_3.grid(row=2, column=0, padx=5, pady=10)
        add_student_4 = Button(Add_frame_button, text = "Другие", width=20, height = 2, bg=bg_frame_b, fg=fg_b,
                               font = (font_all_1, 10, ""))
        add_student_4.grid(row=3, column=0, padx=5, pady=10)
#Manage mini Frame on Add frame-------------------------------------------------------------------------------------------------------------------------------
        self.Manage_mini_Frame = Frame(self.Manage_Frame, bg = bg_frame)
        self.Manage_mini_Frame.place( y=75, width=self.width_manage_frame-10, height=self.height_manage_frame-100)
        self.Manage_mini_Frame.place_forget()

# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
        m_title = Label(self.Manage_Frame, text = "Панель управления", bd = 4, relief = RIDGE, bg= bg_frame, fg = fg_frame, font = (font_all_1, 25, font_all_3))
        m_title.grid(row = 0, columnspan = 2, pady = 20, padx = 45, ipadx = 40, ipady = 3.5)
        # m_title.grid(relx=.5, rely=.75, anchor="c")
#-------------------------------------------------------------------------------------------------------------------------------
        lbl_rool = Label(self.Manage_mini_Frame, text = "No.", bg= bg_frame, fg = fg_frame, font = (font_all_1, 20, font_all_3))
        lbl_rool.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = "w")

        txt_Roll = Entry(self.Manage_mini_Frame, textvariable = self.roll_No_var, font = (font_all_1, 15, "bold"))
        txt_Roll.grid(row = 1, column = 1, pady = 10, sticky = "w")
#-------------------------------------------------------------------------------------------------------------------------------
        lbl_name = Label(self.Manage_mini_Frame, text="Имя", bg= bg_frame, fg=fg_frame, font = (font_all_1, 20, font_all_3))
        lbl_name.grid(row=2, column=0, padx = 20, pady=20, sticky="w")

        txt_name = Entry(self.Manage_mini_Frame,textvariable = self.name_var, font=(font_all_1, 15, "bold"))
        txt_name.grid(row=2, column=1, pady=10, sticky="w")
#-------------------------------------------------------------------------------------------------------------------------------
        lbl_Email = Label(self.Manage_mini_Frame, text="Email", bg= bg_frame, fg=fg_frame, font=(font_all_1, 20, font_all_3))
        lbl_Email.grid(row=3, column=0, padx = 20, pady=20, sticky="w")

        txt_Email = Entry(self.Manage_mini_Frame,textvariable = self.email_var, font=(font_all_1, 15, "bold"))
        txt_Email.grid(row=3, column=1, pady=10, sticky="w")
# -------------------------------------------------------------------------------------------------------------------------------
        lbl_Gender = Label(self.Manage_mini_Frame, text="Пол", bg= bg_frame, fg=fg_frame, font = (font_all_1, 20, font_all_3))
        lbl_Gender.grid(row=4, column=0, padx = 20, pady=10, sticky="w")

        combo_Gender = ttk.Combobox(self.Manage_mini_Frame,textvariable = self.gender_var, font = (font_all_1, 14, "bold"), width = 17,  state = 'readonly')
        combo_Gender['values'] = ("Мужчина", "Женщина")
        combo_Gender.grid(row = 4, column = 1, pady = 10, sticky="w")
# -------------------------------------------------------------------------------------------------------------------------------
        lbl_Contact = Label(self.Manage_mini_Frame, text="Контакты", bg= bg_frame, fg=fg_frame, font = (font_all_1, 20, font_all_3))
        lbl_Contact.grid(row=5, column=0, padx = 20, pady=20, sticky="w")

        txt_Contact = Entry(self.Manage_mini_Frame,textvariable = self.contact_var, font=(font_all_1, 15, "bold"))
        txt_Contact.grid(row=5, column=1, pady=10, sticky="w")
# -------------------------------------------------------------------------------------------------------------------------------
        lbl_DOB = Label(self.Manage_mini_Frame, text="Дата рождения", bg= bg_frame, fg=fg_frame, font = (font_all_1, 20, font_all_3))
        lbl_DOB.grid(row=6, column=0, padx = 20, pady=20, sticky="w")

        txt_DOB = Entry(self.Manage_mini_Frame,textvariable = self.dob_var, font=(font_all_1, 15, "bold"))
        txt_DOB.grid(row=6, column=1, pady=10, sticky="w")
# -------------------------------------------------------------------------------------------------------------------------------
        lbl_Address = Label(self.Manage_mini_Frame, text="Адрес", bg= bg_frame, fg=fg_frame, font=(font_all_1, 20, font_all_3))
        lbl_Address.grid(row=7, column=0, padx = 20, pady=20, sticky="w")

        self.txt_Address = Text(self.Manage_mini_Frame, width = 20, height = 4, font = (font_all_1, 14, "bold"))
        self.txt_Address.grid(row=7, column=1, pady=10, sticky="w")

        self.AddButton = Button(self.Manage_mini_Frame, text="Добавить", width=35, height=2, bg="#2ea44f", fg=fg_b,
                           command=self.add_students, font = (font_all_1, 11, "bold"))
        # self.AddButton.grid(row=8, columnspan=2, padx=40, pady=15)
        # self.AddButton.grid_forget()

        self.UpdateButton = Button(self.Manage_mini_Frame, text="Обновить", width=35, height=2, bg="#f9826c", fg=fg_b,
                                command=self.update_data, font=(font_all_1, 11, "bold"))
        # self.UpdateButton.grid(row=8, columnspan=2, padx=40, pady=15)
        # self.UpdateButton.grid_forget()

        self.DeleteButton = Button(self.Manage_mini_Frame, text="Удалить", width=35, height=2, bg="red", fg=fg_b,
                                   command=self.delete_data, font=(font_all_1, 11, "bold"))
        # self.UpdateButton.grid(row=9, columnspan=2, padx=40, pady=15)
        # self.UpdateButton.grid_forget()

        self.Back_Button = Button(self.Manage_mini_Frame, text = "Назад", width = 15, height = 2, bg = bg_frame_b, fg = fg_b,
                             command = self.show_manage_frame, font = (font_all_1, 10, "bold"))
        # self.Back_Button.grid(row = 9, column = 0, padx = 0, pady = 10)
        # self.Back_Button.grid_forget()
# Button Frame on Manage frame-------------------------------------------------------------------------------------------------------------------------------
        Button_Frame = Frame(self.Manage_mini_Frame, bd=4, relief=RIDGE, bg="white")
        # Button_Frame.place(x=8, y=680, width=width_manage_frame * 0.912)
        Button_Frame.place(relx=.5, rely=.75, anchor="c")
        Button_Frame.place_forget()

        padx_b = 20 #Общий padx для ADD ,UPDATE ,DELETE , CLEAR BUTTONS



        AddButton1 = Button(Button_Frame, text = "Добавить", width = 15, height = 1, bg = bg_frame_b, fg = fg_b, command = self.add_students).grid(row = 0, column = 0, padx = padx_b, pady = 10)
        UpdateButton = Button(Button_Frame, text = "Обновить", width = 15, height = 1, bg = bg_frame_b, fg = fg_b, command = self.update_data).grid(row = 0, column = 1, padx = padx_b, pady = 10)
        # DeleteButton = Button(Button_Frame, text = "Удалить", width = 15, height = 1, bg = bg_frame_b, fg = fg_b, command = self.delete_data).grid(row = 1, column = 0, padx = padx_b, pady = 10)
        ClearButton = Button(Button_Frame, text = "Очистить", width = 15, height = 1, bg = bg_frame_b, fg = fg_b, command = self.clear).grid(row = 1, column = 1, padx = padx_b, pady = 10)
# Detail Frame*******************************************************************************************************************
        width_detail_frame = self.get_mo[0] * 0.729 #Ширина Detail Frame
        height_detail_frame = self.get_mo[1] * 0.9 #Высота Detail Frame

        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg= bg_frame)
        self.Detail_Frame.place(x=500, y=90, width=width_detail_frame, height=height_detail_frame)
# -------------------------------------------------------------------------------------------------------------------------------
        self.lbl_Search = Label(self.Detail_Frame, text="Поиск по", bg= bg_frame, fg=fg_frame, font=(font_all_1, 20, font_all_3)) #надпись Поиск по
        self.lbl_Search.grid(row=0, column=0, padx = 20, pady=20, sticky="w")
        self.combo_Search = ttk.Combobox(self.Detail_Frame, textvariable = self.search_by, width = 10,
                                         font=("Times New Roman", 13, font_all_3), state='readonly')
        self.combo_Search.bind("<<ComboboxSelected>>", self.TextBoxUpdate) #Забиндил чтобы когда выбирали пол, пропадал label и его заменял combobox с выборкой м или ж
        self.combo_Search['values'] = ("roll_no", "name", "email", "gender", "contact")
        self.combo_Search.grid(row=0, column=1, pady=10, sticky="w")
    # -------------------------------------------------------------------------------------------------------------------------------
        self.combo_gender = ttk.Combobox(self.Detail_Frame, textvariable=self.search_txt, width=10,
                                         font=("Times New Roman", 13, ""), state='readonly')
        # self.combo_gender.bind("<<ComboboxSelected>>", self.TextBoxUpdate)
        self.combo_gender['values'] = ("Мужчина", "Женщина")
        self.combo_gender.grid(row=0, column=2, pady=10, padx=20, sticky="w")
        self.combo_gender.grid_remove() #Сделал невидимым так как он должен выходить только после того как в combo_Search выбирется gender, а реализует это функция self.TextBoxUpdate
        self.txt_Search = Entry(self.Detail_Frame, textvariable = self.search_txt, width = 10, font=(font_all_1, 14, font_all_3))
        self.txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.show_manage_frame_txt = StringVar()
        self.show_manage_frame_txt = "0"

        SearchButton = Button(self.Detail_Frame, text="Поиск", width=10, pady = 5, bg = bg_frame_b, fg = fg_b, command = self.search_data, font=(font_all_1, 14, font_all_3)).grid(row=0, column=3, padx=30, pady=10)
        ShowallButton = Button(self.Detail_Frame, text="Показать все", width=15, pady = 5, padx = 10, bg = bg_frame_b, fg = fg_b, command = self.fetch_data, font=(font_all_1, 14, font_all_3)).grid(row=0, column=4, padx=30, pady=10)
        exit_root = Button(self.Detail_Frame, text="Выйти", width=15, pady = 5, padx = 10, bg = bg_frame_b, fg = fg_b, command = self.exit_root, font=(font_all_1, 14, font_all_3)).grid(row=0, column=5, padx=30, pady=10)
        show_manage_frame = Button(self.Detail_Frame, text = "Скрыть", width=15, pady = 5, padx = 10, bg = bg_frame_b, fg = fg_b, command = self.show_manage_frame, font=(font_all_1, 14, font_all_3)).grid(row=0, column=7, padx=30, pady=10)
# ComboBox for Table Frame*******************************************************************************************************************
        self.change_Table_txt = StringVar()
        self.combo_change_table = ttk.Combobox(self.Detail_Frame, textvariable=self.change_Table_txt, width=10,
                                         font=("Times New Roman", 13, font_all_3), state='disabled')
        # self.combo_change_table.bind("<<ComboboxSelected>>",
        #                        self.Change_Table)  #
        self.combo_change_table['values'] = ("students", "users")
        # self.combo_change_table.current(0)

        self.combo_change_table.grid(row=0, column=6, pady=10, sticky="w")
# Table Frame*******************************************************************************************************************
        self.Table_Frame = Frame(self.Detail_Frame, bd = 4, relief = RIDGE, bg = bg_frame)
        self.Table_Frame.place(x = 10, y = 70, width = width_detail_frame * 0.98, height = height_detail_frame * 0.9)

        self.scroll_x = Scrollbar(self.Table_Frame, orient = HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient = VERTICAL)

        self.Student_table = ttk.Treeview(self.Table_Frame,
                                                  columns=("roll", "name", "email", "gender", "contact", "dob", "address"),
                                                  xscrollcommand=self.scroll_x.set, yscrollcommand=self.scroll_y.set)
        style = ttk.Style(self.root)
        style.configure('Treeview', rowheight=40)  # Высота каждой строки в таблице
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.Student_table.xview)
        self.scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="No.")
        self.Student_table.heading("name", text="Имя")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Пол")
        self.Student_table.heading("contact", text="Контакты")
        self.Student_table.heading("dob", text="Дата рождения")
        self.Student_table.heading("address", text="Адрес")

        self.Student_table.column("roll", width=20)
        self.Student_table.column("name", width=120)
        self.Student_table.column("email", width=130)
        self.Student_table.column("gender", width=50)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=180)
        self.Student_table['show'] = 'headings'
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<Double-Button-1>", self.get_cursor)

        self.fetch_data()
#Показ панели управления*********************************************************************************************************************
    def show_manage_frame(self, Check = ""):
        if Check == "add":
            if self.Manage_mini_Frame.place_info() == {}:
                self.Add_frame.place_forget()
                self.Manage_mini_Frame.place(y=65, width=self.width_manage_frame - 10, height=self.height_manage_frame - 100)
                self.AddButton.grid(row=8, columnspan=2, padx=40, pady=15)
                self.Back_Button.grid(row=9, column=0, padx=0, pady=10)
                self.DeleteButton.grid_forget()
            else:
                self.Manage_mini_Frame.place_forget()
                self.Add_frame.place(y=70, width=self.width_manage_frame - 8, height=self.height_manage_frame / 4)
                self.AddButton.grid_forget()
                self.DeleteButton.grid_forget()
                self.Back_Button.grid_forget()
        elif Check == "update":
            if self.Manage_mini_Frame.place_info() == {}:
                self.Add_frame.place_forget()
                self.Manage_mini_Frame.place(y=65, width=self.width_manage_frame - 10, height=self.height_manage_frame - 100)
                self.UpdateButton.grid(row=8, columnspan=2, padx=40, pady=15)
                self.DeleteButton.grid(row=9, columnspan=2, padx=40, pady=15)
                self.Back_Button.grid(row=10, column=0, padx=0, pady=10)
            else:
                self.Manage_mini_Frame.place_forget()
                self.Add_frame.place(y=70, width=self.width_manage_frame - 8, height=self.height_manage_frame / 4)
                self.UpdateButton.grid_forget()
                self.DeleteButton.grid_forget()
                self.Back_Button.grid_forget()
        else:
            self.Manage_mini_Frame.place_forget()
            self.Add_frame.place(y=70, width=self.width_manage_frame - 8, height=self.height_manage_frame / 4)
            self.AddButton.grid_forget()
            self.UpdateButton.grid_forget()
            self.Back_Button.grid_forget()
# gender bind -------------------------------------------------------------------------------------------------------------------------------
    def TextBoxUpdate(self, event):
        if self.search_by.get() == "gender":
            self.txt_Search.grid_remove()
            self.combo_gender.grid()
        else:
            self.combo_gender.grid_remove()
            self.txt_Search.grid()
# function for buttons -------------------------------------------------------------------------------------------------------------------------------
    def exit_root(self):
        self.root.destroy()
# Connect to db -------------------------------------------------------------------------------------------------------------------------------
    def add_students(self):
        if self.roll_No_var.get() == "" or self.name_var.get() == "":
                messagebox.showerror("Error", "All fields are required!!!")
        else:
                connect = psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost")
                cur = connect.cursor()
                try:
                    removed = self.txt_Address.get('1.0', END).replace("\n", "")
                    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.roll_No_var.get(),
                                                                                      self.name_var.get(),
                                                                                      self.email_var.get(),
                                                                                      self.gender_var.get(),
                                                                                      self.contact_var.get(),
                                                                                      self.dob_var.get(),
                                                                                      removed
                                                                                      ))

                    connect.commit()

                    self.fetch_data()
                    self.clear()

                    connect.close()
                    messagebox.showinfo("Success", "Данные были успешно записаны!")
                except:
                    messagebox.showerror("Error", "Студент с таким номером уже существует!")

# Show data on table from db-------------------------------------------------------------------------------------------------------------------------------
    def fetch_data(self):
        self.txt_Search.delete(0, END)
        self.combo_Search.set("")
        connect = psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost")
        cur = connect.cursor()
        cur.execute("select * from students ORDER BY roll_no ASC")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            connect.commit()
        connect.close()

# Clear all entry for add students-------------------------------------------------------------------------------------------------------------------------------
    def clear(self):
        self.roll_No_var.set(""),
        self.name_var.set(""),
        self.email_var.set(""),
        self.gender_var.set(""),
        self.contact_var.set(""),
        self.dob_var.set(""),
        self.txt_Address.delete('1.0', END)
# get one row which you click then set on blank for add student-------------------------------------------------------------------------------------------------------------------------------
    def get_cursor(self, event):
        self.show_manage_frame("update")
        curosor_row = self.Student_table.focus()
        contents = self.Student_table.item(curosor_row)
        row = contents['values']
        removed = row[6].replace("\n", "")
        print(row)


        self.roll_No_var.set(row[0]),
        self.name_var.set(row[1]),
        self.email_var.set(row[2]),
        self.gender_var.set(row[3]),
        self.contact_var.set(row[4]),
        self.dob_var.set(row[5]),
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert(END, removed)
# Update data on db-------------------------------------------------------------------------------------------------------------------------------
    def update_data(self):
        # connect = self.link
        option = messagebox.askyesno("Update", "Вы хотите обновить этот обьект?")
        if option>0:
            connect = psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost")
            cur = connect.cursor()
            cur.execute(
                "update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s", (
                    self.name_var.get(),
                    self.email_var.get(),
                    self.gender_var.get(),
                    self.contact_var.get(),
                    self.dob_var.get(),
                    self.txt_Address.get('1.0', END),
                    self.roll_No_var.get()
                ))

            connect.commit()

            self.fetch_data()
            self.clear()

            connect.close()
# Delete data from db-------------------------------------------------------------------------------------------------------------------------------
    def delete_data(self):
        connect = psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost")
        cur = connect.cursor()
        print(self.roll_No_var.get())
        cur.execute("delete from students where roll_no={}".format(self.roll_No_var.get()) )
        connect.commit()
        connect.close()
        self.fetch_data()
        self.clear()
# Search data by key-------------------------------------------------------------------------------------------------------------------------------
    def search_data(self):
        # connect = self.link
        connect = psycopg2.connect(dbname="stm", user="postgres", password="askarova180774", host="localhost")
        cur = connect.cursor()
        if self.search_by.get() == "roll_no":
            cur.execute("select * from students where " + str(
                self.search_by.get() + "=" + self.search_txt.get()))
        else:
            # cur.execute("select * from students where " + str(
            #     self.search_by.get() + " LIKE '%" + str(self.search_txt.get()) + "%'"))
            cur.execute("SELECT * FROM students WHERE LOWER( students."
                        + self.search_by.get() + ") LIKE  '%" + str(self.search_txt.get().lower()) + "%' ORDER BY roll_no ASC")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            connect.commit()
        connect.close()
# -------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------

root = Tk()
# Tk.wm_attributes(root, "-fullscreen", True)

ob = Student(root)
root.mainloop()