import pytest

from src.product import Product
from src.exceptions import ZeroProductQuantity


def test_category_init(get_category):
    assert get_category.name == 'Paper for office and artist'
    assert get_category.description == 'These products are for office(printing) and artists works'
    assert get_category.products_count == 3
    assert get_category.category_count == 1


def test_products_property(get_category):
    assert get_category.products == ('Sketchbook, Цена: 350.0, Остаток: 13\n'
                                     'Notebook, Цена: 45.8, Остаток: 113\n'
                                     'Album, Цена: 113.0, Остаток: 23\n')


def test_add_product(get_category, get_product):
    assert len(get_category.products_in_list) == 3
    get_category.add_product(get_product)
    assert len(get_category.products_in_list) == 4


def test_category_str(get_category):
    assert str(get_category) == 'Paper for office and artist, количество продуктов: 149 шт.'


def test_Category_Iterator(category_iterator):
    iter(category_iterator)
    assert category_iterator.index == 0
    assert next(category_iterator).name == 'Sketchbook'
    assert next(category_iterator).name == 'Notebook'
    assert next(category_iterator).name == 'Album'

    with pytest.raises(StopIteration):
        next(category_iterator)


def test_category_add_product_error(get_category):
    with pytest.raises(TypeError):
        class Test:
            pass
        test = Test()
        get_category.add_product(test)


def test_category_add_product_periodic_task(get_category, smartphone_1):
    get_category.add_product(smartphone_1)
    assert get_category.products_in_list[-1].name == 'Nokia G400 5G'


def test_average_cost(get_category, category_without_products):
    assert get_category.average_cost() == 169.6
    assert category_without_products.average_cost() == 0


def test_average_cost_exception(capsys, get_category):
    product_add = Product('Brush', 'Drawing instrument', 190, 3)

    get_category.add_product(product_add)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-2] == 'Операция прошла успешно! Товар добавлен в категорию'
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'


def test_category_error(get_category):
    with pytest.raises(ValueError):
        get_category.add_product(Product('Томаты', 'Овощи', 250, 0))
