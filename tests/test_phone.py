from src.item import Item
from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
item1 = Item("Смартфон", 10000, 20)


def test_Phone():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
