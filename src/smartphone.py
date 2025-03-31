from src.product import Product


class Smartphone(Product):
    """Класс категории товара - Смартфон"""
    product_class_list=[]
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color=None):
        super().__init__(name, description, price, quantity, color)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        Smartphone.product_class_list.append({'name': self.name,
                                           'description': self.description,
                                           'price': self.price,
                                           'quantity': self.quantity,
                                           'color': self.color,
                                           'efficiency': self.efficiency,
                                           'model': self.model,
                                           'memory': self.memory})


    def __add__(self, other):
        if isinstance(other, Smartphone):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise TypeError


if __name__ == '__main__':
    smart_phone = Smartphone ('Sony Xperia', 'The device include: Music Pro, Video Pro, Cinema Pro and PlayStationApp...', 50000, 5, 'Qualcomm Snapgragon 8 Gen in 1, 8', 'Sony', '256Gb')
    print(smart_phone.name)
    print(smart_phone.description)
    print(smart_phone.price)
    print(smart_phone.quantity)
    print(smart_phone.efficiency)
    print(smart_phone.model)
    print(smart_phone.memory)

    smart_phone2 = Smartphone ('Samsung', 'The device include: good memory, strong screen...', 30000, 25, '4:2', 'Samsung', '64Gb')

    print(smart_phone + smart_phone2)