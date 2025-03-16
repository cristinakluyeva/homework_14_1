class Product:
    """Класс представляет информацию о товаре: название, описание, цена, количество"""
    name: str
    description: str
    price: float
    quantity: int
    product_class_list = []

    def __init__(self, name, description, price, quantity):
        self.name = name # Название товара/продукта
        self.description = description # Описание товара
        self.__price = price # Стоимость товара
        self.quantity = quantity # Доступное количество товара(в наличие/ на складе)
        Product.product_class_list.append({'name': self.name,
                                           'description': self.description,
                                           'price': self.__price,
                                           'quantity': self.quantity})

    @classmethod
    def new_product(cls, add_product:dict):
        for products_dict in cls.product_class_list:
                if products_dict['name'] == add_product['name']:
                    products_dict['quantity'] += add_product['quantity']
                    if products_dict['price'] < add_product['price']:
                        products_dict['price'] = add_product['price']
                    return products_dict
                else:
                    name = add_product ['name']
                    description = add_product['description']
                    price = add_product['price']
                    quantity = add_product['quantity']
                    return cls(name, description, price, quantity)

    @property
    def price(self):
        """Возвращает приватный атрибут класса"""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """Повышает или понижает стоимость товара новую цену на товар"""
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif 0 <new_price <= self.__price:
            user_input = input('Если вы хотите понизить стоимость товара введите: yes')
            if user_input.startswith(('Y','y','У', 'у')):
                self.__price = new_price
        elif new_price > self.price:
            self.__price = new_price
        return self.__price
