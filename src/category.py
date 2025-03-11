class Category:
    """Класс представляет категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name # Название категории
        self.description = description # Описание категории
        self.products = products # список товаров, входящих в данную категорию
        Category.category_count += 1 # количество категорий
        Category.products_count += len(self.products) # количество товаров по данной категории
