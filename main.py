import os
import customtkinter as ctk
from tkinter import StringVar
from tkinter import filedialog

#Внешний вид
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

#Окно
app = ctk.CTk()
app.title("CHOS SSR")
app.geometry('400x300')
#------------------------------------------------------

#Переменные путей
user_save_path= StringVar(value='No directory')

#------------------------------------------------------
#функции
def select_user_save_files():
    folder = filedialog.askdirectory(title="Select your save files")
    print(folder)

#------------------------------------------------------


#------------------------------------------------------

#BUTTONS
btn = ctk.CTkButton(app,text="Select folfer",width=140, command=select_user_save_files)
btn.grid(row=0, column=0, padx=(12,12), pady=12, sticky="w")
#------------------------------------------------------
#Labels

#------------------------------------------------------



app.mainloop()

# user_path = r'F:\Ai\Dasha'
#
# def list_files(path):
#     print(os.listdir(path))
#
#
# list_files(user_path)

