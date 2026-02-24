import customtkinter as ctk

class SettingsPanel:
    def __init__(self, parent):
        self.parent = parent
        self.opened = False

        # Overlay для затемнения
        self.overlay = ctk.CTkFrame(parent, fg_color="#000000")
        self.overlay.place_forget()  # скрыт изначально
        self.overlay.bind("<Button-1>", self.close)

        # Панель настроек
        self.panel = ctk.CTkFrame(parent, width=400, corner_radius=10)
        self.panel.place_forget()  # скрыта по умолчанию

        # Пример кнопки на панели
        self.example_button = ctk.CTkButton(self.panel, text="Пример кнопки")
        self.example_button.pack(padx=20, pady=20)

    # Открытие панели — справа
    def open(self):
        if self.opened:
            return
        # Показываем overlay
        self.overlay.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.overlay.lift()
        # Показываем панель справа
        self.panel.place(relx=1.0, rely=0, relheight=1.0, anchor='ne')  # строго справа
        self.panel.lift()
        self.opened = True

    # Закрытие панели
    def close(self, event=None):
        if not self.opened:
            return
        self.panel.place_forget()
        self.overlay.place_forget()
        self.opened = False

    # Переключение
    def toggle(self):
        if self.opened:
            self.close()
        else:
            self.open()