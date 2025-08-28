from dataclasses import dataclass
import os

#Значения которые хранит каждая редкость
@dataclass
class Rarity:
    key: str
    name: str
    weight: int
    min_price: int
    max_price: int

#Словарь редкостей
rarities = {
    "custom": Rarity(
        key="custom",
        name="Кустарное",
        weight=5,
        min_price=10,
        max_price=50
    ),
    "common": Rarity(
        key="common",
        name="Заурядное",
        weight=15,
        min_price=50,
        max_price=150
    ),
    "solid": Rarity(
        key="solid",
        name="Солидное",
        weight=25,
        min_price=150,
        max_price=300
    ),
    "experimental": Rarity(
        key="experimental",
        name="Экспериментальное",
        weight=15,
        min_price=100,
        max_price=500
    ),
    "unthinkable": Rarity(
        key="unthinkable",
        name="Немыслимое",
        weight=5,
        min_price=500,
        max_price=1000
    ),
    "canonical": Rarity(
        key="canonical",
        name="Каноническое",
        weight=10,
        min_price=700,
        max_price=1500
    ),
    "breakthrough": Rarity(
        key="breakthrough",
        name="Прорывное",
        weight=3,
        min_price=1000,
        max_price=2500
    ),
}

## Блок с определением словарей
rarity_weights = {key: value.weight for key, value in rarities.items()}
rarity_names = {key: value.name for key, value in rarities.items()}
rarity_price_ranges = {key: (value.min_price, value.max_price) for key, value in rarities.items()}

json_filepath = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', 'txt_parser', 'items.json'))

