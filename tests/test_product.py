from src.product import Product
from mock import patch


def test_product_init(get_product):
    assert get_product.name == 'Sketchbook'
    assert get_product.description == 'This book intended to be used for drawing with pens and pencils. Format: square 20x20'
    assert get_product.price == 350.0
    assert get_product.quantity == 13


def test_new_product():
    test_product = {'name': 'pen',
                     'description': 'writing material',
                     'price': 25.0,
                     'quantity': 20}
    Product.new_product = test_product
    assert Product.new_product == {'name': 'pen', 'description': 'writing material', 'price': 25.0, 'quantity': 20}
    test_product_dublicate = {'name': 'pen',
                    'description': 'writing material',
                    'price': 250.0,
                    'quantity': 45}
    Product.new_product = test_product_dublicate
    assert Product.new_product == {'name': 'pen', 'description': 'writing material', 'price': 250.0, 'quantity': 45}


def test_price_property(get_product):
    assert get_product.price == 350.0


@patch("builtins.input")
def test_price_setter(mock_input, capsys, get_product):
    get_product.price = 400.5
    assert get_product.price == 400.5

    get_product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    mock_input.return_value = "y"
    get_product.price = 340.5
    assert get_product.price == 340.5
