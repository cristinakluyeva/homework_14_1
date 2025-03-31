from src.product import Product
from src.smartphone import Smartphone


class LawnGrass(Product):
    """Класс категории товара: Трава газонная."""
    product_class_list=[]
    def __init__(self, name, description, price, quantity, country, germination_period, color=None):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period
        LawnGrass.product_class_list.append({'name': self.name,
                                           'description': self.description,
                                           'price': self.price,
                                           'quantity': self.quantity,
                                           'color': self.color,
                                           'country': self.country,
                                           'germination_period': self.germination_period})

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError



if __name__ == '__main__':
    lawn_grass = LawnGrass('Green field', 'Short and soft cover', 1200, 10, 'Russia', '30 days', 'green')
    print(lawn_grass.name)
    print(lawn_grass.description)
    print(lawn_grass.price)
    print(lawn_grass.quantity)
    print(lawn_grass.country)
    print(lawn_grass.germination_period)
    print(lawn_grass.color)

    lawn_grass2 = LawnGrass('Football grass', 'Ideal for sport area', 3500, 100, 'USA', '40 days', 'light green')
    print(lawn_grass + lawn_grass2)
    smart_phone = Smartphone('Sony Xperia',
                             'The device include: Music Pro, Video Pro, Cinema Pro and PlayStationApp...', 50000, 5,
                             'Qualcomm Snapgragon 8 Gen in 1, 8', 'Sony', '256Gb')