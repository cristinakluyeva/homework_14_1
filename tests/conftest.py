import pytest

from src.category_iterator import CategoryIterator
from src.product import Product
from src.category import Category


@pytest.fixture
def get_product():
    return Product(
        name='Sketchbook',
        description='This book intended to be used for drawing with pens and pencils. Format: square 20x20',
        price=350.0,
        quantity=13

    )


@pytest.fixture
def get_product1():
    return Product(
        name='Album',
        description='This book intended to be used for drawing with colors and acrylic. Format: square 15x35',
        price=230.0,
        quantity=48

    )


@pytest.fixture
def get_category():
    return Category(
        name='Paper for office and artist',
        description='These products are for office(printing) and artists works',
        products=[Product('Sketchbook', 'This book intended to be used for drawing with pens and pencils. Format: square 20x20', 350.0, 13),
                  Product('Notebook', 'This notebook intended to be used for drawing and writing with pens and pencils.', 45.8, 113),
                  Product('Album', 'This album intended to be used for drawing with gouche. Format: square 40x15', 113.0, 23)]
    )


@pytest.fixture
def category_iterator(get_category):
    return CategoryIterator(get_category)
