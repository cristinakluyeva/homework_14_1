import pytest

from src.category_iterator import CategoryIterator
from src.product import Product
from src.category import Category
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


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


@pytest.fixture
def smartphone_1():
    return Smartphone('Nokia G400 5G', 'Android system', 25000, 19, 'Snapgragon 480 Plus, 4', 'Nokia', '64Gb')


@pytest.fixture
def smartphone_2():
    return Smartphone('Sony Xperia', 'The device include: Music Pro, Video Pro, Cinema Pro and PlayStationApp...', 50000, 5, 'Qualcomm Snapgragon 8 Gen in 1, 8', 'Sony', '256Gb')


@pytest.fixture
def lawngrass_1():
    return LawnGrass('Green field', 'Short and soft cover', 1200, 10, 'Russia', '30 days', 'green')


@pytest.fixture
def lawngrass_2():
    return LawnGrass('Football grass', 'Ideal for sport area', 3500, 100, 'USA', '40 days', 'light green')