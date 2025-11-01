import os
import helpers

import customtkinter as ctk
from tkinter import StringVar
from tkinter import filedialog



#Внешний вид
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

#Окно
app = ctk.CTk()
app.title("CHOS SSR")
app.geometry('540x300')
#------------------------------------------------------

#Переменные путей
user_save_path= StringVar(value='No directory')

#------------------------------------------------------
#FUNCTIONS & COMMANDS
def zip_save_command():
    folder_str = user_save_path.get()
    helpers.zip_user_saves(folder_str)

def select_user_save_files():
    folder = filedialog.askdirectory(title="Select your save files")
    user_save_path.set(folder)
    print(folder)

#------------------------------------------------------
#Labels
label = ctk.CTkLabel(app,textvariable=user_save_path, anchor="w")
label.grid(row=0, column=0, padx=(12,12), sticky="w")

#------------------------------------------------------

#BUTTONS
btn = ctk.CTkButton(app,text="Select folder",width=140, command=select_user_save_files)
btn.grid(row=1, column=0, padx=(12,12), pady=6, sticky="w")

btn = ctk.CTkButton(app,text="saves to zip",width=140, command=zip_save_command)
btn.grid(row=2, column=0, padx=(12,12), pady=6, sticky="w")

#------------------------------------------------------


#------------------------------------------------------



app.mainloop()

# user_path = r'F:\Ai\Dasha'
#
# def list_files(path):
#     print(os.listdir(path))
#
#
# list_files(user_path)

