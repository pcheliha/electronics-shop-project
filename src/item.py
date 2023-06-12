import csv
import pathlib
import os
from src.error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:

        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, x):
        if len(x) > 10:
            raise Exception("Длина наименования товара больше 10 символов")
        self.__name = x

    @staticmethod
    def string_to_number(x):
        x = float(x)
        x = round(x, 1)
        return int(x)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total = self.price * self.quantity
        return total

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        try:
            file = open("../src/items.csv", encoding="1251")
        except Exception as ex:
            print(ex)
        else:
            with file:
                data = csv.DictReader(file)
                try:
                    for i in data:
                        if None in i.values():
                            raise InstantiateCSVError
                        else:
                            name, price, quantity = i['name'], int(i['price']), int(i['quantity'])
                            cls(name, price, quantity)
                except InstantiateCSVError as ex:
                    print(ex.message)
                except ValueError as ex:
                    print(ex)

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError("Складывать можно только объекты Item и дочерние от них")
        return self.quantity + other.quantity


class KeyboardMixin:
    def __init__(self, language='EN'):
        self.__language = language

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, lang):
        if lang != 'EN' or 'RU':
            raise AttributeError("AttributeError: property 'language' of 'KeyBoard' object has no setter")
        self.__language = lang

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self
