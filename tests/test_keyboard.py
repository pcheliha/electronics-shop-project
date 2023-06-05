from src.keyboard import KeyBoard
from src.item import Item

kb = KeyBoard('Dark Project KD87A', 9600, 5)


def test_keyboard():
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"
    assert str(kb.language) == "RU"

