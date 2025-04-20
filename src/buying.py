from abc import ABC, abstractmethod


class Buying(ABC):
    """Класс покупки: класс заготовка(клише) для классов: Order, Category"""
    @abstractmethod
    def add_product(self):
        pass

    @abstractmethod
    def products_in_list(self):
        pass
