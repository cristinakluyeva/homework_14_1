from src.product import Product


class LawnGrass(Product):
    """Класс категории товара: Трава газонная."""
    def __init__(self, name, description, price, quantity, country, germination_period, color=None):
        super().__init__(name, description, price, quantity, color)
        self.country = country
        self.germination_period = germination_period



if __name__ == '__main__':
    lawn_grass = LawnGrass('Green field', 'Short and soft cover', 1200, 10, 'Russia', '30 days', 'green')
    print(lawn_grass.name)
    print(lawn_grass.description)
    print(lawn_grass.price)
    print(lawn_grass.quantity)
    print(lawn_grass.country)
    print(lawn_grass.germination_period)
    print(lawn_grass.color)