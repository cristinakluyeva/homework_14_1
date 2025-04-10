from src.order import Order


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

