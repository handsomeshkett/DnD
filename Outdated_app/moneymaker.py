import os
import re
import random

price_ranges = {
    "кустарное": (100, 300),
    "заурядное": (100, 500),
    "солидное": (800, 2000),
    "экспериментальное": (1000, 3000),
    "немыслимое": (2000, 5000),
    "прорывное": (5000, 10000),
    "каноническое": (5000, 35100),
}

def choose_random_price(low, high):
    low_100 = (low + 99) // 100
    high_100 = high // 100
    choice = random.randint(low_100, high_100) * 100
    return choice

def find_category(text):
    text_lower = text.lower()
    for category in price_ranges.keys():
        if category in text_lower:
            return category
    return None

price_line_pattern = re.compile(
    rf"^\s*({'|'.join(price_ranges.keys())}):\s*\d+\$\s*$",
    re.IGNORECASE
)

def update_price_line(lines, category, price):
    new_price_line = f"{category.capitalize()}: {price}$\n"
    for i, line in enumerate(lines):
        if price_line_pattern.match(line):
            lines[i] = new_price_line
            return lines
    if not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    lines.append("\n" + new_price_line)
    return lines

def process_file(filepath):
    print(f"Обрабатываю файл: {filepath}")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except Exception as e:
        print(f"  Ошибка чтения: {e}")
        return

    text = "".join(lines)
    category = find_category(text)

    if not category:
        print("  Категория редкости не найдена, пропускаю файл.")
        return

    low, high = price_ranges[category]
    price = choose_random_price(low, high)
    lines = update_price_line(lines, category, price)

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print(f"  Добавлена/обновлена цена: {category.capitalize()}: {price}$")
    except Exception as e:
        print(f"  Ошибка записи: {e}")

def scan_directory(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith(".txt"):
                process_file(os.path.join(dirpath, filename))

if __name__ == "__main__":
    import sys
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    scan_directory(root)
