from tkinter import *
from customtkinter import *
from customtkinter import set_appearance_mode
from tkinter import messagebox
from tkinter import ttk
from BE.Law import low, Appointment, Safe
from BLL.Rules import Blrepository
from datetime import datetime, timedelta


class AppPrs(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.creatwidget()
        self.case_entry = None
        self.Newload()

    def creatwidget(self):
        menubar = Menu(self.screen)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="زبان", menu=filemenu)
        filemenu.add_command(label="انگلیسی", command=self.English)
        filemenu.add_command(label="فارسی", command=self.Persian)
        self.screen.config(menu=menubar)

        set_appearance_mode("dark")

        styleAll = ttk.Style()
        styleAll.theme_use('clam')
        styleAll.configure("TCombobox", background="#3f414d", foreground="black")

        self.menu_bar = Menu(self.screen)
        self.screen.config(menu=self.menu_bar)

        """self.appointment_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="نوبت دهی", menu=self.appointment_menu)
        self.appointment_menu.add_command(label="برنامه‌ریزی نوبت ها", command=self.Newopen_appointment_window)
"""
        self.Language = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="زبان", menu=self.Language)
        self.Language.add_command(label="انگلیسی", command=self.English)
        self.Language.add_command(label="فارسی", command=self.Persian)

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
        self.PartyInLawsuit = StringVar()
        self.CaseStatus = StringVar()
        self.search_var = StringVar()

        self.EntId = Entry(self.screen, textvariable=self.Id)

        self.lblClient = CTkLabel(self.screen, text="اطلاعات موکل", font=("Far.Badr", 35), ).place(x=120, y=10)
        self.LblName = CTkLabel(self.screen, text="نام  کامل", font=("Far.Badr", 22)).place(x=250, y=70)
        self.EntName = CTkEntry(self.screen, textvariable=self.Name, justify='right', width=150, text_color="white",
                                font=("Far.Badr", 16))
        self.EntName.insert(0, "سعیدتوکلی")
        self.EntName.configure(text_color="gray")
        self.EntName.bind("<FocusIn>", self.NewInEntryName)
        self.EntName.bind("<FocusOut>", self.NewOutEntryName)
        self.EntName.place(x=60, y=70)

        self.LblPhone = CTkLabel(self.screen, text="شماره تلفن", font=("Far.Badr", 22)).place(x=250, y=100)
        self.EntPhone = CTkEntry(self.screen, textvariable=self.PhoneNumber, width=150, text_color="white")
        self.EntPhone.insert(0, "09123456789")
        self.EntPhone.configure(text_color="gray")
        self.EntPhone.bind("<FocusIn>", self.NewInEntryPhone)
        self.EntPhone.bind("<FocusOut>", self.NewOutEntryPhone)
        self.EntPhone.place(x=60, y=100)

        self.LblId = CTkLabel(self.screen, text="کد ملی", font=("Far.Badr", 22)).place(x=250, y=130)
        self.EntId = CTkEntry(self.screen, textvariable=self.PersonId, width=150, text_color="white")
        self.EntId.insert(0, "0150148876")
        self.EntId.configure(text_color="gray")
        self.EntId.bind("<FocusIn>", self.NewInEntId)
        self.EntId.bind("<FocusOut>", self.NewOutEntId)
        self.EntId.place(x=60, y=130)

        self.LblAdress = CTkLabel(self.screen, text="آدرس کامل ", font=("Far.Badr", 25)).place(x=250, y=160)
        self.EntAdress = CTkEntry(self.screen, textvariable=self.FullAddress, justify='right', width=150,
                                  text_color="white", font=("Far.Badr", 16))
        self.EntAdress.insert(0, "ایران,تهران,صادقیه")
        self.EntAdress.configure(text_color="gray")
        self.EntAdress.bind("<FocusIn>", self.NewInEntryAddress)
        self.EntAdress.bind("<FocusOut>", self.NewOutEntryAddress)
        self.EntAdress.place(x=60, y=160)

        self.LblJob = CTkLabel(self.screen, text="شغل", font=("Far.Badr", 25)).place(x=250, y=190)
        self.EntJob = CTkEntry(self.screen, textvariable=self.JobTitle, width=150, justify='right', text_color="white",
                               font=("Far.Badr", 16))
        self.EntJob.insert(0, "وکیل")
        self.EntJob.configure(text_color="gray")
        self.EntJob.bind("<FocusIn>", self.NewInEntryJob)
        self.EntJob.bind("<FocusOut>", self.NewOutEntryJob)
        self.EntJob.place(x=60, y=190)
        # یکی از توابعسی که کار نمیکنه مثل تبت نام بیار
        # تابع ثبت نام انگلیسی و دکمه اش رو میاری از کدهای انگلیسیاستاد توی انگلیسی کار نمیکنه فارسی کار میکرد الان
        self.LblFind = CTkLabel(self.screen, text="نحوه آشنایی؟", font=("Far.Badr", 25)).place(x=250, y=220)
        self.EntFind = CTkEntry(self.screen, textvariable=self.HowFindUs, justify='right', width=150,
                                text_color="white", font=("Far.Badr", 16))
        self.EntFind.insert(0, "اجتماعی شبکه")
        self.EntFind.configure(text_color="gray")
        self.EntFind.bind("<FocusIn>", self.NewInEntryFind)
        self.EntFind.bind("<FocusOut>", self.NewOutEntryFind)
        self.EntFind.place(x=60, y=220)

        self.LblType = CTkLabel(self.screen, text="نوع پرونده", font=("Far.Badr", 25)).place(x=250, y=250)
        self.FileType = StringVar()
        self.ComboFileType = ttk.Combobox(self.screen, state="readonly",
                                          values=["پرونده حقوقی", "پرونده کیفری", "پرونده ثبتی", "پرونده خانوادگی",
                                                  "سایر"],
                                          textvariable=self.FileType, justify="right", width=22, font=("Far.Badr", 8))
        self.ComboFileType.place(x=60, y=250)
        self.ComboFileType.bind("<<ComboboxSelected>>", self.Newon_combobox_select)

        self.entry_dict = {
            "پرونده‌های مدنی": (CTkLabel(self.screen, text="نوع پرونده مدنی", justify='right', font=("Far.Badr", 13)),
                                Entry(self.screen, textvariable=self.CaseType, width=150, font=("Far.Badr", 13))),
            "پرونده‌های کیفری": (CTkLabel(self.screen, text="نوع پرونده کیفری", justify='right', font=("Far.Badr", 13)),
                                 Entry(self.screen, textvariable=self.CaseType, width=150, font=("Far.Badr", 13))),
            "پرونده‌های ثبت": (CTkLabel(self.screen, text="نوع پرونده ثبتی", justify='right', font=("Far.Badr", 13)),
                               Entry(self.screen, textvariable=self.CaseType, width=150, font=("Far.Badr", 13))),
            "پرونده‌های خانوادگی": (
            CTkLabel(self.screen, text="نوع پرونده خانوادگی", justify='right', font=("Far.Badr", 12)),
            Entry(self.screen, textvariable=self.CaseType, width=150, font=("Far.Badr", 13))),
            "سایر پرونده‌ها": (CTkLabel(self.screen, text="نوع پرونده", justify='right', font=("Far.Badr", 13)),
                               Entry(self.screen, textvariable=self.CaseType, width=150, font=("Far.Badr", 13))),
        }

        self.LblLawsuit = CTkLabel(self.screen, text="طرفین دعوی", font=("Far.Badr", 25)).place(x=250, y=310)
        self.Lawsuit = StringVar()
        self.ComboLawsuit = ttk.Combobox(self.screen, state="readonly", justify='right',
                                         values=["شخص حقیقی", "شخص حقوقی"], textvariable=self.Lawsuit, width=22,
                                         font=("Far.Badr", 8))
        self.ComboLawsuit.place(x=60, y=310)

        self.LblCase = CTkLabel(self.screen, text="وضعیت پرونده", font=("Far.Badr", 25)).place(x=250, y=340)
        self.Case = StringVar()
        self.ComboCase = ttk.Combobox(self.screen, state="readonly", justify='right',
                                      values=["فقط مشاوره", "حکم صادر شده", "حکم صادر نشده", "قبل از دعوی"],
                                      textvariable=self.Case, width=22, font=("Far.Badr", 8))
        self.ComboCase.place(x=60, y=340)
        # دو متغیر مجزا برای هر گروه رادیو باتن
        self.radio_judgment_issued_var = StringVar(value=" ")
        self.radio_judgment_pending_var = StringVar(value=" ")

        self.radio_buttons = {
            "حکم صادر شده": [
                Radiobutton(self.screen, text="بدوی", variable=self.radio_judgment_issued_var, justify='right',
                            value="بدوی", font=("Far.Badr", 12)),
                Radiobutton(self.screen, text="تجدید نظر", variable=self.radio_judgment_issued_var, justify='right',
                            value="تجدید نظر", font=("Far.Badr", 12))
            ],
            "حکم صادر نشده": [
                Radiobutton(self.screen, text="وکیل دارم", variable=self.radio_judgment_pending_var,
                            font=("Far.Badr", 12),
                            value="وکیل دارم"),
                Radiobutton(self.screen, text="وکیل ندارم", variable=self.radio_judgment_pending_var,
                            font=("Far.Badr", 12),
                            value="وکیل ندارم")
            ]
        }

        self.ComboCase.bind("<<ComboboxSelected>>", self.Newon_case_combobox_select)

        self.LblHistory = CTkLabel(self.screen, text="مراجعات", font=("Far.Badr", 25)).place(x=250, y=430)
        self.History = StringVar()
        self.ComboHistory = ttk.Combobox(self.screen, state="readonly", justify='right', values=["اولین بار", "دیگر"],
                                         textvariable=self.History, width=22)
        self.ComboHistory.place(x=60, y=430)
        self.frametbl = Frame(self.screen)
        self.frametbl.place(x=10, y=470)

        self.scrollbar = Scrollbar(self.frametbl, orient=VERTICAL)

        self.tbl = ttk.Treeview(self.frametbl, columns=(
            "a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8", "a9", "a10", "a11", "a12", "a13", "a14"), show="headings",
                                height=10, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tbl.yview)

        # تعریف اندازه ستون‌ها و نام‌های سرستون به زبان فارسی
        self.tbl.column("a1", width=50)
        self.tbl.heading("a1", text="شناسه")

        self.tbl.column("a2", width=110)
        self.tbl.heading("a2", text="نام کامل")

        self.tbl.column("a3", width=90)
        self.tbl.heading("a3", text="شماره تلفن")

        self.tbl.column("a4", width=70)
        self.tbl.heading("a4", text="شناسه شخص")

        self.tbl.column("a5", width=170)
        self.tbl.heading("a5", text="آدرس کامل")

        self.tbl.column("a6", width=70)
        self.tbl.heading("a6", text="عنوان شغلی")

        self.tbl.column("a7", width=80)
        self.tbl.heading("a7", text="نحوه آشنایی؟")

        self.tbl.column("a8", width=90)
        self.tbl.heading("a8", text="نوع پرونده")

        self.tbl.column("a9", width=90)
        self.tbl.heading("a9", text="نوع دقیق پرونده‌")

        self.tbl.column("a10", width=90)
        self.tbl.heading("a10", text="طرف در دعوی")

        self.tbl.column("a11", width=110)
        self.tbl.heading("a11", text="وضعیت پرونده")

        self.tbl.column("a12", width=110)
        self.tbl.heading("a12", text="حکم صادر شده")

        self.tbl.column("a13", width=125)
        self.tbl.heading("a13", text="حکم صادر نشده")

        self.tbl.column("a14", width=70)
        self.tbl.heading("a14", text="تاریخچه")

        self.tbl.bind("<<TreeviewSelect>>", self.Newget_selection)
        self.tbl.pack(side=LEFT, fill=BOTH, expand=True)

        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.btnSubmit = CTkButton(self.screen, text="ذخیره", fg_color="#3f414d", command=self.Newsubmit_data, width=10)
        self.btnSubmit.place(x=420, y=430)

        self.btnLoad = CTkButton(self.screen, text="ویرایش", fg_color="#3f414d", command=self.Newupdate, width=10)
        self.btnLoad.place(x=520, y=430)

        self.btndelete = CTkButton(self.screen, text="حذف", fg_color="#3f414d", command=self.delete, width=10)
        self.btndelete.place(x=620, y=430)

        self.SearchFrame = Frame(self.screen, width=400, height=300, background="brown")
        self.SearchFrame.place_forget()
        self.btnsearch = CTkButton(self.screen, text="جستجو", fg_color="#3f414d", command=self.NewClicksearch, width=10)
        self.btnsearch.place(x=720, y=430)
        self.bgframe = PhotoImage(file="design.png")
        self.Img = Label(self.SearchFrame, text="*", image=self.bgframe).place(x=0, y=0)
        self.LblSearch = CTkLabel(self.SearchFrame, text="جستجو", font=("Roboto", 15))
        self.LblSearch.place(x=80, y=30)
        self.search = StringVar()
        self.EntSearch = CTkEntry(self.SearchFrame, textvariable=self.search)
        self.EntSearch.place(x=130, y=30)
        self.EntSearch.bind("<KeyRelease>", self.Newsearch)  # اتصال به تابع جستجو

        # جعبه نمایش پیشنهادات
        self.suggestion_listbox = CTkTextbox(self.SearchFrame, width=350, height=150)
        self.suggestion_listbox.place(x=30, y=80)
        self.suggestion_listbox.bind("<ButtonRelease-1>", self.Newon_suggestion_select)  # انتخاب پیشنهاد

        self.btnclose = Button(self.SearchFrame, text="بستن", image=self.icoclose, command=self.NewClickClose).place(
            x=350, y=6)
        self.ButtonReporting = CTkButton(self.screen, text="گزارشات", command=self.NewReporting, fg_color="#961520")
        self.ButtonReporting.place(x=1070, y=430)

        self.frmlogin = Frame(self.screen, bg="#747cd6", width=9000, height=9000)
        self.frmlogin.place(x=0, y=0)
        self.Idshakhsi = StringVar()
        self.Full = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        self.Role = StringVar()

        self.lbluser = CTkLabel(self.frmlogin, text="نام کاربری", font=("Far.Badr", 25, "bold"))
        self.lbluser.place(x=750, y=202)

        self.entuser = CTkEntry(self.frmlogin, textvariable=self.user, width=150)
        self.entuser.insert(0, "Mr.Tavakoli")
        self.entuser.configure(text_color="gray")
        self.entuser.bind("<FocusIn>", self.EnterUserIn)
        self.entuser.bind("<FocusOut>", self.EnterUserOut)
        self.entuser.place(x=580, y=210)

        self.lblpass = CTkLabel(self.frmlogin, text="رمز عبور", font=("Far.Badr", 25, "bold"))
        self.lblpass.place(x=750, y=254)

        self.entpass = CTkEntry(self.frmlogin, textvariable=self.password, show="*", width=150)
        self.entpass.insert(0, "1234")
        self.entpass.configure(text_color="gray")
        self.entpass.bind("<FocusIn>", self.EnterPassIn)
        self.entpass.bind("<FocusOut>", self.EnterPassOut)
        self.entpass.place(x=580, y=260)

        self.Btnlogin = CTkButton(self.frmlogin, text="ورود", command=self.NewLog, fg_color="#3f414d")
        self.Btnlogin.place(x=400, y=500)

        self.entuser.bind("<Return>", self.Newforshow)
        self.entpass.bind("<Return>", self.Newlogin_focus)

        self.frmlogin.bind("<Map>", self.Newon_entry_click)

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

    def NewReporting(self):
        # ایجاد یک frame جدید برای نمایش جدول
        self.report_frame = Frame(self.screen, background="#3b161a", width=640, height=400)
        self.report_frame.place(x=300, y=80)
        self.ButClose = Button(self.report_frame, text="بستن", command=self.Newreportclose)
        self.ButClose.place(x=600, y=10)

        # تنظیمات جدول (Treeview)
        self.tree_report = ttk.Treeview(self.report_frame, columns=('a1', 'a2'), show='headings', height=10)

        self.tree_report.column('a1', width=150)
        self.tree_report.heading('a1', text='نام کامل')
        self.tree_report.column('a2', width=150)
        self.tree_report.heading('a2', text='حکم صادر شده')

        # استفاده از place برای جایگذاری جدول
        self.tree_report.place(x=10, y=10, width=580, height=380)

        # بازیابی اطلاعات از دیتابیس
        self.Newload_reporting_data()

    def Newload_reporting_data(self):
        # دیکشنری برای ترجمه
        translation_dict = {
            "First Instance": "بدوی",
            "Appeal": "تجدید نظر",
            "Final Judgment": "نهایی",
            # اضافه کردن سایر ترجمه‌های مورد نیاز
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

    def Newreportclose(self):
        self.report_frame.place_forget()

    def Newon_entry_click(self, e):
        self.entuser.focus_set()

    def NewInEntryName(self, e):
        if self.EntName.get() == "سعیدتوکلی":
            self.EntName.delete(0, "end")
            self.EntName.configure(text_color="white")

    def NewOutEntryName(self, e):
        if self.EntName.get() == "":
            self.EntName.insert(0, "سعیدتوکلی")
            self.EntName.configure(text_color="gray")

    def NewInEntryPhone(self, e):
        if self.EntPhone.get() == "09123456789":
            self.EntPhone.delete(0, "end")
            self.EntPhone.configure(text_color="white")

    def NewOutEntryPhone(self, e):
        if self.EntPhone.get() == "":
            print("out ok")
            self.EntPhone.insert(0, "09123456789")
            self.EntPhone.configure(text_color="gray")

    def NewInEntId(self, e):
        if self.EntId.get() == "0150148876":
            self.EntId.delete(0, "end")
            self.EntId.configure(text_color="white")

    def NewOutEntId(self, e):
        if self.EntId.get() == "":
            self.EntId.insert(0, "0150148876")
            self.EntId.configure(text_color="gray")

    def NewInEntryAddress(self, e):
        if self.EntAdress.get() == "ایران,تهران,صادقیه":
            self.EntAdress.delete(0, "end")
            self.EntAdress.configure(text_color="white")

    def NewOutEntryAddress(self, e):
        if self.EntAdress.get() == "":
            self.EntAdress.insert(0, "ایران,تهران,صادقیه")
            self.EntAdress.configure(text_color="gray")

    def NewInEntryJob(self, e):
        if self.EntJob.get() == "وکیل":
            self.EntJob.delete(0, "end")
            self.EntJob.configure(text_color="white")

    def NewOutEntryJob(self, e):
        if self.EntJob.get() == "":
            self.EntJob.insert(0, "وکیل")
            self.EntJob.configure(text_color="gray")

    def NewInEntryFind(self, e):
        if self.EntFind.get() == "اجتماعی شبکه":
            self.EntFind.delete(0, "end")
            self.EntFind.configure(text_color="white")

    def NewOutEntryFind(self, e):
        if self.EntFind.get() == "":
            self.EntFind.insert(0, "اجتماعی شبکه")
            self.EntFind.configure(text_color="gray")

    def Newforshow(self, e):
        self.entpass.focus_set()

    def Newlogin_focus(self, e):
        self.Btnlogin.invoke()

    def NewLog(self):
        print("NewLog function is triggered")
        new = Safe("", self.user.get(), self.password.get(), "")
        ob = Blrepository()
        res = ob.vasl(Safe, new)

        print("Result from vasl:", res)
        print("Result type:", type(res))  # چاپ نوع داده

        if not res:
            messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه است!")
        else:
            # چاپ ویژگی‌های شیء برای بررسی
            print("Role:", getattr(res, 'Role', 'N/A'))
            print("FullName:", getattr(res, 'FullName', 'N/A'))

            if res.Role == "کارمند":
                self.frmlogin.place_forget()
                print("کارمند وارد شده است")
                self.appointment_menu = Menu(self.menu_bar, tearoff=0)
                self.menu_bar.add_cascade(label="نوبت دهی", menu=self.appointment_menu)
                self.appointment_menu.add_command(label="برنامه‌ریزی نوبت ها", command=self.Newopen_appointment_window)

            elif res.Role == "مدیر":
                self.frmlogin.place_forget()
                btn_add_member = CTkButton(self.screen, text="افزودن عضو", command=self.Newadd_member,
                                           fg_color="#3f414d", width=25)
                btn_add_member.place(x=815, y=430)
                self.appointment_menu = Menu(self.menu_bar, tearoff=0)
                self.menu_bar.add_cascade(label="نوبت دهی", menu=self.appointment_menu)
                self.appointment_menu.add_command(label="برنامه‌ریزی نوبت ها", command=self.Newopen_appointment_window)

    def Newadd_member(self):
        self.add_member_frame = Frame(self.screen, bg="darkblue")
        self.add_member_frame.place(x=0, y=0, width=700, height=500)

        # تعریف متغیرها
        self.Id = StringVar()
        self.name = StringVar()
        self.user = StringVar()
        self.password = StringVar()
        self.Role = StringVar()
        self.search_member_var = StringVar()

        # لیبل و ورودی برای نام کارمند
        self.lbl_name = CTkLabel(self.add_member_frame, text="نام کامل", font=("Far.Badr", 20))
        self.lbl_name.place(x=180, y=20)
        self.ent_name = CTkEntry(self.add_member_frame, textvariable=self.name, width=145, justify='right',
                                 font=("Far.Badr", 14))
        self.ent_name.insert(0, "سعید توکلی")
        self.ent_name.configure(text_color="gray")
        self.ent_name.bind("<FocusIn>", self.FullIn)
        self.ent_name.bind("<FocusOut>", self.FullOut)
        self.ent_name.place(x=20, y=20)

        # لیبل و ورودی برای نام کاربری
        self.lbl_username = CTkLabel(self.add_member_frame, text="نام کاربری", font=("Far.Badr", 20))
        self.lbl_username.place(x=180, y=60)
        self.ent_username = CTkEntry(self.add_member_frame, textvariable=self.user, width=145)
        self.ent_username.insert(0, "Mr.Tavakoli")
        self.ent_username.configure(text_color="gray")
        self.ent_username.bind("<FocusIn>", self.EntUserIn)
        self.ent_username.bind("<FocusOut>", self.EntUserOut)
        self.ent_username.place(x=20, y=60)

        # لیبل و ورودی برای رمز عبور
        self.lbl_password = CTkLabel(self.add_member_frame, text="رمز عبور", font=("Far.Badr", 20))
        self.lbl_password.place(x=180, y=100)
        self.ent_password = CTkEntry(self.add_member_frame, textvariable=self.password, width=145)
        self.ent_password.insert(0, "1234")
        self.ent_password.configure(text_color="gray")
        self.ent_password.bind("<FocusIn>", self.EntPassIn)
        self.ent_password.bind("<FocusOut>", self.EntPassOut)
        self.ent_password.place(x=20, y=100)

        # لیبل و ورودی برای نقش
        self.lbl_role = CTkLabel(self.add_member_frame, text="نقش", font=("Far.Badr", 20))
        self.lbl_role.place(x=180, y=140)
        self.ComboRole = ttk.Combobox(self.add_member_frame, state="readonly", values=["مدیر", "کارمند"],
                                      textvariable=self.Role)
        self.ComboRole.place(x=20, y=140)

        # جدول برای نمایش اطلاعات
        self.frmscr = Frame(self.add_member_frame)
        self.frmscr.place(x=300, y=60)
        self.scr = Scrollbar(self.frmscr, orient=VERTICAL)
        self.tbl_members = ttk.Treeview(self.frmscr, columns=("#1", "#2", "#3", "#4", "#5"), show="headings",
                                        height=20, yscrollcommand=self.scrollbar.set)
        self.scr.config(command=self.tbl_members.yview)
        self.tbl_members.column("#1", width=50)
        self.tbl_members.heading("#1", text="شناسه")
        self.tbl_members.column("#2", width=110)
        self.tbl_members.heading("#2", text="نام کامل")
        self.tbl_members.column("#3", width=75)
        self.tbl_members.heading("#3", text="نام کاربری")
        self.tbl_members.column("#4", width=75)
        self.tbl_members.heading("#4", text="رمز عبور")
        self.tbl_members.column("#5", width=70)
        self.tbl_members.heading("#5", text="نقش")
        self.tbl_members.pack(side=LEFT, fill=BOTH, expand=True)
        self.tbl_members.bind("<<TreeviewSelect>>", self.NewGetselectionadd)
        self.Newload_members_data(self.tbl_members)
        self.scr.pack(side=RIGHT, fill=Y)
        # دکمه‌ها
        btn_add = CTkButton(self.add_member_frame, text="افزودن عضو", fg_color="#3f414d", command=self.Newaddbox,
                            width=7)
        btn_add.place(x=0, y=200)
        btn_update = CTkButton(self.add_member_frame, text="بروزرسانی", command=self.Newupdatebox, fg_color="#3f414d",
                               width=7)
        btn_update.place(x=100, y=200)
        btn_delete = CTkButton(self.add_member_frame, text="حذف", command=self.Newdelete_member, fg_color="#3f414d",
                               width=7)
        btn_delete.place(x=172, y=200)
        self.sbutton = CTkButton(self.add_member_frame, text="جستجو", command=self.Newsearch_framemember,
                                 fg_color="#3f414d", width=7)
        self.sbutton.place(x=238, y=200)
        btn_close = Button(self.add_member_frame, text="بستن", image=self.icoclose, command=self.NewTclose).place(x=640,
                                                                                                                  y=10)

        # فریم جستجو
        self.search_member_frame = Frame(self.add_member_frame, bg="lightgray", padx=10, pady=10)
        self.search_member_frame.place_forget()
        self.lblsearch = CTkLabel(self.search_member_frame, text="جستجو", text_color="black", font=("Roboto", 15))
        self.lblsearch.place(x=5, y=20)
        self.entsearch = CTkEntry(self.search_member_frame, textvariable=self.search_member_var, width=150)
        self.entsearch.place(x=80, y=20)
        self.suggestion_textbox = CTkTextbox(self.search_member_frame, width=260, height=300)
        self.suggestion_textbox.place(x=10, y=50)
        self.suggestion_textbox.bind("<ButtonRelease-1>", self.Newsuggestion_member)
        self.entsearch.bind("<KeyRelease>", self.Newsearch_automember)
        self.bclose = Button(self.search_member_frame, text="بستن", image=self.icoclose, command=self.Newsearchclose)
        self.bclose.place(x=250, y=6)

    def FullIn(self, e):
        if self.ent_name.get() == "سعید توکلی":
            self.ent_name.delete(0, "end")
            self.ent_name.configure(text_color="white")

    def FullOut(self, e):
        if self.ent_name.get() == "":
            self.ent_name.insert(0, "سعید توکلی")
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

    def Newaddbox(self):
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

    def Newload_members_data(self, treeview):
        # بارگذاری اطلاعات از دیتابیس
        ob = Blrepository()
        members = ob.Read(Safe)  # فرض می‌کنیم متد Read تمام اعضا را بازمی‌گرداند

        # پاک‌سازی جدول قبل از بارگذاری مجدد داده‌ها
        for row in treeview.get_children():
            treeview.delete(row)

        # نمایش اطلاعات در جدول
        for member in members:
            treeview.insert("", END, values=(member.Id, member.FullName, member.UserName, member.Password, member.Role))

    def Newupdatebox(self):
        obj = Blrepository()
        obj.Update(Safe, self.Idsel, FullName=self.ent_name.get(), UserName=self.ent_username.get(),
                   Password=self.ent_password.get(), Role=self.ComboRole.get())
        self.Newload_members_data(self.tbl_members)

    def NewGetselectionadd(self, event):
        # دریافت آیتم‌های انتخاب‌شده
        selected_item = self.tbl_members.selection()
        self.ent_name.configure(text_color="white")
        self.ent_username.configure(text_color="white")
        self.ent_password.configure(text_color="white")
        if not selected_item:
            return

        # دریافت مقادیر از آیتم انتخاب‌شده
        item_values = self.tbl_members.item(selected_item)["values"]

        # بررسی طول مقادیر برای جلوگیری از خطا
        if len(item_values) >= 5:
            self.Idsel = item_values[0]
            self.Id.set(self.Idsel)
            self.namesel = item_values[1]
            self.name.set(self.namesel)
            self.usersel = item_values[2]
            self.user.set(self.usersel)
            self.passsel = item_values[3]
            self.password.set(self.passsel)
            self.Rolesel = item_values[4]
            self.Role.set(self.Rolesel)

    def Newdelete_member(self):
        j = Blrepository()
        j.Delete(Safe, self.Idsel)
        self.Newload_members_data(self.tbl_members)
        self.name.set('')
        self.user.set('')
        self.password.set('')
        self.Role.set('')

    def Newsearch_framemember(self):
        self.search_member_frame.place(x=0, y=240, width=300, height=250)

    def Newsearch_automember(self, event=None):
        """جستجو در پایگاه داده و به‌روزرسانی جدول و پیشنهادات"""
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

    def Newsuggestion_member(self, event):
        try:
            # دریافت مختصات کلیک
            index = self.suggestion_textbox.index(f"@{event.x},{event.y}")

            # یافتن خط کامل در محل کلیک
            selected_line = self.suggestion_textbox.get(f"{index} linestart", f"{index} lineend")

            if selected_line:
                # بررسی فرمت مورد انتظار
                parts = selected_line.split(" - ")
                if len(parts) > 1:
                    selected_id = parts[0].strip()

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
                        self.NewGetselectionadd(None)
                    else:
                        print("داده‌ای با شناسه انتخاب‌شده یافت نشد")
                else:
                    print("فرمت داده انتخاب‌شده معتبر نیست")
            else:
                print("خطی انتخاب نشده است")
        except Exception as e:
            print(f"خطا: {e}")

    def Newsearchclose(self):
        self.search_member_frame.place_forget()
        self.Newload_members_data(self.tbl_members)

    def NewTclose(self):
        self.add_member_frame.place_forget()

    def Newon_combobox_select(self, event):
        self.selected_value = self.ComboFileType.get()

        # حذف لیبل و ورودی قبلی اگر وجود داشته باشد
        if hasattr(self, 'current_label') and self.current_label is not None:
            self.current_label.destroy()
            self.current_label = None

        if hasattr(self, 'case_entry') and self.case_entry is not None:
            self.case_entry.destroy()
            self.case_entry = None

        if self.selected_value == "پرونده حقوقی":
            self.current_label = CTkLabel(self.screen, text="نوع پرونده حقوقی", font=("Far.Badr", 18))
            self.current_label.place(x=250, y=280)
            self.case_entry = CTkEntry(self.screen, width=150, justify='right', font=("Far.Badr", 15))
            self.case_entry.place(x=60, y=280)

        elif self.selected_value == "پرونده کیفری":
            self.current_label = CTkLabel(self.screen, text="نوع پرونده کیفری", font=("Far.Badr", 18))
            self.current_label.place(x=250, y=280)
            self.case_entry = CTkEntry(self.screen, width=150, justify='right', font=("Far.Badr", 15))
            self.case_entry.place(x=60, y=280)

        elif self.selected_value == "پرونده ثبتی":
            self.current_label = CTkLabel(self.screen, text="نوع پرونده ثبتی", font=("Far.Badr", 18))
            self.current_label.place(x=250, y=280)
            self.case_entry = CTkEntry(self.screen, width=150, justify='right', font=("Far.Badr", 15))
            self.case_entry.place(x=60, y=280)

        elif self.selected_value == "پرونده خانوادگی":
            self.current_label = CTkLabel(self.screen, text="نوع پرونده خانوادگی", font=("Far.Badr", 18))
            self.current_label.place(x=250, y=280)
            self.case_entry = CTkEntry(self.screen, width=150, justify='right', font=("Far.Badr", 15))
            self.case_entry.place(x=60, y=280)

        elif self.selected_value == "سایر":
            self.current_label = CTkLabel(self.screen, text="نوع پرونده", font=("Far.Badr", 18))
            self.current_label.place(x=250, y=280)
            self.case_entry = CTkEntry(self.screen, width=150, justify='right', font=("Far.Badr", 15))
            self.case_entry.place(x=60, y=280)

    def Newon_case_combobox_select(self, event):
        selected_case = self.ComboCase.get()

        # پنهان کردن تمام رادیو باتن‌ها
        for radiobutton_list in self.radio_buttons.values():
            for radiobutton in radiobutton_list:
                radiobutton.place_forget()

        # نمایش رادیو باتن‌های مرتبط با گزینه انتخاب‌شده
        if selected_case in self.radio_buttons:
            y_position = 370
            for radiobutton in self.radio_buttons[selected_case]:
                radiobutton.place(x=60, y=y_position)
                y_position += 30

        # چاپ مقادیر برای بررسی
        self.check_radio_buttons()

    def Newsubmit_data(self):
        id = self.Id.get()
        name = self.EntName.get()
        phone = self.EntPhone.get()
        person_id = self.EntId.get()
        address = self.EntAdress.get()
        job_title = self.EntJob.get()
        how_find_us = self.EntFind.get()
        file_type = self.FileType.get()

        case_type = self.case_entry.get() if self.case_entry else ""

        party_lawsuit = self.Lawsuit.get()
        case_status = self.Case.get()

        # تنظیم مقدار انتخاب‌شده برای رادیو باتن‌ها با استفاده از متغیرهای مجزا
        radio_choice_issued = ""
        radio_choice_pending = ""

        if case_status == "حکم صادر شده":
            radio_choice_issued = self.radio_judgment_issued_var.get()  # متغیر مربوط به حکم صادر شده
        elif case_status == "حکم صادر نشده":
            radio_choice_pending = self.radio_judgment_pending_var.get()  # متغیر مربوط به حکم صادر نشده

        history = self.History.get()

        # ایجاد رکورد جدید برای جدول
        new_record = low(
            FullName=name,
            PhoneNumber=phone,
            PersonId=person_id,
            FullAddress=address,
            JobTitle=job_title,
            HowFindUs=how_find_us,
            FileType=file_type,
            CaseType=case_type,
            PartyInLawsuit=party_lawsuit,
            CaseStatues=case_status,
            JudgmentIssued=radio_choice_issued if case_status == "حکم صادر شده" else "",
            JudgmentPending=radio_choice_pending if case_status == "حکم صادر نشده" else "",
            History=history
        )

        # افزودن رکورد جدید به دیتابیس
        obj = Blrepository()
        obj.AddRegister(new_record)

        # بارگذاری مجدد جدول پس از افزودن رکورد جدید
        self.Newload()

    def Newload(self):

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

    def Newupdate(self):
        if not hasattr(self, 'Idrow'):
            print("هیچ رکوردی انتخاب نشده است.")
            return
        # ادامه عملیات آپدیت
        obj = Blrepository()
        obj.Update(low, self.Idrow, FullName=self.EntName.get(),
                   PhoneNumber=self.EntPhone.get(),
                   PersonId=self.EntId.get(),
                   FullAddress=self.EntAdress.get(),
                   JobTitle=self.EntJob.get(),
                   HowFindUs=self.EntFind.get(),
                   FileType=self.ComboFileType.get(),
                   CaseType=self.case_entry.get() if hasattr(self, 'case_entry') else "",
                   PartyInLawsuit=self.Lawsuit.get(),
                   CaseStatues=self.Case.get(),
                   JudgmentIssued=self.radio_judgment_issued_var.get() if self.Case.get() == "حکم صادر شده" else "",
                   JudgmentPending=self.radio_judgment_pending_var.get() if self.Case.get() == "حکم صادر نشده" else "",
                   History=self.History.get()
                   )
        self.Newload()

    def Newget_selection(self, event):
        select = self.tbl.selection()  # انتخاب سطر از جدول
        self.EntName.configure(text_color="white")
        self.EntPhone.configure(text_color="white")
        self.EntId.configure(text_color="white")
        self.EntAdress.configure(text_color="white")
        self.EntJob.configure(text_color="white")
        self.EntFind.configure(text_color="white")

        if select:
            self.Idrow = self.tbl.item(select)["values"][0]
            self.Id.set(self.Idrow)

            # سایر مقادیر را از جدول دریافت کنید
            Namerow = self.tbl.item(select)["values"][1]
            self.Name.set(Namerow)

            Phonerow = self.tbl.item(select)["values"][2]
            self.PhoneNumber.set(Phonerow)

            Personrow = self.tbl.item(select)["values"][3]
            self.PersonId.set(Personrow)

            Addressrow = self.tbl.item(select)["values"][4]
            self.FullAddress.set(Addressrow)

            Jobrow = self.tbl.item(select)["values"][5]
            self.JobTitle.set(Jobrow)

            Howrow = self.tbl.item(select)["values"][6]
            self.HowFindUs.set(Howrow)

            Typerow = self.tbl.item(select)["values"][7]
            self.FileType.set(Typerow)

            self.ComboFileType.set(Typerow)
            self.Newon_combobox_select(None)

            Caserow = self.tbl.item(select)["values"][8]
            if self.case_entry:
                self.case_entry.delete(0, 'end')
                self.case_entry.insert(0, Caserow)

            Lowsuiterow = self.tbl.item(select)["values"][9]
            self.Lawsuit.set(Lowsuiterow)

            Statusrow = self.tbl.item(select)["values"][10]
            self.CaseStatus.set(Statusrow)
            self.ComboCase.set(Statusrow)
            self.Newon_case_combobox_select(None)

            # تنظیم رادیو باتن‌ها بر اساس وضعیت
            if Statusrow == "حکم صادر شده":
                RadioChoice = self.tbl.item(select)["values"][11].strip()  # از strip() برای حذف فاصله‌ها استفاده کنید
                self.radio_judgment_issued_var.set(RadioChoice)  # برای حکم صادر شده

                for radiobutton in self.radio_buttons["حکم صادر شده"]:
                    if radiobutton.cget("value") == RadioChoice:
                        radiobutton.select()
                    else:
                        radiobutton.deselect()

            elif Statusrow == "حکم صادر نشده":
                test = self.tbl.item(select)["values"][12].strip()  # از strip() برای حذف فاصله‌ها استفاده کنید
                RadioChoice = test
                self.radio_judgment_pending_var.set(RadioChoice)  # برای حکم صادر نشده

                for radiobutton in self.radio_buttons["حکم صادر نشده"]:
                    rbtn = radiobutton.cget("value")
                    if rbtn == RadioChoice:
                        radiobutton.select()
                    else:
                        radiobutton.deselect()
            self.check_radio_buttons()

            Historyrow = self.tbl.item(select)["values"][13]
            self.History.set(Historyrow)

    def check_radio_buttons(self):
        print("Issued Radio Value:", self.radio_judgment_issued_var.get())
        print("Pending Radio Value:", self.radio_judgment_pending_var.get())

    def Newsearch(self, event=None):
        text_search = self.search.get().strip().lower()

        # پاک کردن لیست پیشنهادات
        self.suggestion_listbox.delete("1.0", "end")

        obj = Blrepository()
        results = obj.Search(low, text_search)

        if hasattr(self, 'tbl') and self.tbl:
            for row in self.tbl.get_children():
                self.tbl.delete(row)

        for record in results:
            self.tbl.insert(
                "",
                "end",
                values=(record.Id,
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
                        record.History.strip())
            )

        for record in results:
            suggestion_text = f"{record.Id} - {record.FullName.strip()}\n"
            self.suggestion_listbox.insert("end", suggestion_text)

    def Newon_suggestion_select(self, event):
        # دریافت مکان کلیک شده
        index = self.suggestion_listbox.index("@%s,%s" % (event.x, event.y))

        # دریافت متن انتخاب شده از مکان کلیک شده
        selected_line = self.suggestion_listbox.get("1.0", "end-1c").split('\n')
        for i, line in enumerate(selected_line):
            if i + 1 == int(index.split('.')[0]):
                selected_text = line.strip()
                break

        if " - " in selected_text:
            # استخراج شناسه و نام از متن انتخاب شده
            suggestion_id, suggestion_name = selected_text.split(" - ", 1)

            # تنظیم نام در جستجو
            self.search.set(suggestion_name.strip())

            # اجرای جستجو جدید برای به‌روز کردن جدول
            self.Newsearch()

    def delete(self):
        j = Blrepository()
        j.Delete(low, self.Idrow)
        self.Newload()

        # پاک کردن داده‌ها از اینتری‌ها و کمبوباکس‌ها

        self.Id.set('')
        self.EntName.delete(0, 'end')  # پاک کردن محتوای CTkEntry
        self.EntPhone.delete(0, 'end')
        self.EntId.delete(0, 'end')
        self.EntAdress.delete(0, 'end')
        self.EntJob.delete(0, 'end')
        self.EntFind.delete(0, 'end')
        self.FileType.set('')
        self.case_entry.delete(0, 'end')  # پاک کردن محتوای کمبوباکس
        self.Lawsuit.set('')
        self.Case.set('')
        self.CaseType.set('')
        if hasattr(self, 'radio_buttons'):
            for radiobutton_list in self.radio_buttons.values():
                for radiobutton in radiobutton_list:
                    radiobutton.place_forget()
        self.History.set('')

    def NewClicksearch(self):
        self.SearchFrame.place(x=380, y=10)

    def NewClickClose(self):
        self.SearchFrame.place_forget()
        self.Newload()

    def Newopen_appointment_window(self):
        self.appointment_frame = Frame(self.screen, bg="#329da8")
        self.appointment_frame.place(x=20, y=20, width=860, height=550)

        # فیلدهای ورودی برای جزئیات قرار ملاقات
        self.client_name_var = StringVar()
        self.date_var = StringVar()
        self.time_var = StringVar()
        self.notes_var = StringVar()

        self.en = CTkLabel(self.appointment_frame, text="نام مشتری", text_color="black", font=("Far.Badr", 15)).place(
            x=300, y=20)
        self.en = CTkEntry(self.appointment_frame, textvariable=self.client_name_var, justify='right', width=250).place(
            x=20, y=20)

        CTkLabel(self.appointment_frame, text="تاریخ قرار ملاقات", text_color="black", font=("Far.Badr", 15)).place(
            x=300,
            y=60)
        self.ed = CTkEntry(self.appointment_frame, textvariable=self.date_var, width=250)
        self.ed.insert(0, "YYYY-MM-DD")
        self.ed.configure(text_color="gray")
        self.ed.bind("<FocusIn>", self.NewDateIn)
        self.ed.bind("<FocusOut>", self.NewDateOut)
        self.ed.place(x=20, y=60)

        self.et = CTkLabel(self.appointment_frame, text="زمان قرار ملاقات", text_color="black",
                           font=("Far.Badr", 15)).place(x=300,
                                                        y=100)
        self.et = CTkEntry(self.appointment_frame, textvariable=self.time_var, width=250)
        self.et.insert(0, "12:12")
        self.et.configure(text_color="gray")
        self.et.bind("<FocusIn>", self.TimeIn)
        self.et.bind("<FocusOut>", self.TimeOut)
        self.et.place(x=20, y=100)

        self.ep = CTkLabel(self.appointment_frame, text="تلفن", text_color="black", font=("Far.Badr", 15)).place(x=300,
                                                                                                                 y=140)
        self.ep = CTkEntry(self.appointment_frame, textvariable=self.notes_var, width=250)
        self.ep.insert(0, "09122395467")
        self.ep.configure(text_color="gray")
        self.ep.bind("<FocusIn>", self.PhoneIn)
        self.ep.bind("<FocusOut>", self.PhoneOut)
        self.ep.place(x=20, y=140)

        CTkButton(self.appointment_frame, text="ذخیره", command=self.Newsave_appointment, fg_color="#3f414d",
                  width=7).place(x=150, y=180)
        CTkButton(self.appointment_frame, text="ویرایش", command=self.Newedit_appointment, fg_color="#3f414d",
                  width=7).place(x=220, y=180)
        CTkButton(self.appointment_frame, text="حذف", command=self.Newdelete_appointment, fg_color="#3f414d",
                  width=9).place(x=290, y=180)
        CTkButton(self.appointment_frame, text="جستجو", command=self.Newshow_search_frame, fg_color="#3f414d",
                  width=9).place(x=367, y=180)
        CTkButton(self.appointment_frame, text="فردا", command=self.Newshow_date, fg_color="#3f414d", width=9).place(
            x=530,
            y=180)
        CTkButton(self.appointment_frame, text="امروز", command=self.Newshow_Today_date, fg_color="#3f414d",
                  width=9).place(x=440, y=180)
        self.appointment_close = Button(self.appointment_frame, text="بستن", image=self.icoclose,
                                        command=self.Newc_appointment)
        self.appointment_close.place(x=800, y=10)
        self.refreshappointment = CTkButton(self.appointment_frame, text="جدول بروزرسانی", command=self.Newrefreshapp,
                                            fg_color="#3f414d", width=10)
        self.refreshappointment.place(x=600, y=180)

        # Treeview برای نمایش قرار ملاقات‌ها
        self.frmappoint = Frame(self.appointment_frame)
        self.frmappoint.place(x=18, y=220, relwidth=0.95, relheight=0.6)
        self.scrappoint = Scrollbar(self.frmappoint, orient=VERTICAL)
        self.Appointmenttbl = ttk.Treeview(self.frmappoint, columns=("a1", "a2", "a3", "a4", "a5"),
                                           show="headings", height=10, yscrollcommand=self.scrollbar.set)
        self.scrappoint.config(command=self.Appointmenttbl.yview)
        self.Appointmenttbl.column("a1", width=50)
        self.Appointmenttbl.heading("a1", text="شناسه")
        self.Appointmenttbl.column("a2", width=50)
        self.Appointmenttbl.heading("a2", text="نام کامل")
        self.Appointmenttbl.column("a3", width=50)
        self.Appointmenttbl.heading("a3", text="تاریخ")
        self.Appointmenttbl.column("a4", width=50)
        self.Appointmenttbl.heading("a4", text="زمان")
        self.Appointmenttbl.column("a5", width=50)
        self.Appointmenttbl.heading("a5", text="تلفن")
        self.Appointmenttbl.pack(side=LEFT, fill=BOTH, expand=True)
        self.Appointmenttbl.bind("<<TreeviewSelect>>", self.Newon_appointment_select)
        self.scrappoint.pack(side=RIGHT, fill=Y)

        self.Newload_appointments_data(self.Appointmenttbl)

        # ایجاد فریم جستجو
        self.search_frame = Frame(self.appointment_frame, bg="#0d6069")
        CTkLabel(self.search_frame, text="جستجو", font=("Far.Badr", 15)).place(x=20, y=20)
        self.entsearch = CTkEntry(self.search_frame, textvariable=self.search_var, width=150)
        self.entsearch.place(x=80, y=20)
        self.mamsearch_close = Button(self.search_frame, text="بستن", image=self.icoclose,
                                      command=self.Newhide_search_frame)
        self.mamsearch_close.place(x=300, y=10)
        self.suggestion_textbox = CTkTextbox(self.search_frame, width=300, height=140)
        # start_index = self.suggestion_listbox.index("sel.first")
        self.suggestion_textbox.place(x=30, y=55)
        self.suggestion_textbox.bind('<ButtonRelease-1>', self.Newsuggest)
        self.entsearch.bind('<KeyRelease>', self.Newsearch_appointment)

    def NewDateIn(self, e):
        if self.ed.get() == "YYYY-MM-DD":
            self.ed.delete(0, "end")
            self.ed.configure(text_color="white")

    def NewDateOut(self, e):
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

    def Newshow_Today_date(self):
        today = datetime.now().date()
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())
        for item in self.appointments:
            if item.AppointmentDate == today.strftime("%Y-%m-%d"):
                self.Appointmenttbl.insert("", "end", values=(
                    item.Id, item.ClientName, item.AppointmentDate, item.AppointmentTime,
                    item.Notes))

    def Newshow_date(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(days=1)
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())
        for item in self.appointments:
            if item.AppointmentDate == tomorrow.strftime("%Y-%m-%d"):
                self.Appointmenttbl.insert("", "end", values=(
                    item.Id, item.ClientName, item.AppointmentDate, item.AppointmentTime,
                    item.Notes))

    def Newsave_appointment(self):
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

        # پاک کردن جدول و بارگذاری مجدد داده‌ها
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())
        self.Newload_appointments_data(self.Appointmenttbl)

    def Newload_appointments_data(self, Appointmenttbl):
        obj = Blrepository()
        self.appointments = obj.Read(Appointment)

        # پاک کردن داده‌های موجود در جدول
        Appointmenttbl.delete(*Appointmenttbl.get_children())

        for appointment in self.appointments:
            Appointmenttbl.insert("", "end", values=(
                appointment.Id, appointment.ClientName, appointment.AppointmentDate, appointment.AppointmentTime,
                appointment.Notes))

    def Newon_appointment_select(self, event):
        selected_item = self.Appointmenttbl.selection()
        self.ed.configure(text_color="white")
        self.et.configure(text_color="white")
        self.ep.configure(text_color="white")

        if selected_item:
            item = self.Appointmenttbl.item(selected_item[0])  # اولین انتخاب را بگیرید
            values = item["values"]

            if values:  # چک کنید که رکورد خالی نباشد
                self.Idsel = values[0]  # شناسه انتخاب شده
                self.client_name_var.set(values[1])  # تنظیم فیلد نام مشتری
                self.date_var.set(values[2])  # تنظیم فیلد تاریخ
                self.time_var.set(values[3])  # تنظیم فیلد زمان
                self.notes_var.set(values[4])  # تنظیم فیلد توضیحات

    def Newedit_appointment(self):
        if not hasattr(self, 'Idsel'):
            messagebox.showwarning("هشدار", "لطفاً یک قرار ملاقات برای ویرایش انتخاب کنید.")
            return

        appi = Blrepository()
        appi.Update(Appointment, self.Idsel, ClientName=self.client_name_var.get(), AppointmentDate=self.date_var.get(),
                    AppointmentTime=self.time_var.get(), Notes=self.notes_var.get())

        selected_id = self.Idsel

        # پاک کردن جدول
        self.Appointmenttbl.delete(*self.Appointmenttbl.get_children())

        # بارگذاری مجدد داده‌ها
        self.Newload_appointments_data(self.Appointmenttbl)

        # انتخاب مجدد آیتم
        for item in self.Appointmenttbl.get_children():
            if self.Appointmenttbl.item(item)["values"][0] == selected_id:
                self.Appointmenttbl.selection_set(item)
                break

    def Newdelete_appointment(self):
        if hasattr(self, 'Idsel'):
            a = Blrepository()
            a.Delete(Appointment, self.Idsel)
            self.Newload_appointments_data(self.Appointmenttbl)
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

    def Newshow_search_frame(self):
        self.search_frame.place(x=500, y=10, width=350, height=200)

    def Newhide_search_frame(self):
        self.search_frame.place_forget()
        self.Newload_appointments_data(self.Appointmenttbl)

    def Newsearch_appointment(self, event=None):
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
                appointment.Id, appointment.ClientName, appointment.AppointmentDate, appointment.AppointmentTime,
                appointment.Notes
            ))

    def Newsuggest(self, event):
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

    def Newrefreshapp(self):
        self.Newload_appointments_data(self.Appointmenttbl)

    def Newc_appointment(self):
        self.appointment_frame.place_forget()

    def English(self):
        # self.screen.destroy()
        from PL import Register
        PageMe = Register.App(self.screen)

        # screen.mainloop()

    def Persian(self):
        pass
