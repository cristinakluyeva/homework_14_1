def test_product_init(get_product):
    assert get_product.name == 'Sketchbook'
    assert get_product.description == 'This book intended to be used for drawing with pens and pencils. Format: square 20x20'
    assert get_product.price == 350.0
    assert get_product.quantity == 13
