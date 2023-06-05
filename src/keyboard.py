from src.item import Item, KeyboardMixin


class KeyBoard(Item, KeyboardMixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)


