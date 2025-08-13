def log_message(*args, **kwargs):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        print(*args, **kwargs, file=f)
import os
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
import json
#Импортируем новый словарь редкостей
from rarity_map import rarities

RARITY_WEIGHTS = {
    "Кустарное": 30,
    "Заурядное": 35,
    "Солидное": 13,
    "Экспериментальное": 12,
    "Немыслимое": 8,
    "Каноническое": 1,
    "Прорывное": 1,
}

RARITY_CATEGORIES = [rarity.name for rarity in rarities.values()]
RARITY_CATEGORIES_GUI = RARITY_CATEGORIES + ['Расходник']
log_message(f"Доступные редкости: {RARITY_CATEGORIES_GUI}")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Ищем подходящие предметы
def scan_files(json_filename, selected_rarities):
    matched_items = {}
    log_message(f"Инициализация словаря предметов: {matched_items}")

    items_json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(items_json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

        for item in items:
            item_name = item.get('name', None)
            item_rarity = item.get('rarity', '').lower() if 'rarity' in item else None
            if item_rarity:
                for rarity in RARITY_CATEGORIES:
                    if item_rarity == rarity.lower() and rarity in selected_rarities:
                        matched_items[item_name] = rarity
                        break
            else:
                # Если предмет без редкости, считаем его расходником
                if 'Расходник' in selected_rarities:
                    matched_items[item_name] = 'Расходник'

    log_message(f"Найденные предметы: {matched_items}")
    return matched_items

def select_random_items(matched_files, total_count):
    items = list(matched_files.items())  # [(name, rarity), ...]
    if not items:
        return []

    # Создаём взвешенный пул предметов
    weighted_pool = []
    for name, rarity in items:
        weight = RARITY_WEIGHTS.get(rarity, 1)
        weighted_pool.extend([(name, rarity)] * weight)

    if not weighted_pool:
        return []

    selected = []
    used = set()
    while len(selected) < min(total_count, len(items)) and weighted_pool:
        choice = random.choice(weighted_pool)
        if choice not in used:
            selected.append(choice)
            used.add(choice)
        # Удаляем все вхождения выбранного предмета, чтобы не выбрать его снова
        weighted_pool = [item for item in weighted_pool if item != choice]

    return selected


def show_info(path):
    # Новый функционал: показываем всю информацию о предмете из items.json
    root.clipboard_clear()
    root.clipboard_append(path)

    # path теперь имя предмета
    item_name = path
    # Загружаем все предметы
    items_json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    with open(items_json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    # Ищем предмет по имени
    item = next((i for i in items if i.get('name') == item_name), None)

    viewer = tk.Toplevel()
    viewer.title(item_name)

    text_widget = tk.Text(viewer, wrap='word', width=80, height=25)
    text_widget.pack(expand=False, fill='both')

    if item:
        # Определяем, оружие это или расходник
        if 'rarity' in item:
            # Оружие
            info = f"Имя: {item.get('name', '')}\n"
            info += f"Редкость: {item.get('rarity', '')}\n"
            info += f"Цена: {item.get('price', '')}\n"
            info += f"Описание: {item.get('description', '')}\n"
            info += f"Тип: {item.get('type', '')}\n"
            info += f"Дистанция: {item.get('range', '')}\n"
            info += f"Урон: {item.get('damage', '')}\n"
            info += f"Заметка: {item.get('note', '')}\n"
            info += f"Боеприпасы: {item.get('ammo', '')}\n"
        else:
            # Расходник
            info = f"Имя: {item.get('name', '')}\n"
            info += f"Описание: {item.get('description', '')}\n"
        text_widget.insert('1.0', info)
    else:
        text_widget.insert('1.0', f"Информация о предмете '{item_name}' не найдена.")
    text_widget.config(state='disabled')


def run_randomizer():
    total_count = simpledialog.askinteger("Сколько предметов?", "Введите количество предметов:", minvalue=1)
    if not total_count:
        return

    # Получение выбранных редкостей
    selected_rarities = [rarity for rarity, var in rarity_vars.items() if var.get()]
  
    log_message(f"Выбранные редкости: {selected_rarities}")

    if not selected_rarities:
        messagebox.showwarning("Ошибка", "Выберите хотя бы одну редкость!")
        return

    #!!!!! Получаем словарь файлов с учетом выбранных редкостей
    matched_files = scan_files("items.json", selected_rarities)
    # Оставить только выбранные редкости
    #filtered_files = {rarity: matched_files[rarity] for rarity in selected_rarities}

    selected_items = select_random_items(matched_files, total_count)
    log_message(f"Выбранные предметы: {selected_items}")

    if not selected_items:
        messagebox.showinfo("Нет результатов", "Не найдено подходящих файлов для выбранных редкостей.")
        return

    result_window = tk.Toplevel()
    result_window.title("Результаты рандомайзера")

    for name, rarity in selected_items:
        frame = tk.Frame(result_window)
        frame.pack(fill='x', pady=2, padx=5)

        tk.Label(frame, text=f"{rarity} → {name}").pack(side='left', anchor='w')
        tk.Button(frame, text="📋", command=lambda n=name: show_info(n)).pack(side='right')

##
### GUI
##root = tk.Tk()
##root.title("Рандомизатор предметов для D&D")
##root.geometry("400x400")
##
##tk.Label(root, text="🎲 Рандомизатор Инвентаря").pack(pady=10)
##
### Блок выбора редкостей
##rarity_frame = tk.LabelFrame(root, text="Выберите редкости", padx=10, pady=5)
##rarity_frame.pack(pady=5, fill='both', padx=10)
##
##rarity_vars = {}
##for rarity in RARITY_CATEGORIES_GUI:
##    var = tk.BooleanVar(value=True)
##    chk = tk.Checkbutton(rarity_frame, text=rarity, variable=var)
##    chk.pack(anchor='w')
##    rarity_vars[rarity] = var
##
##tk.Button(root, text="Запустить", command=run_randomizer, bg="lightgreen").pack(pady=15)
##
##root.mainloop()
##