from src.product import Product


class LawnGrass(Product):
    """Класс категории товара: Трава газонная."""
    product_class_list = []

    def __init__(self, name, description, price, quantity, country, germination_period, color=None):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
        LawnGrass.product_class_list.append(
            {'name': self.name,
             'description': self.description,
             'price': self.price,
             'quantity': self.quantity,
             'color': self.color,
             'country': self.country,
             'germination_period': self.germination_period
             }
        )

    def __add__(self, other):
        if type(other) is LawnGrass:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
