from src.product import Product


class Smartphone(Product):
    """Класс категории товара - Смартфон"""
    product_class_list = []

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color=None):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        Smartphone.product_class_list.append(
            {'name': self.name,
             'description': self.description,
             'price': self.price,
             'quantity': self.quantity,
             'color': self.color,
             'efficiency': self.efficiency,
             'model': self.model,
             'memory': self.memory}
        )

    def __add__(self, other):
        if type(other) is Smartphone:
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError
