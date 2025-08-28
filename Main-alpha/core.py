import json
import random
import os
import sys
from entities import json_filepath

from rarity_map import rarities



def log_message(*args, **kwargs):
    with open('logs.txt', 'a', encoding='utf-8') as f:
        print(*args, **kwargs, file=f)
    print(*args, **kwargs)

##Функции для рандомизации прелметов

def randomize_items(selected_rarities, total_count):

    
    
    selected_rarities = [rarity.lower() for rarity in selected_rarities]

    print(selected_rarities, total_count)
    

    ## Получаем словарь предметов с учетом выбранных редкостей
    
    is_path_valid(json_filepath)

    

    list_of_items = get_items(json_filepath, selected_rarities)
    
    
    

    ## Создаем взвешенный пул предметов с учетом веса редкостей
    ## Выбираем случайные предметы из пула

    items_pool = weighted_random(list_of_items, total_count)

    log_message(f"Выбранные предметы: {items_pool}")

    ## Возвращаем список выбранных предметов

    return items_pool

def get_items(json_filepath, selected_rarities):
    matched_items = {}
    try:
        with open(json_filepath, 'r', encoding='utf-8') as file:
            items = json.load(file)
            
            for item in items:
                item_name = item.get('name', None)
                item_rarity = item.get('rarity', None)
                
                # Проверяем, есть ли у предмета имя и редкость
                if item_name and item_rarity:
                    # Проверяем, входит ли редкость предмета в выбранные редкости
                    if item_rarity in selected_rarities:
                        matched_items[item_name] = item_rarity
                        
    except FileNotFoundError:
        log_message(f"Файл {json_filepath} не найден")
    except json.JSONDecodeError:
        log_message(f"Ошибка чтения JSON файла {json_filepath}")
    except Exception as e:
        log_message(f"Ошибка при загрузке предметов: {e}")

    return matched_items

def weighted_random(items_dict, total_count):
    """
    Выбирает случайные предметы с учетом весов их редкостей
    
    Args:
        items_dict: словарь {"имя предмета": "редкость"}
        total_count: количество предметов для выбора
    
    Returns:
        список выбранных предметов в формате [(имя, редкость), ...]
    """
    if not items_dict:
        log_message("Нет предметов для выбора")
        return []
    
    # Создаем список предметов с весами
    weighted_items = []
    
    # Создаем маппинг русских названий редкостей к английским ключам
    rarity_name_to_key = {rarity.name: key for key, rarity in rarities.items()}
    
    for item_name, item_rarity in items_dict.items():
        # Находим ключ редкости по русскому названию
        rarity_key = rarity_name_to_key.get(item_rarity)
        
        if rarity_key and rarity_key in rarities:
            weight = rarities[rarity_key].weight
            # Добавляем предмет в список столько раз, сколько указано в весе
            for _ in range(weight):
                weighted_items.append((item_name, item_rarity))
        else:
            # Если редкость не найдена, добавляем с весом 1
            weighted_items.append((item_name, item_rarity))
            log_message(f"Неизвестная редкость: {item_rarity} для предмета {item_name}")
    
    # Выбираем случайные предметы
    selected_items = []
    for _ in range(min(total_count, len(weighted_items))):
        if weighted_items:
            selected_item = random.choice(weighted_items)
            selected_items.append(selected_item)
            # Можно убрать выбранный предмет, чтобы избежать дубликатов
            # weighted_items.remove(selected_item)
    
    log_message(f"Выбрано предметов: {len(selected_items)} из {total_count} запрошенных")
    return selected_items

def is_path_valid(json_filepath):
    if not os.path.exists(json_filepath):
        print(f"Файл {json_filepath} не существует")
        return 0
    elif not os.path.isfile(json_filepath):
        print(f"{json_filepath} не является файлом")
        return 0   
    else:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            try:
                items = json.load(f)
                ##print(f"Полученные предметы: {items}")
                return 1
            except json.JSONDecodeError:
                print(f"Ошибка чтения JSON файла {json_filepath}")
                return 0
    

def get_item_description(name, filepath=json_filepath):

    if is_path_valid(filepath):

        with open(filepath, 'r', encoding='utf-8') as f:
            items = json.load(f)

            ##Перенос строки
            for item in items:
                if item['name'] == name:
            ##        for i in item['description']:
            ##            if i % 40 == 0:
            ##                if i == ' ':
            ##                    item['description'] = item['description'].replace(' ', '\n')
            ##                else:

                        
                    return (f"Имя: {item['name']}\nРедкость: {item['rarity']}\nЦена: {item['price']}\nОписание: {item['description']}\nТип: {item['type']}")

if __name__ == "__main__":
    randomize_items(['Кустарное', 'Заурядное', 'Солидное', 'Экспериментальное'], 10)