"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest

from src.item import Item


smartphone = Item('Смартфон', 15, 5)
smartphone.pay_rate = 1.0
smartphone1 = Item('Ноутбук', 10, 3

def test_calculate_total_price():
    assert smartphone.calculate_total_price() == 75


def test_apply_discount():
    assert smartphone.apply_discount() == 15.0


def test_item_name():
    assert smartphone.name == 'Смартфон'
    assert smartphone1.string_to_number(1) == 1
    assert smartphone1.string_to_number("5") == 5
    with pytest.raises(Exception):
        smartphone1.set_name