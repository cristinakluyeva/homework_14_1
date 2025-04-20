from src.product import Product
from src.buying import Buying
from src.exceptions import ZeroProductQuantity


class Category(Buying):
    """Класс представляет категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name  # Название категории
        self.description = description  # Описание категории
        self.__products = products  # список товаров, входящих в данную категорию
        Category.category_count += 1  # количество категорий
        Category.products_count += len(self.__products)  # количество товаров по данной категории

    def __str__(self):
        sum_products = sum(prod.quantity for prod in self.__products)
        return f'{self.name}, количество продуктов: {sum_products} шт.'

    @property
    def products(self):
        products_str = ''
        for prod in self.__products:
            products_str += f'{prod.name}, Цена: {prod.price}, Остаток: {prod.quantity}\n'
        return products_str

    def add_product(self, new_product: Product):
        if isinstance(new_product, Product):
            try:
                if new_product.quantity == 0:
                    raise ZeroProductQuantity('Товар с нулевым количеством не может быть добавлен')
            except ZeroProductQuantity:
                print('Проверьте количество товаров в категории. Возможно вы забыли их добавить.')
            else:
                self.__products.append(new_product)
                Category.products_count += 1
                print('Операция прошла успешно! Товар добавлен в категорию')
            finally:
                print('Обработка добавления товара завершена')
        else:
            raise TypeError

    @property
    def products_in_list(self):
        return self.__products

    def average_cost(self):
        average_cost = 0  # Создаем переменную средней стоимости товаров
        try:  # Попытка вычисления средней стоимости товаров:
            average_cost = sum([prod.price for prod in self.__products]) / len(self.__products)
            return average_cost
        except ZeroDivisionError:  # При возникновении исключения, возвращаем первоначальное значение переменной:
            return average_cost
