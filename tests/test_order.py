import pytest

from src.order import Order
from src.product import Product


def test_order_init(order_1):
    assert order_1.name == 'Груша'
    assert order_1.description == 'Фрукты'
    assert order_1.quantity == 23
    assert order_1.price == 250


def test_order_add_product(order_2):
    Order.add_product(order_2)
    assert Order.ordered_product_list[-1].name == 'Шоколад'


def test_order_products_in_list(capsys, order_1):
    print(Order.products_in_list())

    message = capsys.readouterr()
    assert message.out.strip() == ('Order(Груша, Фрукты, 250, 23)\n'
                                   'Заказали: Груша. Кол-во: 23. Сумма заказа: 5750.')
    # assert message.out.strip() == ('Order(Груша, Фрукты, 250, 23)\n' 'Заказали: Груша,Шоколад,Груша. Кол-во: 96. Сумма заказа: 18450.')


def test_order_add_zero_product():
    with pytest.raises(ValueError):
        Order.add_product(Product('Шоколад', 'Сладости', 139, -4))
