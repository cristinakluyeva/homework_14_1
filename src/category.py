class Category:
    """Класс представляет категории товаров"""
    name: str
    description: str
    products: list
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count +=1
        Category.products_count += len(self.products)