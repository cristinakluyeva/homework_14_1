from src.product import Product
from src.buying import Buying


class Order(Product, Buying):
    """Класс представляет кол-воо заказанных товаров"""
    ordered_product_list =[] # Создаем список заказанных товаров

    def __init__(self, name, description, price, quantity, color=None):
        super().__init__(name, description, price, quantity,color)
        Order.ordered_product_list.append(self)  # При создании экземпляра класса, сразу добавляем его в список заказанных товаров

    def __str__(self):
        return f'Заказали: {self.name}. Кол-во: {self.quantity}. Сумма заказа: {self.quantity * self.price}.'

    @classmethod
    def add_product(cls, new_product: Product):
        if isinstance(new_product, Product):
            cls.ordered_product_list.append(new_product)
        else:
            raise TypeError

    @property
    def products_in_list(self):
        joined_order_names = [prod.name for prod in Order.ordered_product_list]
        quantity_order = sum(prod.quantity for prod in  Order.ordered_product_list)
        price_order = sum([(prod.quantity * prod.price) for prod in Order.ordered_product_list])
        return f'Заказали: {','.join(joined_order_names)}. Кол-во: {quantity_order}. Сумма заказа: {price_order}.'


if __name__ == '__main__':
    order = Order('Груша', 'Фрукты', 250, 23)
    new_order = Product('Грейпфрут', 'Фрукт горьковатый', 149, 15)
    Order.add_product(new_order)
    print(Order.ordered_product_list)
    print(order.products_in_list)

