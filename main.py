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

LOG_TEXT_COLOR = "#42855B"
# ------------------------

# --- Шрифты кнопок ---
BUTTON_FONT = ctk.CTkFont(size=16, weight="bold")
# ----------------------

# ------- Загрузка путей -------------------------------
config_data = helpers.check_config()

saved_path = config_data["user_saves_folder"]
display_path = saved_path if saved_path else 'No directory selected'
user_save_path = StringVar(value=display_path)

#2 . Extension variable
saved_extension = config_data["user_extension"]
user_extension = StringVar(value=saved_extension)

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
    extension = user_extension.get()
    helpers.zip_user_saves(folder_str,extension, log_message)


def unzip_save_command():
    folder_str = user_save_path.get()
    helpers.unzip_user_saves(folder_str, log_message)


def select_user_save_files():
    folder = filedialog.askdirectory(title="Select your save files")
    if not folder:
        return
    user_save_path.set(folder)
    extension = user_extension.get()
    helpers.save_config(folder, extension, log_message)

def open_folder_command():
    app_dir = os.getcwd()
    helpers.open_user_saves(app_dir, log_message)
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

btn_open = ctk.CTkButton(sidebar_frame, text="Zip Folder", width=140, height=40,
                           command=open_folder_command, fg_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR,
                           font=BUTTON_FONT)
btn_open.grid(row=2, column=0, padx=20, pady=10, sticky="w")


btn_zip = ctk.CTkButton(sidebar_frame, text="Saves To Zip", width=140, height=40, command=zip_save_command,
                        fg_color=BUTTON_COLOR,
                        hover_color=BUTTON_HOVER_COLOR,
                        font=BUTTON_FONT)
btn_zip.grid(row=3, column=0, padx=20, pady=10, sticky="w")

btn_unzip = ctk.CTkButton(sidebar_frame, text="Unzip To Saves", width=140, height=40, command=unzip_save_command,
                          fg_color=BUTTON_COLOR,
                          hover_color=BUTTON_HOVER_COLOR,
                          font=BUTTON_FONT)
btn_unzip.grid(row=4, column=0, padx=20, pady=10, sticky="w")




# ======================================================
# 1.1. ВЛОЖЕННЫЙ ФРЕЙМ ДЛЯ РАСШИРЕНИЯ (внизу Sidebar)
# ======================================================
extension_frame = ctk.CTkFrame(sidebar_frame, fg_color="transparent") # 'transparent' чтобы не было лишних рамок
extension_frame.grid(row=5, column=0, padx=20, pady=(40,10), sticky="s") # Размещаем внизу (sticky="s")
extension_frame.columnconfigure(0, weight=1) # Чтобы элементы внутри расширялись

# 1. Заголовок
extension_label = ctk.CTkLabel(extension_frame, text="Extension (start with '.' )", font=ctk.CTkFont(size=12, weight="normal"))
extension_label.grid(row=0, column=0, padx=(0, 5), pady=(0, 2), sticky="w")

# 2. Поле ввода
user_input = ctk.CTkEntry(extension_frame, placeholder_text=".sav, .txt...", textvariable=user_extension, width=140)
user_input.grid(row=1, column=0, padx=0, pady=(0, 5), sticky="ew") # sticky="ew" - растягиваем

# 3. Кнопка "Сохранить" рядом с инпутом?
# Если кнопка должна быть под инпутом, как "Select Folder"
btn_save_ext = ctk.CTkButton(extension_frame, text="Save Ext", width=140, height=30,
                             command=lambda: helpers.save_config(user_save_path.get(), user_extension.get(), log_message),
                             fg_color=BUTTON_COLOR,
                             hover_color=BUTTON_HOVER_COLOR,
                             font=ctk.CTkFont(size=12, weight="bold"))

# Размещение кнопки под полем ввода (самый простой вариант)
btn_save_ext.grid(row=2, column=0, padx=0, pady=(5, 0), sticky="ew")

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

if saved_extension:
    log_textbox.insert("end", f"\nТекущие расшерение: {saved_extension}\n", "matrix_green")
else:
    log_textbox.insert("end", "\nНадо таки расширение файла.\n", "matrix_green")
log_textbox.configure(state="disabled")  # Запрещаем ручное редактирование

# настройка цвета для логов
log_textbox.tag_config("matrix_green", foreground="#ffffff")
log_textbox.tag_config("error_red", foreground="#FF6363")

# -------------------------------------------------------------------------------------------------------



app.mainloop()
