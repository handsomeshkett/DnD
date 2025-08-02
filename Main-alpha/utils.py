from rarity_map import rarities, Weapon, Consumable


def process_weapon_file(file_path):
    
    rarity_name_map = {v.name.lower(): key for key, v in rarities.items()} 
    current_weapon = Weapon()

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            
            lines = [line.strip() for line in f if line.strip()]

            #обработка пустых файлов
            if not lines:
                print(f"Empty file: {file_path}")
                return 0

            #обработка первой строки отдельно, потому что не всегда одинаковый формат
            first_line = lines[0]
            if ":" in first_line:
                name = first_line.split(":", 1)[1].strip()
            else:
                name = first_line.strip()
            name = name.split("(", 1)[0].strip()
            current_weapon.name = name

            #обработка остальных строк
            for line in lines[1:]:
                formated_line = line.strip().lower()
                if formated_line.startswith("тип"):
                    current_weapon.type = formated_line.split(":", 1)[1].strip()
                elif formated_line.startswith("дальность"):
                    current_weapon.range = formated_line.split(":", 1)[1].strip()
                elif formated_line.startswith("урон"):
                    current_weapon.damage = formated_line.split(":", 1)[1].strip()
                elif formated_line.startswith("прим"):
                    current_weapon.description = formated_line.split(":", 1)[1].strip()
                elif formated_line.startswith("патроны"):
                    current_weapon.ammo = formated_line.split(":", 1)[1].strip()

                #обработка редкости используя обьект из rarity_map
                for rarity_name, key in rarity_name_map.items():
                    if rarity_name in formated_line:

                        current_weapon.rarity = rarities[key].name
                        rarity_obj = rarities[key]
                        current_weapon.price = formated_line.split(":", 1)[1].strip()
                        break

        return current_weapon.to_dict()
    except Exception as e:
        print(f"Error while reading file {file_path}: {e}")

def  process_consumable_file(file_path):
    current_consumable = Consumable()  # Using Consumable class for consistency

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

            #обработка пустых файлов
            if not lines:
                print(f"Empty file: {file_path}")
                return 0

            #обработка первой строки отдельно, потому что не всегда одинаковый формат
            first_line = lines[0]
            name = first_line.strip()
            current_consumable.name = name

            #обработка остальных строк
            for line in lines[1:]:
                formated_line = line.strip()
                current_consumable.description = formated_line

        return current_consumable.to_dict()
    except Exception as e:
        print(f"Error while reading file {file_path}: {e}")