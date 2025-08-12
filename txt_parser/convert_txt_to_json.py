#Данный файл переводит все текстовые файлы с описанием оружия к одному JSON файлу

import os
import json
from rarity_map import rarities
from utils import process_weapon_file, process_consumable_file


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
CONSUMABLE_FOLDER = os.path.join(BASE_DIR, "Расходники")
WEAPON_FOLDER = os.path.join(BASE_DIR, "Оружие")

items = []

#Добавляем оружие в словарь
for root, dirs, files in os.walk(WEAPON_FOLDER):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)  # Creating correct file path

            items.append(process_weapon_file(file_path))

#Добавляем расходники в словарь
for root, dirs, files in os.walk(CONSUMABLE_FOLDER):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)  # Creating correct file path

            items.append(process_consumable_file(file_path))
            



output_path = os.path.join(os.path.dirname(__file__), "items.json")
with open(output_path, "w", encoding="utf-8") as json_file:
    json.dump(items, json_file, indent=2, ensure_ascii=False)
print(f"Successfully saved {len(items)} items in {output_path}")


