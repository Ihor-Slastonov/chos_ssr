import os
import helpers

import customtkinter as ctk
from tkinter import StringVar
from tkinter import filedialog

# Внешний вид
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

# Окно
app = ctk.CTk()
app.title("CHOS SSR")
app.geometry('800x450')
app.minsize(700, 400)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
# ------------------------------------------------------
# ------- Загрузка путей -------------------------------
saved_path = helpers.check_config()
display_path = saved_path if saved_path else 'No directory selected'
user_save_path = StringVar(value=display_path)

# ------------------------------------------------------

# ======================================================
# 1. ЛЕВАЯ ПАНЕЛЬ (SIDEBAR FRAME)
# ======================================================
sidebar_frame = ctk.CTkFrame(app, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
sidebar_frame.grid_rowconfigure(5, weight=1)

# Заголовок программы (как на дизайне)
logo_label = ctk.CTkLabel(sidebar_frame, text="CHOS SSR", font=ctk.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky='w')

# Кнопки
btn_select = ctk.CTkButton(sidebar_frame, text="Select folder", width=140,
                           command=lambda: select_user_save_files)
btn_select.grid(row=1, column=0, padx=20, pady=(10, 5), sticky="w")

btn_zip = ctk.CTkButton(sidebar_frame, text="saves to zip", width=140, command=lambda: zip_save_command)
btn_zip.grid(row=2, column=0, padx=20, pady=5, sticky="w")

btn_unzip = ctk.CTkButton(sidebar_frame, text="unzip to save", width=140, command=lambda: unzip_save_command)
btn_unzip.grid(row=3, column=0, padx=20, pady=5, sticky="w")

# ------------------------------------------------------


# --------------------------------------------------------------------------------------------------------

# ======================================================
# 2. ПРАВАЯ ПАНЕЛЬ (MAIN CONTENT FRAME)
# ======================================================
main_frame = ctk.CTkFrame(app, corner_radius=0)
main_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
main_frame.grid_columnconfigure(0, weight=1)
main_frame.grid_rowconfigure(1, weight=1)

log_title = ctk.CTkLabel(main_frame, text="Системный лог", font=ctk.CTkFont(size=14, weight="bold"))
log_title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

# WIDGETS
log_textbox = ctk.CTkTextbox(main_frame, width=500, height=300)
log_textbox.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="nsew")
log_textbox.insert("end", "Добро пожаловать CHOS_овцы\n", "matrix_green")
if display_path != 'No directory selected':
    log_textbox.insert("end", f"\nТекущая папка сохранений: {display_path}", "matrix_green")
else:
    log_textbox.insert("end", "\nНу выбери папку а.", "matrix_green")
log_textbox.configure(state="disabled")  # Запрещаем ручное редактирование

# настройка цвета для логов
log_textbox.tag_config("matrix_green", foreground="#00FF41")

# -------------------------------------------------------------------------------------------------------
# FUNCTIONS & COMMANDS
folder_str = user_save_path.get()


def log_message(message):
    log_textbox.configure(state='normal')
    log_textbox.insert("end", f"\n{message}", "matrix_green")
    log_textbox.see("end")  # Прокрутка к последней строке
    log_textbox.configure(state="disabled")


def zip_save_command():
    helpers.zip_user_saves(folder_str)


def unzip_save_command():
    helpers.unzip_user_saves(folder_str)


def select_user_save_files():
    folder = filedialog.askdirectory(title="Select your save files")
    user_save_path.set(folder)
    print(folder)
    helpers.save_config(folder)


# ----------------------------------------------------------

app.mainloop()
