

def log_message(*args, **kwargs):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        print(*args, **kwargs, file=f)

##Функции для рандомизации прелметов

def randomize_items(selected_rarities, total_count):
    pass

    ## Получаем словарь предметов с учетом выбранных редкостей

    ## Создаем взвешенный пул предметов с учетом веса редкостей

    ## Выбираем случайные предметы из пула

    ## Возвращаем список выбранных предметов

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

