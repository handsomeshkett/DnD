import os
import random
import tkinter as tk
from tkinter import simpledialog

# Категории и вероятности выпадения
RARITY_WEIGHTS = {
    "Кустарное": 30,
    "Заурядное": 35,
    "Солидное": 13,
    "Экспериментальное": 12,
    "Немыслимое": 8,
    "Каноническое": 1,
    "Прорывное": 1,
}
RARITY_CATEGORIES = list(RARITY_WEIGHTS.keys())

# Путь к директории (текущая директория, где лежит скрипт)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def scan_files(directory):
    matched_files = {rarity: [] for rarity in RARITY_CATEGORIES}

    for root, _, files in os.walk(directory):
        for fname in files:
            if not fname.lower().endswith('.txt'):
                continue  # пропускаем все файлы, кроме .txt

            path = os.path.join(root, fname)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read().lower()
                    found = False
                    for rarity in RARITY_CATEGORIES:
                        if rarity.lower() in content or rarity.lower() in fname.lower():
                            matched_files[rarity].append(path)
                            found = True
                            break
            except Exception as e:
                print(f"Ошибка при чтении файла {path}: {e}")

    return matched_files


def select_random_items(matched_files, total_count):
    flat_pool = []
    for rarity, weight in RARITY_WEIGHTS.items():
        flat_pool.extend([rarity] * weight)

    selected = []

    while len(selected) < total_count:
        if not flat_pool:
            break

        rarity = random.choice(flat_pool)
        if matched_files[rarity]:
            file_path = random.choice(matched_files[rarity])
            matched_files[rarity].remove(file_path)
            selected.append((rarity, file_path))

        flat_pool = [r for r in flat_pool if matched_files[r]]

    return selected

def copy_and_show_file(path):
    # Копируем путь в буфер обмена
    root.clipboard_clear()
    root.clipboard_append(path)

    # Создаем новое окно для просмотра содержимого
    viewer = tk.Toplevel()
    viewer.title(os.path.basename(path))

    text_widget = tk.Text(viewer, wrap='word', width=80, height=25)
    text_widget.pack(expand=False, fill='both')

    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        content = f"Не удалось прочитать файл:\n{e}"

    text_widget.insert('1.0', content)
    text_widget.config(state='disabled')  # Запретить редактирование

def run_randomizer():
    total_count = simpledialog.askinteger("Сколько предметов?", "Введите количество предметов:", minvalue=1)
    if not total_count:
        return

    matched_files = scan_files(BASE_DIR)
    selected_items = select_random_items(matched_files, total_count)

    result_window = tk.Toplevel()
    result_window.title("Результаты рандомайзера")

    for rarity, path in selected_items:
        frame = tk.Frame(result_window)
        frame.pack(fill='x', pady=2, padx=5)

        tk.Label(frame, text=f"{rarity} → {os.path.basename(path)}").pack(side='left', anchor='w')
        tk.Button(frame, text="📋", command=lambda p=path: copy_and_show_file(p)).pack(side='right')

# GUI
root = tk.Tk()
root.title("Рандомизатор предметов для D&D")
root.geometry("500x300")

tk.Label(root, text="🎲 Рандомизатор Инвентаря").pack(pady=10)
tk.Button(root, text="Запустить", command=run_randomizer, bg="lightgreen").pack(pady=10)

root.mainloop()
