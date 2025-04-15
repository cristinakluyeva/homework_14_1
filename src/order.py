from src.product import Product
from src.buying import Buying
from src.exceptions import ZeroProductQuantity

class Order(Product, Buying):
    """Класс представляет кол-воо заказанных товаров"""
    ordered_product_list =[] # Создаем список заказанных товаров

    def __init__(self, name, description, price, quantity, color=None):
        super().__init__(name, description, price, quantity,color)
        if self.__class__.__name__=='Order':
            Order.ordered_product_list.append(self)
        else:
            print("Используйте метод add_product")  # При создании экземпляра класса, сразу добавляем его в список заказанных товаров

    def __str__(self):
        return f'Заказали: {self.name}. Кол-во: {self.quantity}. Сумма заказа: {self.quantity * self.price}.'

    @classmethod
    def add_product(cls, new_product: Product):
        if isinstance(new_product, Product):
            try:
                if new_product.quantity <= 0:
                    raise ZeroProductQuantity('Товар с нулевым количеством не может быть добавлен')
            except ZeroProductQuantity as e:
                print(str(e))
            else:
                name = new_product.name
                description = new_product.description
                price = new_product.price
                quantity = new_product.quantity
                color = new_product.color if new_product.color else None
                print('Операция прошла успешно! Товар добавлен в заказ')
                return cls(name, description, price, quantity, color)
            finally:
                print('Обработка добавления товара в заказ завершена')
        else:
            raise TypeError

    @classmethod
    def products_in_list(cls):
        """Метод выводит все заказы: их общее кол-во и стоимость"""
        joined_order_names = [prod.name for prod in cls.ordered_product_list]
        quantity_order = sum(prod.quantity for prod in  cls.ordered_product_list)
        price_order = sum([(prod.quantity * prod.price) for prod in cls.ordered_product_list])
        return f'Заказали: {','.join(joined_order_names)}. Кол-во: {quantity_order}. Сумма заказа: {price_order}.'


