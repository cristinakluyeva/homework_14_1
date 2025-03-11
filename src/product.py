class Product:
    """Класс представляет информацию о товаре: название, описание, цена, количество"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name # Название товара/продукта
        self.description = description # Описание товара
        self.price = price # Стоимость товара
        self.quantity = quantity # Доступное количество товара(в наличие/ на складе)
