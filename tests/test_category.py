def test_category_init(get_category):
    assert get_category.name == 'Paper for office and artist'
    assert get_category.description == 'These products are for office(printing) and artists works'
    assert get_category.products_count == 3
    assert get_category.category_count == 1

def test_products_property(get_category):
    assert get_category.products == ('Sketchbook, Цена: 350.0, Остаток: 13\n'
                                     'Notebook, Цена: 45.8, Остаток: 113\n'
                                     'Album, Цена: 113.0, Остаток: 23\n')

def test_products_setter(get_category, get_product):
    assert len(get_category.products_in_list) == 3
    get_category.products = get_product
    assert len(get_category.products_in_list) == 4
