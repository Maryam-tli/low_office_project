from tkinter import *
from customtkinter import *
from customtkinter import set_appearance_mode
from tkinter import messagebox
from tkinter import ttk
from BE.Law import low, Appointment, Safe
from BLL.Rules import Blrepository
from datetime import datetime, timedelta


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.creatwidget()
        self.load()

    def creatwidget(self):

        menubar = Menu(self.screen)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Language", menu=filemenu)
        filemenu.add_command(label="English", command=self.English)
        filemenu.add_command(label="Persian", command=self.Persian)
        self.screen.config(menu=menubar)

        set_appearance_mode("dark")

        styleAll = ttk.Style()
        styleAll.theme_use('clam')
        styleAll.configure("TCombobox", background="#3f414d", foreground="black")

        self.menu_bar = Menu(self.screen)
        self.screen.config(menu=self.menu_bar)

        # self.appointment_menu = Menu(self.menu_bar, tearoff=0)
        # self.menu_bar.add_cascade(label="Appointment", menu=self.appointment_menu)
        # self.appointment_menu.add_command(label="Schedule Appointment", command=self.open_appointment_window)

        self.Language = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Language", menu=self.Language)
        self.Language.add_command(label="English", command=self.English)
        self.Language.add_command(label="Persian", command=self.Persian)

        self.backimage = PhotoImage(file="img2.png")
        self.lblback = Label(self.screen, image=self.backimage).place(x=0, y=0)
        self.icoclose = PhotoImage(file="c5.png")

        self.Id = IntVar()
        self.Name = StringVar()
        self.PersonId = StringVar()
        self.PhoneNumber = StringVar()
        self.FullAddress = StringVar()
        self.JobTitle = StringVar()
        self.HowFindUs = StringVar()
        self.CaseType = StringVar()
        self.CaseType1 = StringVar()
        self.PartyInLawsuit = StringVar()
        self.CaseStatus = StringVar()

        # self.font=("Roboto", 25)

        self.EntId = Entry(self.screen, textvariable=self.Id)

        self.lblClient = CTkLabel(self.screen, text="Client Information", font=("Roboto", 25)).place(x=40, y=10)
        self.LblName = CTkLabel(self.screen, text="Full Name", font=("Roboto", 15)).place(x=50, y=70)
        self.EntName = CTkEntry(self.screen, textvariable=self.Name, width=150, text_color="white")
        self.EntName.insert(0, "SaeedTavakoli")
        self.EntName.configure(text_color="gray")
        self.EntName.bind("<FocusIn>", self.InEntryName)
        self.EntName.bind("<FocusOut>", self.OutEntryName)
        self.EntName.place(x=170, y=70)

        self.LblPhone = CTkLabel(self.screen, text="Phone Number", font=("Roboto", 15)).place(x=50, y=100)
        self.EntPhone = CTkEntry(self.screen, textvariable=self.PhoneNumber, width=150, text_color="white")
        self.EntPhone.insert(0, "09123456789")
        self.EntPhone.configure(text_color="gray")
        self.EntPhone.bind("<FocusIn>", self.InEntryPhone)
        self.EntPhone.bind("<FocusOut>", self.OutEntryPhone)
        self.EntPhone.place(x=170, y=100)

        self.LblId = CTkLabel(self.screen, text=" Person Id", font=("Roboto", 15)).place(x=50, y=130)
        self.EntId = CTkEntry(self.screen, textvariable=self.PersonId, width=150, text_color="white")
        self.EntId.insert(0, "0150148876")
        self.EntId.configure(text_color="gray")
        self.EntId.bind("<FocusIn>", self.InEntId)
        self.EntId.bind("<FocusOut>", self.OutEntId)
        self.EntId.place(x=170, y=130)

        self.LblAdress = CTkLabel(self.screen, text="Full Address", font=("Roboto", 15)).place(x=50, y=160)
        self.EntAdress = CTkEntry(self.screen, textvariable=self.FullAddress, width=150, text_color="white")
        self.EntAdress.insert(0, "Iran,Tehran,Sadeghieh")
        self.EntAdress.configure(text_color="gray")
        self.EntAdress.bind("<FocusIn>", self.InEntryAddress)
        self.EntAdress.bind("<FocusOut>", self.OutEntryAddress)
        self.EntAdress.place(x=170, y=160)

        self.LblJob = CTkLabel(self.screen, text="Job Title", font=("Roboto", 15)).place(x=50, y=190)
        self.EntJob = CTkEntry(self.screen, textvariable=self.JobTitle, width=150, text_color="white")
        self.EntJob.insert(0, "lawyer")
        self.EntJob.configure(text_color="gray")
        self.EntJob.bind("<FocusIn>", self.InEntryJob)
        self.EntJob.bind("<FocusOut>", self.OutEntryJob)
        self.EntJob.place(x=170, y=190)

        self.LblFind = CTkLabel(self.screen, text="How Find Us", font=("Roboto", 15)).place(x=50, y=220)
        self.EntFind = CTkEntry(self.screen, textvariable=self.HowFindUs, width=150, text_color="white")
        self.EntFind.insert(0, "MyFriend")
        self.EntFind.configure(text_color="gray")
        self.EntFind.bind("<FocusIn>", self.InEntryFind)
        self.EntFind.bind("<FocusOut>", self.OutEntryFind)
        self.EntFind.place(x=170, y=220)

        self.LblType = CTkLabel(self.screen, text="File Type", font=("Roboto", 15)).place(x=50, y=250)
        self.FileType = StringVar()
        self.ComboFileType = ttk.Combobox(self.screen, state="readonly",
                                          values=["Civil Cases", "Criminal Cases", "Registry Cases", "Family Cases",
                                                  "Other Cases"], textvariable=self.FileType, width=22)
        self.ComboFileType.place(x=170, y=250)
        self.ComboFileType.bind("<<ComboboxSelected>>", self.on_combobox_select)

        self.entry_dict = {
            "Civil Cases": (CTkLabel(self.screen, text="Civil Case Type", font=("Roboto", 15)),
                            CTkEntry(self.screen, textvariable=self.CaseType, width=150)),
            "Criminal Cases": (CTkLabel(self.screen, text="Criminal Case Type", font=("Roboto", 15)),
                               CTkEntry(self.screen, textvariable=self.CaseType, width=150)),
            "Registry Cases": (CTkLabel(self.screen, text="Registry Case Type", font=("Roboto", 15)),
                               CTkEntry(self.screen, textvariable=self.CaseType, width=150)),
            "Family Cases": (CTkLabel(self.screen, text="Family Case Type", font=("Roboto", 15)),
                             CTkEntry(self.screen, textvariable=self.CaseType, width=150)),
            "Other Cases": (CTkLabel(self.screen, text="Other Case Type", font=("Roboto", 15)),
                            CTkEntry(self.screen, textvariable=self.CaseType, width=150)),
        }

        self.LblLawsuit = CTkLabel(self.screen, text="Party in a lawsuit", font=("Roboto", 15)).place(x=50, y=310)
        self.Lawsuit = StringVar()
        self.ComboLawsuit = ttk.Combobox(self.screen, state="readonly", values=["Individual", "Juridical person"],
                                         textvariable=self.Lawsuit, width=22)
        self.ComboLawsuit.place(x=170, y=310)

        self.LblCase = CTkLabel(self.screen, text="Case Status", font=("Roboto", 15)).place(x=50, y=340)
        self.Case = StringVar()
        self.ComboCase = ttk.Combobox(self.screen, state="readonly",
                                      values=["Consultation Only", "Judgment Issued", "Judgment Pending",
                                              "Before Lawsuit"], textvariable=self.Case, width=22)
        self.ComboCase.place(x=170, y=340)
        self.radio_var = StringVar(value=" ")

        self.radio_buttons = {
            "Judgment Issued": [
                Radiobutton(self.screen, text="First Instance", variable=self.radio_var, value="First Instance"),
                Radiobutton(self.screen, text="Appeal", variable=self.radio_var, value="Appeal")
            ],
            "Judgment Pending": [
                Radiobutton(self.screen, text="I have a lawyer", variable=self.radio_var, value="I have a lawyer"),
                Radiobutton(self.screen, text="I do not have a lawyer", variable=self.radio_var,
                            value="I do not have a lawyer")
            ]
        }
        self.ComboCase.bind("<<ComboboxSelected>>", self.on_case_combobox_select)

        self.LblHistory = CTkLabel(self.screen, text="History of visits", font=("Roboto", 15)).place(x=50, y=430)
        self.History = StringVar()
        self.ComboHistory = ttk.Combobox(self.screen, state="readonly", values=["First time", "Others"],
                                         textvariable=self.History, width=22)

        self.ComboHistory.place(x=170, y=430)

        self.frametbl = Frame(self.screen)
        self.frametbl.place(x=10, y=470)

        self.scrollbar = Scrollbar(self.frametbl, orient=VERTICAL)

        self.tbl = ttk.Treeview(self.frametbl, columns=(
            "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14"),
                                show="headings", height=10, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tbl.yview)

        for i in range(1, 15):
            self.tbl.column("a1", width=50)
            self.tbl.heading("a1", text="Id")
            self.tbl.column("a2", width=110)
            self.tbl.heading("a2", text="Full Name")
            self.tbl.column("a3", width=90)
            self.tbl.heading("a3", text="Phone Number")
            self.tbl.column("a4", width=70)
            self.tbl.heading("a4", text="Person Id")
            self.tbl.column("a5", width=170)
            self.tbl.heading("a5", text="Full Address")
            self.tbl.column("a6", width=70)
            self.tbl.heading("a6", text="Job Title")
            self.tbl.column("a7", width=80)
            self.tbl.heading("a7", text="How Find Us")
            self.tbl.column("a8", width=90)
            self.tbl.heading("a8", text="File Type")
            self.tbl.column("a9", width=70)
            self.tbl.heading("a9", text="Cases Type")
            self.tbl.column("a10", width=90)
            self.tbl.heading("a10", text="Party in Lawsuit")
            self.tbl.column("a11", width=110)
            self.tbl.heading("a11", text="Case Status")
            self.tbl.column("a12", width=110)
            self.tbl.heading("a12", text="Judgment Issued")
            self.tbl.column("a13", width=125)
            self.tbl.heading("a13", text="Judgment Pending")
            self.tbl.column("a14", width=70)
            self.tbl.heading("a14", text="History")

        self.tbl.bind("<<TreeviewSelect>>", self.Getselection)
        self.tbl.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.btnSubmit = CTkButton(self.screen, text="Save", fg_color="#3f414d", command=self.submit_data, width=10)
        self.btnSubmit.place(x=420, y=430)

        self.btnLoad = CTkButton(self.screen, text="Edit", fg_color="#3f414d", command=self.Update, width=10)
        self.btnLoad.place(x=520, y=430)

        self.btndelete = CTkButton(self.screen, text="Delete", fg_color="#3f414d", command=self.Delete, width=10)
        self.btndelete.place(x=620, y=430)

        self.SearchFrame = Frame(self.screen, width=400, height=300, background="brown")
        self.SearchFrame.place_forget()
        self.btnsearch = CTkButton(self.screen, text="Search", fg_color="#3f414d", command=self.Clicksearch, width=10)
        self.btnsearch.place(x=720, y=430)
        self.bgframe = PhotoImage(file="design.png")
        self.Img = Label(self.SearchFrame, text="*", image=self.bgframe).place(x=0, y=0)
        self.LblSearch = CTkLabel(self.SearchFrame, text="Search", font=("Roboto", 15))
        self.LblSearch.place(x=80, y=30)
        self.search = StringVar()
        self.EntSearch = CTkEntry(self.SearchFrame, textvariable=self.search)
        self.EntSearch.place(x=130, y=30)
        self.EntSearch.bind("<KeyRelease>", self.Search)  # اتصال به تابع جستجو

        # جعبه نمایش پیشنهادات
        self.suggestion_listbox = CTkTextbox(self.SearchFrame, width=350, height=150)
        self.suggestion_listbox.place(x=30, y=80)
        self.suggestion_listbox.bind("<ButtonRelease-1>", self.on_suggestion_select)  # انتخاب پیشنهاد

        self.btnclose = Button(self.SearchFrame, text="Close", image=self.icoclose, command=self.ClickClose).place(
            x=350, y=6)
        self.ButtonReporting = CTkButton(self.screen, text="Reporting", command=self.Reporting, fg_color="#961520")
        self.ButtonReporting.place(x=950, y=430)

        # Frame login
        self.frmlogin = Frame(self.screen, bg="#747cd6", width=9000, height=9000)
        self.frmlogin.place(x=0, y=0)
        self.Idshakhsi = StringVar()
        self.Full = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        self.Role = StringVar()
        self.lbluser = CTkLabel(self.frmlogin, text="Username", font=("Roboto", 25, "bold")).place(x=450, y=202)
        self.entuser = CTkEntry(self.frmlogin, textvariable=self.user, width=150)
        self.entuser.insert(0, "Mr.Tavakoli")
        self.entuser.configure(text_color="gray")
        self.entuser.bind("<FocusIn>", self.EnterUserIn)
        self.entuser.bind("<FocusOut>", self.EnterUserOut)
        self.entuser.place(x=580, y=210)
        self.lblpass = CTkLabel(self.frmlogin, text="Password", font=("Roboto", 25, "bold")).place(x=450, y=254)
        self.entpass = CTkEntry(self.frmlogin, textvariable=self.password, show="*", width=150)
        self.entpass.insert(0, "1234")
        self.entpass.configure(text_color="gray")
        self.entpass.bind("<FocusIn>", self.EnterPassIn)
        self.entpass.bind("<FocusOut>", self.EnterPassOut)
        self.entpass.place(x=580, y=260)
        self.Btnlogin = CTkButton(self.frmlogin, text="Login", command=self.Log, fg_color="#3f414d")
        self.Btnlogin.place(x=400, y=500)
        self.entuser.bind("<Return>", self.forshow)
        self.entpass.bind("<Return>", self.login_focus)
        self.frmlogin.bind("<Map>", self.on_entry_click)

    def EnterUserIn(self, e):
        if self.entuser.get() == "Mr.Tavakoli":
            self.entuser.delete(0, "end")
            self.entuser.configure(text_color="white")

    def EnterUserOut(self, e):
        if self.entuser.get() == "":
            self.entuser.insert(0, "Mr.Tavakoli")
            self.entuser.configure(text_color="gray")

    def EnterPassIn(self, e):
        if self.entpass.get() == "1234":
            self.entpass.delete(0, "end")
            self.entpass.configure(text_color="white")

    def EnterPassOut(self, e):
        if self.entpass.get() == "":
            self.entpass.insert(0, "1234")
            self.entpass.configure(text_color="gray")

    def Reporting(self):
        # ایجاد یک frame جدید برای نمایش جدول
        self.report_frame = Frame(self.screen, background="#3b161a", width=640, height=400)
        self.report_frame.place(x=300, y=80)
        self.ButClose = Button(self.report_frame, text="Close", command=self.reportclose)
        self.ButClose.place(x=600, y=10)

        # تنظیمات جدول (Treeview)
        self.tree_report = ttk.Treeview(self.report_frame, columns=('a1', 'a2'), show='headings', height=10)

        self.tree_report.column('a1', width=150)
        self.tree_report.heading('a1', text='Full Name')
        self.tree_report.column('a2', width=150)
        self.tree_report.heading('a2', text='Judgment Issued')

        # استفاده از place برای جایگذاری جدول
        self.tree_report.place(x=10, y=10, width=580, height=380)

        # بازیابی اطلاعات از دیتابیس
        self.load_reporting_data()

    def load_reporting_data(self):
        # دیکشنری برای ترجمه
        translation_dict = {
            "بدوی": "First Instance",
            "تجدید نظر": "Appeal",
        }

        # دریافت داده‌ها از دیتابیس
        records = Blrepository().Read(low)

        # پاک کردن داده‌های قبلی جدول
        for item in self.tree_report.get_children():
            self.tree_report.delete(item)

        # اضافه کردن داده‌ها به جدول
        for record in records:
            # فقط رکوردهایی که JudgmentIssued انتخاب شده‌اند
            if record.JudgmentIssued:  # اطمینان از وجود مقدار
                # ترجمه مقدار JudgmentIssued
                translated_judgment_issued = translation_dict.get(record.JudgmentIssued, record.JudgmentIssued)
                self.tree_report.insert('', 'end', values=(record.FullName, translated_judgment_issued))

    def reportclose(self):
        self.report_frame.place_forget()

    def on_entry_click(self, e):
        self.entuser.focus_set()

    def InEntryName(self, e):
        if self.EntName.get() == "SaeedTavakoli":
            self.EntName.delete(0, "end")
            self.EntName.configure(text_color="white")

    def OutEntryName(self, e):
        if self.EntName.get() == "":
            self.EntName.insert(0, "SaeedTavakoli")
            self.EntName.configure(text_color="gray")

    def InEntryPhone(self, e):
        if self.EntPhone.get() == "09123456789":
            self.EntPhone.delete(0, "end")
            self.EntPhone.configure(text_color="white")

    def OutEntryPhone(self, e):
        if self.EntPhone.get() == "":
            print("out ok")
            self.EntPhone.insert(0, "09123456789")
            self.EntPhone.configure(text_color="gray")

    def InEntId(self, e):
        if self.EntId.get() == "0150148876":
            self.EntId.delete(0, "end")
            self.EntId.configure(text_color="white")

    def OutEntId(self, e):
        if self.EntId.get() == "":
            self.EntId.insert(0, "0150148876")
            self.EntId.configure(text_color="gray")

    def InEntryAddress(self, e):
        if self.EntAdress.get() == "Iran,Tehran,Sadeghieh":
            self.EntAdress.delete(0, "end")
            self.EntAdress.configure(text_color="white")

    def OutEntryAddress(self, e):
        if self.EntAdress.get() == "":
            self.EntAdress.insert(0, "Iran,Tehran,Sadeghieh")
            self.EntAdress.configure(text_color="gray")

    def InEntryJob(self, e):
        if self.EntJob.get() == "lawyer":
            self.EntJob.delete(0, "end")
            self.EntJob.configure(text_color="white")

    def OutEntryJob(self, e):
        if self.EntJob.get() == "":
            self.EntJob.insert(0, "lawyer")
            self.EntJob.configure(text_color="gray")

    def InEntryFind(self, e):
        if self.EntFind.get() == "MyFriend":
            self.EntFind.delete(0, "end")
            self.EntFind.configure(text_color="white")

    def OutEntryFind(self, e):
        if self.EntFind.get() == "":
            self.EntFind.insert(0, "MyFriend")
            self.EntFind.configure(text_color="gray")

    def forshow(self, e):
        self.entpass.focus_set()

    def login_focus(self, e):
        self.Btnlogin.invoke()

    def Log(self):
        new = Safe("", self.user.get(), self.password.get(), "")
        ob = Blrepository()
        res = ob.vasl(Safe, new)

        if not res:
            messagebox.showerror("Error", "Username or Password is incorrect!")
        elif res.Role == "Employee":
            self.frmlogin.place_forget()
            self.appointment_menu = Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="Appointment", menu=self.appointment_menu)
            self.appointment_menu.add_command(label="Schedule Appointment", command=self.open_appointment_window)

        elif res.Role == "Manager":
            self.frmlogin.place_forget()
            btn_add_member = CTkButton(self.screen, text="Add Member", command=self.add_member, fg_color="#3f414d",
                                       width=25)
            btn_add_member.place(x=815, y=430)
            self.appointment_menu = Menu(self.menu_bar, tearoff=0)
            self.menu_bar.add_cascade(label="Appointment", menu=self.appointment_menu)
            self.appointment_menu.add_command(label="Schedule Appointment", command=self.open_appointment_window)

    def add_member(self):
        self.add_member_frame = Frame(self.screen, bg="dark blue")
        self.add_member_frame.place(x=0, y=0, width=700, height=500)

        # تعریف متغیرها
        self.Id = StringVar()
        self.name = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        self.Role = StringVar()
        self.search_member_var = StringVar()

        # لیبل و ورودی برای نام کارمند
        self.lbl_name = CTkLabel(self.add_member_frame, text="FullName:", font=("Roboto", 15))
        self.lbl_name.place(x=20, y=20)
        self.ent_name = CTkEntry(self.add_member_frame, textvariable=self.name, width=145)
        self.ent_name.insert(0, "Saeed Tavakoli")
        self.ent_name.configure(text_color="gray")
        self.ent_name.bind("<FocusIn>", self.FullIn)
        self.ent_name.bind("<FocusOut>", self.FullOut)
        self.ent_name.place(x=150, y=20)

        # لیبل و ورودی برای نام کاربری
        self.lbl_username = CTkLabel(self.add_member_frame, text="Username:", font=("Roboto", 15))
        self.lbl_username.place(x=20, y=60)
        self.ent_username = CTkEntry(self.add_member_frame, textvariable=self.user, width=145)
        self.ent_username.insert(0, "Mr.Tavakoli")
        self.ent_username.configure(text_color="gray")
        self.ent_username.bind("<FocusIn>", self.EntUserIn)
        self.ent_username.bind("<FocusOut>", self.EntUserOut)
        self.ent_username.place(x=150, y=60)

        # لیبل و ورودی برای رمز عبور
        self.lbl_password = CTkLabel(self.add_member_frame, text="Password:", font=("Roboto", 15))
        self.lbl_password.place(x=20, y=100)
        self.ent_password = CTkEntry(self.add_member_frame, textvariable=self.password, width=145)
        self.ent_password.insert(0, "1234")
        self.ent_password.configure(text_color="gray")
        self.ent_password.bind("<FocusIn>", self.EntPassIn)
        self.ent_password.bind("<FocusOut>", self.EntPassOut)
        self.ent_password.place(x=150, y=100)

        # لیبل و ورودی برای نقش
        self.lbl_role = CTkLabel(self.add_member_frame, text="Role", font=("Roboto", 15))
        self.lbl_role.place(x=20, y=140)
        self.ComboRole = ttk.Combobox(self.add_member_frame, state="readonly", values=["Manager", "Employee"],
                                      textvariable=self.Role)
        self.ComboRole.place(x=150, y=140)

        # جدول برای نمایش اطلاعات
        self.frmscr = Frame(self.add_member_frame)
        self.frmscr.place(x=300, y=60)
        self.scr = Scrollbar(self.frmscr, orient=VERTICAL)
        self.tbl_members = ttk.Treeview(self.frmscr, columns=("#1", "#2", "#3", "#4", "#5"), show="headings",
                                        height=20, yscrollcommand=self.scrollbar.set)
        self.scr.config(command=self.tbl_members.yview)
        self.tbl_members.column("#1", width=50)
        self.tbl_members.heading("#1", text="Id")
        self.tbl_members.column("#2", width=110)
        self.tbl_members.heading("#2", text="FullName")
        self.tbl_members.column("#3", width=75)
        self.tbl_members.heading("#3", text="Username")
        self.tbl_members.column("#4", width=75)
        self.tbl_members.heading("#4", text="Password")
        self.tbl_members.column("#5", width=70)
        self.tbl_members.heading("#5", text="Role")
        self.tbl_members.pack(side=LEFT, fill=BOTH, expand=True)
        self.tbl_members.bind("<<TreeviewSelect>>", self.Getselectionadd)
        self.scr.pack(side=RIGHT, fill=Y)
        self.load_members_data(self.tbl_members)

        # دکمه‌ها
        btn_add = CTkButton(self.add_member_frame, text="Add Member", fg_color="#3f414d", command=self.addbox, width=7)
        btn_add.place(x=0, y=200)
        btn_update = CTkButton(self.add_member_frame, text="Update", command=self.updatebox, fg_color="#3f414d",
                               width=7)
        btn_update.place(x=100, y=200)
        btn_delete = CTkButton(self.add_member_frame, text="Delete", command=self.delete_member, fg_color="#3f414d",
                               width=7)
        btn_delete.place(x=172, y=200)
        self.sbutton = CTkButton(self.add_member_frame, text="Search", command=self.search_framemember,
                                 fg_color="#3f414d", width=7)
        self.sbutton.place(x=238, y=200)
        btn_close = Button(self.add_member_frame, text="Close", image=self.icoclose, command=self.Tclose).place(x=640,
                                                                                                                y=10)

        # فریم جستجو
        self.search_member_frame = Frame(self.add_member_frame, bg="lightgrey", padx=10, pady=10)
        self.search_member_frame.place_forget()
        self.lblsearch = CTkLabel(self.search_member_frame, text="Search", text_color="black", font=("Roboto", 15))
        self.lblsearch.place(x=5, y=20)
        self.entsearch = CTkEntry(self.search_member_frame, textvariable=self.search_member_var, width=150)
        self.entsearch.place(x=80, y=20)
        self.suggestion_textbox = CTkTextbox(self.search_member_frame, width=260, height=300)
        self.suggestion_textbox.place(x=10, y=50)
        self.suggestion_textbox.bind("<ButtonRelease-1>", self.suggestion_member)
        self.entsearch.bind("<KeyRelease>", self.search_automember)
        self.bclose = Button(self.search_member_frame, text="Close", image=self.icoclose, command=self.searchclose)
        self.bclose.place(x=250, y=6)

    def FullIn(self, e):
        if self.ent_name.get() == "Saeed Tavakoli":
            self.ent_name.delete(0, "end")
            self.ent_name.configure(text_color="white")

    def FullOut(self, e):
        if self.ent_name.get() == "":
            self.ent_name.insert(0, "Saeed Tavakoli")
            self.ent_name.configure(text_color="gray")

    def EntUserIn(self, e):
        if self.ent_username.get() == "Mr.Tavakoli":
            self.ent_username.delete(0, "end")
            self.ent_username.configure(text_color="white")

    def EntUserOut(self, e):
        if self.ent_username.get() == "":
            self.ent_username.insert(0, "Mr.Tavakoli")
            self.ent_username.configure(text_color="gray")

    def EntPassIn(self, e):
        if self.ent_password.get() == "1234":
            self.ent_password.delete(0, "end")
            self.ent_password.configure(text_color="white")

    def EntPassOut(self, e):
        if self.ent_password.get() == "":
            self.ent_password.insert(0, "1234")
            self.ent_password.configure(text_color="gray")

    def addbox(self):
        # گرفتن اطلاعات از ورودی‌ها
        name = self.name.get()
        username = self.user.get()
        password = self.password.get()
        role = self.Role.get()

        # اعتبارسنجی اولیه
        if not name or not username or not password or not role:
            return  # اگر فیلدی خالی باشد، تابع متوقف می‌شود

        # اضافه کردن اطلاعات به دیتابیس
        new_member = Safe(FullName=name, UserName=username, Password=password, Role=role)
        ob = Blrepository()
        ob.Add(new_member)

        # پاک کردن ورودی‌ها
        self.name.set('')
        self.user.set('')
        self.password.set('')
        self.Role.set('')

        # اضافه کردن داده‌های جدید به جدول
        self.tbl_members.insert("", END, values=(
            new_member.Id, new_member.FullName, new_member.UserName, new_member.Password, new_member.Role))

    def load_members_data(self, table):
        # بارگذاری اطلاعات از دیتابیس
        ob = Blrepository()
        members = ob.Read(Safe)  # فرض می‌کنیم متد Read تمام اعضا را بازمی‌گرداند

        # پاک‌سازی جدول قبل از بارگذاری مجدد داده‌ها
        table.delete(*table.get_children())

        # نمایش اطلاعات در جدول
        for member in members:
            table.insert("", "end", values=(member.Id, member.FullName, member.UserName, member.Password, member.Role))

    def updatebox(self):
        obj = Blrepository()
        obj.Update(Safe, self.Idsel, FullName=self.ent_name.get(), UserName=self.ent_username.get(),
                   Password=self.ent_password.get(), Role=self.ComboRole.get())
        self.load_members_data(self.tbl_members)

    def Getselectionadd(self, event):
        selected_item = self.tbl_members.selection()
        self.ent_name.configure(text_color="white")
        self.ent_username.configure(text_color="white")
        self.ent_password.configure(text_color="white")
        if not selected_item:
            return

        self.Idsel = self.tbl_members.item(selected_item)["values"][0]
        self.Id.set(self.Idsel)
        self.namesel = self.tbl_members.item(selected_item)["values"][1]
        self.name.set(self.namesel)
        self.usersel = self.tbl_members.item(selected_item)["values"][2]
        self.user.set(self.usersel)
        self.passsel = self.tbl_members.item(selected_item)["values"][3]
        self.password.set(self.passsel)
        self.Rolesel = self.tbl_members.item(selected_item)["values"][4]
        self.Role.set(self.Rolesel)

    def delete_member(self):
        j = Blrepository()
        j.Delete(Safe, self.Idsel)
        self.load_members_data(self.tbl_members)
        self.name.set('')
        self.user.set('')
        self.password.set('')
        self.Role.set('')

    def search_framemember(self):
        self.search_member_frame.place(x=0, y=240, width=300, height=250)

    def search_automember(self, event=None):
        text_search = self.search_member_var.get().lower()
        print("Search triggered with:", text_search)

        # پاک کردن پیشنهادات قبلی
        self.suggestion_textbox.delete("1.0", "end")

        # جستجو در پایگاه داده با استفاده از Blrepository
        obj = Blrepository()
        results = obj.search_member(Safe, text_search)

        # پاک کردن ردیف‌های قبلی جدول
        self.tbl_members.delete(*self.tbl_members.get_children())

        # افزودن نتایج جستجو به جدول و پیشنهادات
        if results:
            for record in results:
                # افزودن نتیجه به جدول
                self.tbl_members.insert(
                    "",
                    "end",
                    values=(record.Id, record.FullName, record.UserName, record.Password, record.Role)
                )
                # افزودن پیشنهاد به TextBox
                suggestion_text = f"{record.Id} - {record.FullName}"
                self.suggestion_textbox.insert("end", suggestion_text + "\n")
        else:
            self.suggestion_textbox.insert("end", "هیچ داده‌ای یافت نشد")

    def suggestion_member(self, event):
        try:
            # دریافت مختصات کلیک
            index = self.suggestion_textbox.index(f"@{event.x},{event.y}")

            # یافتن خط کامل در محل کلیک
            selected_line = self.suggestion_textbox.get(f"{index} linestart", f"{index} lineend")

            if selected_line:
                # استخراج شناسه از خط انتخاب‌شده
                selected_id = selected_line.split(" - ")[0].strip()

                # جستجوی عضو با شناسه انتخاب‌شده
                obj = Blrepository()
                member = obj.search_member_by_id(Safe, selected_id)

                # پاک کردن ردیف‌های قبلی جدول
                self.tbl_members.delete(*self.tbl_members.get_children())

                # افزودن نتیجه به جدول
                if member:
                    self.tbl_members.insert(
                        "",
                        "end",
                        values=(member.Id, member.FullName, member.UserName, member.Password, member.Role)
                    )
                    # تنظیم مقادیر در ورودی‌ها
                    self.Getselectionadd(None)
                else:
                    print("داده‌ای با شناسه انتخاب‌شده یافت نشد")
            else:
                print("خطی انتخاب نشده است")
        except Exception as e:
            print(f"خطا: {e}")

    def Tclose(self):
        self.add_member_frame.place_forget()

    def searchclose(self):
        self.search_member_frame.place_forget()
        self.load_members_data(self.tbl_members)

    def on_combobox_select(self, event):
        print("on_combobox_select")
        self.selected_value = self.ComboFileType.get()
        print(self.selected_value)

        # حذف لیبل‌ها و ورودی‌های قبلی
        if hasattr(self, 'current_label'):
            self.current_label.destroy()
        if hasattr(self, 'current_entry'):
            self.current_entry.destroy()

        # ایجاد لیبل و ورودی جدید بر اساس انتخاب کاربر
        if self.selected_value == "Civil Cases":
            self.current_label = CTkLabel(self.screen, text="Civil Case Type")
            self.current_label.place(x=50, y=280)
            self.current_entry = CTkEntry(self.screen, width=150)
            self.current_entry.place(x=170, y=280)

        elif self.selected_value == "Criminal Cases":
            self.current_label = CTkLabel(self.screen, text="Criminal Cases Type")
            self.current_label.place(x=50, y=280)
            self.current_entry = CTkEntry(self.screen, width=150)
            self.current_entry.place(x=170, y=280)

        elif self.selected_value == "Registry Cases":
            self.current_label = CTkLabel(self.screen, text="Registry Cases Type")
            self.current_label.place(x=50, y=280)
            self.current_entry = CTkEntry(self.screen, width=150)
            self.current_entry.place(x=170, y=280)

        elif self.selected_value == "Family Cases":
            self.current_label = CTkLabel(self.screen, text="Family Cases Type")
            self.current_label.place(x=50, y=280)
            self.current_entry = CTkEntry(self.screen, width=150)
            self.current_entry.place(x=170, y=280)

        elif self.selected_value == "Other Cases":
            self.current_label = CTkLabel(self.screen, text="Other Cases Type")
            self.current_label.place(x=50, y=280)
            self.current_entry = CTkEntry(self.screen, width=150)
            self.current_entry.place(x=170, y=280)
        print(self.current_entry.get())

    def on_case_combobox_select(self, event):
        selected_case = self.ComboCase.get()

        for radiobutton_list in self.radio_buttons.values():
            for radiobutton in radiobutton_list:
                radiobutton.place_forget()
        if selected_case in self.radio_buttons:
            y_position = 370
            for radiobutton in self.radio_buttons[selected_case]:
                radiobutton.place(x=50, y=y_position)
                y_position += 30

    def submit_data(self):
        # دریافت مقادیر از ویجت‌ها
        print("start EN")
        id = self.Id.get()
        name = self.Name.get()
        phone = self.PhoneNumber.get()
        person_id = self.PersonId.get()
        address = self.FullAddress.get()
        job_title = self.JobTitle.get()
        how_find_us = self.HowFindUs.get()
        file_type = self.ComboFileType.get()

        # استخراج مقدار case_type از current_entry
        if hasattr(self, 'current_entry'):
            case_type = self.current_entry.get().strip()
        else:
            case_type = ""

        party_lawsuit = self.Lawsuit.get()
        case_status = self.Case.get()

        # مقداردهی به وضعیت رادیویی بر اساس وضعیت مورد نظر
        radio_choice = ""
        if case_status == "Judgment Issued":
            radio_choice = self.radio_var.get() if self.radio_var.get() else ""
        elif case_status == "Judgment Pending":
            radio_choice = self.radio_var.get() if self.radio_var.get() else ""

        history = self.History.get()

        # ایجاد یک رکورد جدید
        new_record = low(
            FullName=name,
            PhoneNumber=phone,
            PersonId=person_id,
            FullAddress=address,
            JobTitle=job_title,
            HowFindUs=how_find_us,
            FileType=file_type,
            CaseType=case_type,  # ذخیره‌سازی مقدار case_type
            PartyInLawsuit=party_lawsuit,
            CaseStatues=case_status,
            JudgmentIssued=radio_choice if case_status == "Judgment Issued" else "",
            JudgmentPending=radio_choice if case_status == "Judgment Pending" else "",
            History=history
        )

        # ایجاد شیء از Blrepository برای اضافه کردن رکورد به دیتابیس
        obj = Blrepository()
        obj.AddRegister(new_record)

        # بارگذاری داده‌های جدید در Treeview
        self.load()

    def load(self):

        for row in self.tbl.get_children():
            self.tbl.delete(row)

        obj = Blrepository()
        records = obj.Read(low)

        for record in records:
            self.tbl.insert("", "end",
                            values=(record.Id, record.FullName, record.PhoneNumber, record.PersonId, record.FullAddress,
                                    record.JobTitle, record.HowFindUs, record.FileType, record.CaseType,
                                    record.PartyInLawsuit, record.CaseStatues, record.JudgmentIssued,
                                    record.JudgmentPending, record.History))

    def Update(self):
        obj = Blrepository()
        obj.Update(low, self.Idrow, FullName=self.EntName.get(),
                   PhoneNumber=self.EntPhone.get(),
                   PersonId=self.EntId.get(),
                   FullAddress=self.EntAdress.get(),
                   JobTitle=self.EntJob.get(),
                   HowFindUs=self.EntFind.get(),
                   FileType=self.ComboFileType.get(),
                   case_type=self.CaseType.get() if self.FileType.get() else "",
                   PartyInLawsuit=self.Lawsuit.get(),
                   CaseStatues=self.Case.get(),
                   JudgmentIssued=self.radio_var.get() if self.Case.get() == "Judgment Issued" else "",
                   JudgmentPending=self.radio_var.get() if self.Case.get() == "Judgment Pending" else "",
                   History=self.History.get()
                   )
        self.load()

    def Getselection(self, event):
        select = self.tbl.selection()
        self.EntName.configure(text_color="white")
        self.EntPhone.configure(text_color="white")
        self.EntId.configure(text_color="white")
        self.EntAdress.configure(text_color="white")
        self.EntJob.configure(text_color="white")
        self.EntFind.configure(text_color="white")

        if select:
            values = self.tbl.item(select)["values"]

            self.Idrow = values[0]
            self.Id.set(self.Idrow)

            self.Name.set(values[1])
            self.PhoneNumber.set(values[2])
            self.PersonId.set(values[3])
            self.FullAddress.set(values[4])
            self.JobTitle.set(values[5])
            self.HowFindUs.set(values[6])
            self.ComboFileType.set(values[7])

            # Call on_combobox_select to update the current_entry field
            self.on_combobox_select(None)
            case_type_value = values[8] if values[8] else ''
            self.current_entry.delete(0, 'end')
            self.current_entry.insert(0, case_type_value)

            self.Lawsuit.set(values[9])
            self.CaseStatus.set(values[10])
            self.ComboCase.set(values[10])
            self.on_case_combobox_select(None)

            if values[10] in ["Judgment Issued", "Judgment Pending"]:
                RadioChoice = values[11] if values[10] == "Judgment Issued" else values[12]
                self.radio_var.set(RadioChoice)

                for radiobutton in self.radio_buttons[values[10]]:
                    if radiobutton.cget("value") == RadioChoice:
                        radiobutton.select()
                    else:
                        radiobutton.deselect()
            else:
                self.radio_var.set("")

            self.History.set(values[13])

    def Search(self, event=None):  # اضافه کردن event=None
        # گرفتن مقدار جستجو از ورودی و حذف فاصله‌های اضافی
        text_search = self.search.get().strip().lower()

        # چاپ پیام برای اطمینان از اجرای تابع
        print("Search triggered with:", text_search)

        # پاک کردن پیشنهادات قبلی از جعبه متن
        self.suggestion_listbox.delete("1.0", "end")

        # جستجو در پایگاه داده با استفاده از کلاس Blrepository
        obj = Blrepository()
        results = obj.Search(low, text_search)

        # پاک کردن ردیف‌های قبلی جدول (اگر جدول تعریف شده باشد)
        if hasattr(self, 'tbl') and self.tbl:
            for row in self.tbl.get_children():
                self.tbl.delete(row)

        # افزودن نتایج جستجو به جدول
        for record in results:
            self.tbl.insert(
                "",
                "end",
                values=(
                    record.Id,
                    record.FullName.strip(),
                    record.PhoneNumber.strip(),
                    record.PersonId.strip(),
                    record.FullAddress.strip(),
                    record.JobTitle.strip(),
                    record.HowFindUs.strip(),
                    record.FileType.strip(),
                    record.CaseType.strip(),
                    record.PartyInLawsuit.strip(),
                    record.CaseStatues.strip(),
                    record.JudgmentIssued.strip(),
                    record.JudgmentPending.strip(),
                    record.History.strip()
                )
            )

        # افزودن نتایج به لیست پیشنهادات در جعبه متن
        for record in results:
            suggestion_text = f"{record.Id} - {record.FullName.strip()}"
            self.suggestion_listbox.insert("end", suggestion_text + "\n")

    def on_suggestion_select(self, event):
        # گرفتن ایندکس‌های انتخاب‌شده
        try:
            # برای به‌دست‌آوردن محدوده انتخاب
            start_index = self.suggestion_listbox.index("sel.first")
            end_index = self.suggestion_listbox.index("sel.last")

            # گرفتن متن انتخاب‌شده و حذف فاصله‌های اضافی
            selection = self.suggestion_listbox.get(start_index, end_index).strip()

            # جدا کردن ID و نام از انتخاب
            if " - " in selection:
                suggestion_id, suggestion_name = selection.split(" - ", 1)

                # به‌روزرسانی ورودی جستجو با انتخاب
                self.search.set(suggestion_name.strip())

                # اجرای جستجو مجدد با استفاده از نام انتخاب شده
                self.Search(event)
        except TclError as e:
            print(f"Error: {e}")

    def Delete(self):
        j = Blrepository()
        j.Delete(low, self.Idrow)
        self.load()
        self.Id.set('')
        self.EntName.delete(0, 'end')  # پاک کردن محتوای CTkEntry
        self.EntPhone.delete(0, 'end')
        self.EntId.delete(0, 'end')
        self.EntAdress.delete(0, 'end')
        self.EntJob.delete(0, 'end')
        self.EntFind.delete(0, 'end')
        self.FileType.set('')
        self.CaseStatus.set('')  # پاک کردن محتوای کمبوباکس
        self.Lawsuit.set('')
        self.FileType.set('')
        self.CaseType.set('')
        self.current_entry.delete(0, 'end')
        self.ComboCase.set('')
        if hasattr(self, 'radio_buttons'):
            for radiobutton_list in self.radio_buttons.values():
                for radiobutton in radiobutton_list:
                    radiobutton.place_forget()
        self.History.set('')

    def Clicksearch(self):
        self.SearchFrame.place(x=380, y=10)

    def ClickClose(self):
        self.SearchFrame.place_forget()
        self.load()

    def open_appointment_window(self):
        self.appointment_frame = Frame(self.screen, bg="#329da8")
        self.appointment_frame.place(x=20, y=20, width=860, height=550)

        # Input fields for appointment details
        self.client_name_var = StringVar()
        self.date_var = StringVar()
        self.time_var = StringVar()
        self.notes_var = StringVar()

        CTkLabel(self.appointment_frame, text="Client Name", text_color="black", font=("Roboto", 15)).place(x=20, y=20)
        CTkEntry(self.appointment_frame, textvariable=self.client_name_var, width=250).place(x=150, y=20)

        CTkLabel(self.appointment_frame, text="Appointment Date", text_color="black", font=("Roboto", 15)).place(x=20,
                                                                                                                 y=60)
        self.ed = CTkEntry(self.appointment_frame, textvariable=self.date_var, width=250)
        self.ed.insert(0, "YYYY-MM-DD")
        self.ed.configure(text_color="gray")
        self.ed.bind("<FocusIn>", self.DateIn)
        self.ed.bind("<FocusOut>", self.DateOut)
        self.ed.place(x=150, y=60)

        self.et = CTkLabel(self.appointment_frame, text="Appointment Time", text_color="black",
                           font=("Roboto", 15)).place(x=20, y=100)
        self.et = CTkEntry(self.appointment_frame, textvariable=self.time_var, width=250)
        self.et.insert(0, "12:12")
        self.et.configure(text_color="gray")
        self.et.bind("<FocusIn>", self.TimeIn)
        self.et.bind("<FocusOut>", self.TimeOut)
        self.et.place(x=150, y=100)

        self.ep = CTkLabel(self.appointment_frame, text="PhoneNumber", text_color="black", font=("Roboto", 15)).place(
            x=20, y=140)
        self.ep = CTkEntry(self.appointment_frame, textvariable=self.notes_var, width=250)
        self.ep.insert(0, "09122395467")
        self.ep.configure(text_color="gray")
        self.ep.bind("<FocusIn>", self.PhoneIn)
        self.ep.bind("<FocusOut>", self.PhoneOut)
        self.ep.place(x=150, y=140)

        CTkButton(self.appointment_frame, text="Save", command=self.save_appointment, fg_color="#3f414d",
                  width=7).place(x=150, y=180)
        CTkButton(self.appointment_frame, text="Edit", command=self.edit_appointment, fg_color="#3f414d",
                  width=7).place(x=220, y=180)
        CTkButton(self.appointment_frame, text="Delete", command=self.delete_appointment, fg_color="#3f414d",
                  width=9).place(x=290, y=180)
        CTkButton(self.appointment_frame, text="Search", command=self.show_search_frame, fg_color="#3f414d",
                  width=9).place(x=367, y=180)
        CTkButton(self.appointment_frame, text="ForTomorrow", command=self.show_date, fg_color="#3f414d",
                  width=9).place(x=530, y=180)
        CTkButton(self.appointment_frame, text="ForToday", command=self.show_Today_date, fg_color="#3f414d",
                  width=9).place(x=440, y=180)
        self.appointment_close = Button(self.appointment_frame, text="Close", image=self.icoclose,
                                        command=self.c_appointment)
        self.appointment_close.place(x=800, y=10)
        self.refreshappointment = CTkButton(self.appointment_frame, text="Refresh Table", command=self.refreshapp,
                                            fg_color="#3f414d", width=10)
        self.refreshappointment.place(x=645, y=180)

        # Treeview for displaying appointments
        self.frmappoint = Frame(self.appointment_frame)
        self.frmappoint.place(x=18, y=220, relwidth=0.95, relheight=0.6)
        self.scrappoint = Scrollbar(self.frmappoint, orient=VERTICAL)
        self.Appointmenttbl = ttk.Treeview(self.frmappoint, columns=("a1", "a2", "a3", "a4", "a5"),
                                           show="headings", height=10, yscrollcommand=self.scrollbar.set)
        self.scrappoint.config(command=self.Appointmenttbl.yview)
        self.Appointmenttbl.column("a1", width=50)
        self.Appointmenttbl.heading("a1", text="Id")
        self.Appointmenttbl.column("a2", width=50)
        self.Appointmenttbl.heading("a2", text="Full Name")
        self.Appointmenttbl.column("a3", width=50)
        self.Appointmenttbl.heading("a3", text="Date")
        self.Appointmenttbl.column("a4", width=50)
        self.Appointmenttbl.heading("a4", text="Time")
        self.Appointmenttbl.column("a5", width=50)
        self.Appointmenttbl.heading("a5", text="PhoneNumber")
        self.Appointmenttbl.pack(side=LEFT, fill=BOTH, expand=True)
        self.Appointmenttbl.bind("<<TreeviewSelect>>", self.on_appointment_select)
        self.scrappoint.pack(side=RIGHT, fill=Y)

        self.load_appointments_data(self.Appointmenttbl)

        # Search frame
        self.search_frame = Frame(self.appointment_frame, bg="#0d6069")
        self.search_var = StringVar()
        CTkLabel(self.search_frame, text="Search", font=("Roboto", 15)).place(x=20, y=20)
        self.entsearch = CTkEntry(self.search_frame, textvariable=self.search_var, width=150)
        self.entsearch.place(x=80, y=20)
        self.mamsearch_close = Button(self.search_frame, text="Close", image=self.icoclose,
                                      command=self.hide_search_frame)
        self.mamsearch_close.place(x=300, y=10)
        self.suggestion_textbox = CTkTextbox(self.search_frame, width=300, height=140)
        self.suggestion_textbox.place(x=30, y=55)
        self.suggestion_textbox.bind('<ButtonRelease-1>', self.suggest)
        self.entsearch.bind('<KeyRelease>', self.search_appointment)

    def DateIn(self, e):
        if self.ed.get() == "YYYY-MM-DD":
            self.ed.delete(0, "end")
            self.ed.configure(text_color="white")

    def DateOut(self, e):
        if self.ed.get() == "":
            self.ed.insert(0, "YYYY-MM-DD")
            self.ed.configure(text_color="gray")

    def TimeIn(self, e):
        if self.et.get() == "12:12":
            self.et.delete(0, "end")
            self.et.configure(text_color="white")

    def TimeOut(self, e):
        if self.et.get() == "":
            self.et.insert(0, "12:12")
            self.et.configure(text_color="gray")

    def PhoneIn(self, e):
        if self.ep.get() == "09122395467":
            self.ep.delete(0, "end")
            self.ep.configure(text_color="white")

    def PhoneOut(self, e):
        if self.ep.get() == "":
            self.ep.insert(0, "09122395467")
            self.ep.configure(text_color="gray")

    def show_Today_date(self):
        today = datetime.now().date()
        for row in self.Appointmenttbl.get_children():
            self.Appointmenttbl.delete(row)
        for item in self.appointments:
            if item.AppointmentDate == today.strftime("%Y-%m-%d"):
                self.Appointmenttbl.insert("", "end", values=(
                    item.Id, item.ClientName, item.AppointmentDate, item.AppointmentTime,
                    item.Notes))

    def show_date(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        for row in self.Appointmenttbl.get_children():
            self.Appointmenttbl.delete(row)
        for item in self.appointments:
            # print(type(tomorrow))
            # print(tomorrow.strftime("%Y-%m-%d"))
            # print(type(tomorrow.strftime("%Y-%m-%d")))
            if item.AppointmentDate == tomorrow.strftime("%Y-%m-%d"):
                self.Appointmenttbl.insert("", "end", values=(
                    item.Id, item.ClientName, item.AppointmentDate, item.AppointmentTime,
                    item.Notes))

    def save_appointment(self):
        client_name = self.client_name_var.get()
        appointment_date = self.date_var.get()
        appointment_time = self.time_var.get()
        notes = self.notes_var.get()

        new_appointment = Appointment(
            ClientName=client_name,
            AppointmentDate=appointment_date,
            AppointmentTime=appointment_time,
            Notes=notes
        )

        obj = Blrepository()
        obj.Add(new_appointment)

        # Clear table and reload data
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())
        self.load_appointments_data(self.Appointmenttbl)

    def load_appointments_data(self, Appointmenttbl):
        obj = Blrepository()
        self.appointments = obj.Read(Appointment)

        # Clear existing data in table
        for row in Appointmenttbl.get_children():
            Appointmenttbl.delete(row)

        for appointment in self.appointments:
            Appointmenttbl.insert("", "end", values=(
                appointment.Id, appointment.ClientName, appointment.AppointmentDate, appointment.AppointmentTime,
                appointment.Notes))

    def on_appointment_select(self, event):
        select = self.Appointmenttbl.selection()
        self.ed.configure(text_color="white")
        self.et.configure(text_color="white")
        self.ep.configure(text_color="white")

        if select:
            selected_item = self.Appointmenttbl.item(select)
            self.Idsel = selected_item["values"][0]
            self.client_name_var.set(selected_item["values"][1])
            self.date_var.set(selected_item["values"][2])
            self.time_var.set(selected_item["values"][3])
            self.notes_var.set(selected_item["values"][4])

    def edit_appointment(self):
        if not hasattr(self, 'Idsel'):
            messagebox.showwarning("Warning", "Please select an appointment to edit.")
            return

        appi = Blrepository()
        appi.Update(Appointment, self.Idsel, ClientName=self.client_name_var.get(), AppointmentDate=self.date_var.get(),
                    AppointmentTime=self.time_var.get(), Notes=self.notes_var.get())

        selected_id = self.Idsel

        # Clear table
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())

        # Reload data
        self.load_appointments_data(self.Appointmenttbl)

        # Reselect the item
        for item in self.Appointmenttbl.get_children():
            if self.Appointmenttbl.item(item)["values"][0] == selected_id:
                self.Appointmenttbl.selection_set(item)
                break

    def delete_appointment(self):
        if hasattr(self, 'Idsel'):
            a = Blrepository()
            a.Delete(Appointment, self.Idsel)
            self.load_appointments_data(self.Appointmenttbl)
            self.client_name_var.set('')
            self.date_var.set('')
            self.time_var.set('')
            self.notes_var.set('')
            self.ed.delete(0, 'end')
            self.ed.insert(0, 'YYYY-MM-DD')
            self.ed.configure(text_color="gray")

            self.et.delete(0, 'end')
            self.et.insert(0, '12:12')
            self.et.configure(text_color="gray")

            self.ep.delete(0, 'end')
            self.ep.insert(0, '09122395467')
            self.ep.configure(text_color="gray")

    def show_search_frame(self):
        self.search_frame.place(x=500, y=10, width=350, height=200)

    def hide_search_frame(self):
        self.search_frame.place_forget()
        self.load_appointments_data(self.Appointmenttbl)

    def search_appointment(self, event=None):
        search_text = self.search_var.get().strip().lower()
        obj = Blrepository()

        # دریافت رکوردهای فیلتر شده
        filtered_records = obj.Searchappoint(Appointment, search_text)

        # پاک کردن متن پیشنهادات
        self.suggestion_textbox.delete("1.0", "end")

        # افزودن نتایج فیلتر شده به متن پیشنهادات
        for appointment in filtered_records:
            display_text = f"{appointment.Id}: {appointment.ClientName} - {appointment.AppointmentDate} - {appointment.AppointmentTime}\n"
            self.suggestion_textbox.insert("end", display_text)

        # پاک کردن جدول و نمایش داده‌های فیلتر شده
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())
        for appointment in filtered_records:
            self.Appointmenttbl.insert("", "end", values=(
                appointment.Id,
                appointment.ClientName,
                appointment.AppointmentDate,
                appointment.AppointmentTime,
                appointment.Notes
            ))

    def suggest(self, event):
        try:
            # دریافت موقعیت کلیک موس
            index = self.suggestion_textbox.index(f"@{event.x},{event.y}")
            line_start = self.suggestion_textbox.index(f"{index} linestart")
            line_end = self.suggestion_textbox.index(f"{line_start} lineend")

            # استخراج متن خط انتخاب شده
            selected_text = self.suggestion_textbox.get(line_start, line_end).strip()

            if selected_text:
                # استخراج شناسه از متن انتخاب شده
                try:
                    id_part = selected_text.split(' - ')[0]
                    record_id = id_part.split(': ')[1]
                except IndexError:
                    print("خطا در استخراج شناسه. فرمت متن انتخاب شده صحیح نیست.")
                    return

                # دریافت رکورد خاص بر اساس شناسه انتخاب شده
                obj = Blrepository()
                filtered_record = obj.Searchappoint(Appointment, record_id)

                if filtered_record:
                    # پاک کردن جدول قبل از اضافه کردن داده‌های جدید
                    self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())

                    # پر کردن جدول با رکورد خاص
                    for appointment in filtered_record:
                        self.Appointmenttbl.insert(
                            "",
                            "end",
                            values=(
                                appointment.Id,
                                appointment.ClientName,
                                appointment.AppointmentDate,
                                appointment.AppointmentTime,
                                appointment.Notes
                            )
                        )

                    # نمایش رکورد انتخاب شده در فیلدهای ورودی
                    self.client_name_var.set(appointment.ClientName)
                    self.date_var.set(appointment.AppointmentDate)
                    self.time_var.set(appointment.AppointmentTime)
                    self.notes_var.set(appointment.Notes)

                else:
                    print("رکوردی برای شناسه انتخاب شده پیدا نشد.")
            else:
                print("خطا: متن انتخاب شده خالی است.")
        except TclError as e:
            print(f"خطا: {e}")
        except IndexError:
            print("خطا: فرمت متن انتخاب شده اشتباه است.")

    def refreshapp(self):
        self.load_appointments_data(self.Appointmenttbl)

    def c_appointment(self):
        self.appointment_frame.place_forget()

    def English(self):
        pass

    def Persian(self):
        # self.screen.destroy()
        from PL import PersianRegister
        PageMe = PersianRegister.AppPrs(self.screen)

        # screen.mainloop()
