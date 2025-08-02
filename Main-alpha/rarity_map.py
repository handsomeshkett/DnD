from dataclasses import dataclass

@dataclass
#Значения которые хранит каждая редкость
class Rarity:
    key: str
    name: str
    weight: int
    min_price: int
    max_price: int

#Словарь редкостей
rarities = {
    "custom": Rarity("custom", "кустарное", 5, 10, 50),
    "common": Rarity("common", "заурядное", 15, 50, 150),
    "solid": Rarity("solid", "солидное", 25, 150, 300),
    "experimental": Rarity("experimental", "экспериментальное", 15, 100, 500),
    "unthinkable": Rarity("unthinkable", "немыслимое", 5, 500, 1000),
    "canonical": Rarity("canonical", "каноническое", 10, 700, 1500),
    "breakthrough": Rarity("breakthrough", "прорывное", 3, 1000, 2500),
}

class Weapon:
    def __init__(self):
        self.name = ""
        self.rarity = ""
        self.price = ""
        self.description = ""
        self.type = ""
        self.range = ""
        self.damage = ""
        self.note = ""
        self.ammo = ""
    def to_dict(self):
        return {
            "name": self.name,
            "rarity" :  self.rarity,
            "price": self.price,
            "description" : self.description,
            "type": self.type,
            "range": self.range,
            "damage": self.damage,
            "note": self.note,
            "ammo": self.ammo
        }
    
class Consumable:
    def __init__(self):
        self.name = ""
        self.description = ""

    def to_dict(self):
        return {
            "name": self.name,
            "description" : self.description,
        }