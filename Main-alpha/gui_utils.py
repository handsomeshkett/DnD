

##Функции для рандомизации прелметов

def randomize_item():
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

def get_rarities():
