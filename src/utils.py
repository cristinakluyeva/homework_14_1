import json
import os


from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """Чтение json-файла"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def create_data_from_json(data):
    """Создание экземпляров класса Product из данных json-файла"""
    product_data = []
    for product in data:
        products_list = []
        for p in product["products"]:
            products_list.append(Product(**p))
        product["products"] = products_list
        product_data.append(Category(**product))
    return product_data


if __name__ == '__main__':
    user_products = read_json('../data/products.json')
    users_data = create_data_from_json(user_products)
    print(user_products)
    print(users_data[0].name)
    print(users_data[0].products_count)
