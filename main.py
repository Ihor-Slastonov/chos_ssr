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
# --- КОНСТАНТЫ ЦВЕТА ---
BUTTON_COLOR = "#1F7D53"
BUTTON_HOVER_COLOR = "#1A6C49"
# ------------------------

# --- Шрифты кнопок ---
BUTTON_FONT = ctk.CTkFont(size=16, weight="bold")
# ----------------------

# ------- Загрузка путей -------------------------------
saved_path = helpers.check_config()
display_path = saved_path if saved_path else 'No directory selected'
user_save_path = StringVar(value=display_path)


# ------------------------------------------------------

# FUNCTIONS & COMMANDS

def log_message(message, is_error=False):
    tag = "error_red" if is_error else "matrix_green"

    log_textbox.configure(state='normal')
    log_textbox.insert("end", f"\n{message}\n", tag)
    log_textbox.see("end")  # Прокрутка к последней строке
    log_textbox.configure(state="disabled")


def zip_save_command():
    folder_str = user_save_path.get()
    helpers.zip_user_saves(folder_str, log_message)


def unzip_save_command():
    folder_str = user_save_path.get()
    helpers.unzip_user_saves(folder_str, log_message)


def select_user_save_files():
    folder = filedialog.askdirectory(title="Select your save files")
    user_save_path.set(folder)
    helpers.save_config(folder, log_message)


# ----------------------------------------------------------

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
btn_select = ctk.CTkButton(sidebar_frame, text="Select Folder", width=140, height=40,
                           command=select_user_save_files, fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR,
                           font=BUTTON_FONT)
btn_select.grid(row=1, column=0, padx=20, pady=(10, 10), sticky="w")

btn_zip = ctk.CTkButton(sidebar_frame, text="Saves To Zip", width=140, height=40, command=zip_save_command,
                        fg_color=BUTTON_COLOR,
                        hover_color=BUTTON_HOVER_COLOR,
                        font=BUTTON_FONT)
btn_zip.grid(row=2, column=0, padx=20, pady=10, sticky="w")

btn_unzip = ctk.CTkButton(sidebar_frame, text="Unzip To Saves", width=140, height=40, command=unzip_save_command,
                          fg_color=BUTTON_COLOR,
                          hover_color=BUTTON_HOVER_COLOR,
                          font=BUTTON_FONT)
btn_unzip.grid(row=3, column=0, padx=20, pady=10, sticky="w")

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
    log_textbox.insert("end", f"\nТекущая папка сохранений: {display_path}\n", "matrix_green")
else:
    log_textbox.insert("end", "\nНу выбери папку а.\n", "matrix_green")
log_textbox.configure(state="disabled")  # Запрещаем ручное редактирование

# настройка цвета для логов
log_textbox.tag_config("matrix_green", foreground="#00FF41")
log_textbox.tag_config("error_red", foreground="#FF6363")

# -------------------------------------------------------------------------------------------------------


app.mainloop()
