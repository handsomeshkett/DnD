
import sys
import os
import tkinter as tk
from entities import rarities, rarity_weights, rarity_names, rarity_price_ranges
from core import randomize_items

class DnDApp:
    def __init__(self, root):
        self.root = root
        self.main_frame = tk.Frame(root, bg="#fff")
        self.main_frame.pack(fill='both', expand=True)
        self.show_welcome()

    def show_welcome(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text="Добро пожаловать в мастер-меню DnD!", font=("Arial", 18))
        label.pack(pady=40)

    def clear_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.bottom_menu()

    def bottom_menu(self):
        menu_bar = tk.Frame(self.main_frame, bg="#f3f4f6")
        menu_bar.pack(side='bottom', fill='x')
        btn_item = tk.Button(menu_bar, text="🧰", font=("Arial", 18), command=self.show_item_checkbox, bd=0, bg="#f3f4f6", activebackground="#e0e7ff")
        btn_item.pack(side='left', expand=True, fill='x', padx=10, pady=8)
        btn_quest = tk.Button(menu_bar, text="🏷️", font=("Arial", 18), command=self.generate_price, bd=0, bg="#f3f4f6", activebackground="#e0e7ff")
        btn_quest.pack(side='left', expand=True, fill='x', padx=10, pady=8)
        btn_msg = tk.Button(menu_bar, text="💬", font=("Arial", 18), command=self.send_message, bd=0, bg="#f3f4f6", activebackground="#e0e7ff")
        btn_msg.pack(side='left', expand=True, fill='x', padx=10, pady=8)
        btn_history = tk.Button(menu_bar, text="📜", font=("Arial", 18), command=self.show_history, bd=0, bg="#f3f4f6", activebackground="#e0e7ff")
        btn_history.pack(side='left', expand=True, fill='x', padx=10, pady=8)

        # TODO: Создать правильный bottom_menu для всех страниц
        #       Добавить обработку событий для кнопок

    def show_item_checkbox(self):
        self.clear_frame()
        self.rarity_vars = {}
        
        label = tk.Label(self.main_frame, text="Выберите редкости:", font=("Arial", 16))
        label.pack(pady=20)

        for rarity in rarity_names.values():
            var = tk.BooleanVar(value=True)
            chk = tk.Checkbutton(self.main_frame,
                         text=rarity,
                         variable=var,
                         font=("Arial", 11),
                         anchor='center')
            chk.pack(anchor='center', pady=5)
            self.rarity_vars[rarity] = var
        
        run_button = tk.Button(self.main_frame, text="Далее", command=self.show_item_count, bg="lightgreen",  font=("Arial", 14))
        run_button.pack(anchor= 'center', pady=15) 

        # TODO: Обработка нулевых значений
        #       Сохранение последних выбранных редкостей в настройках

    def show_item_count(self):
        self.clear_frame()
        
        label = tk.Label(self.main_frame, text="Выберите количество предметов для рандомизации:", font=("Arial", 16))
        label.pack(pady=20)
        self.item_count_var = tk.IntVar(value=1)
        count_entry = tk.Entry(self.main_frame, textvariable=self.item_count_var, font=("Arial", 11), width=5)
        count_entry.pack(pady=10)
        
        run_button = tk.Button(self.main_frame, text="Запустить", command=self.show_randomizer_result, bg="lightgreen", font=("Arial", 14))
        run_button.pack(anchor='center', pady=15)

         # TODO: Обработка неправильных значений
         #       Проверка на ноль или отрицательные числа
        
    def show_randomizer_result(self):
        self.clear_frame()

        selected_rarities = []
        for rarity, vars in self.rarity_vars.items():
            if vars.get():           
                selected_rarities.append(rarity)
        count = self.item_count_var.get()
        
        items = randomize_items(selected_rarities, count)

        

    def generate_price(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text="Генерация цены пока не реализована.", font=("Arial", 15))
        label.pack(pady=40)

    def send_message(self):
        self.clear_frame()
        label = tk.Label(self.main_frame, text="Функция отправки сообщения пока не реализована.", font=("Arial", 15))
        label.pack(pady=40)


    def show_history(self):
        self.clear_frame()

        label = tk.Label(self.main_frame, text="История игровых событий:", font=("Arial", 16))
        label.pack(pady=20)

        logs_path = os.path.join(os.path.dirname(__file__), "logs.txt")
        try:
            with open(logs_path, "r", encoding="utf-8") as f:
                logs = f.read()
        except FileNotFoundError:
            logs = "Файл истории (logs.txt) не найден."

        text_box = tk.Text(self.main_frame, wrap="word", font=("Arial", 11), height=20, width=70)
        text_box.insert("1.0", logs)
        text_box.config(state="disabled")
        text_box.pack(padx=10, pady=10)


def run_app():
    root = tk.Tk()
    root.title("DnD Master Menu")
    root.geometry("700x500")
    app = DnDApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()

