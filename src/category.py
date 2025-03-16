from src.product import Product


class Category:
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

    @property
    def products(self):
        products_str = ''
        for prod in self.__products:
            products_str += f'{prod.name}, Цена: {prod.price}, Остаток: {prod.quantity}\n'
        return products_str

    @products.setter
    def products(self, new_product: Product):
        self.__products.append(new_product)
        Category.products_count += 1

    @property
    def products_in_list(self):
        return self.__products


if __name__ == '__main__':
    cat_1 = Category('Овощи', 'Растительные продукты', [Product('помидоры', 'красный, содержит много витамина С', 250.0, 13),
    Product('огурцы', 'диетический продукт, содержит много воды', 149.99, 20),
    Product('кабачки', 'сильное мочегонное средство', 325.7, 120),
    Product('морковь', 'содержит много клетчатки и витамин К', 45.0, 37)])
    print(cat_1.name, cat_1.description, Category.category_count)
    print(cat_1.products)
    # new_product = Product('свекла', 'Восстанавливает кровеснабжение', 50.0, 40)
    cat_1.products = Product('свекла', 'Восстанавливает кровеснабжение', 50.0, 40)
    print(cat_1.products)
    print(Category.products_count, cat_1.products_in_list)
