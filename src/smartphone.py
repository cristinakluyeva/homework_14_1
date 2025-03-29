from src.product import Product


class Smartphone(Product):
    """Класс категории товара - Смартфон"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color=None):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory


if __name__ == '__main__':
    smart_phone = Smartphone ('Sony Xperia', 'The device include: Music Pro, Video Pro, Cinema Pro and PlayStationApp...', 50000, 5, 'Qualcomm Snapgragon 8 Gen in 1, 8', 'Sony', '256Gb')
    print(smart_phone.name)
    print(smart_phone.description)
    print(smart_phone.price)
    print(smart_phone.quantity)
    print(smart_phone.efficiency)
    print(smart_phone.model)
    print(smart_phone.memory)