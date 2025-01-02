import pyodbc
from tkinter import *
from customtkinter import CTk
from PL import Register

if __name__ == "__main__":
    screen = CTk()
    screen.geometry("900x900+0+0")  
    screen.iconbitmap("justice.ico")
    screen.title("Law Office")  
    page_me = Register.App(screen) 

    screen.mainloop()
