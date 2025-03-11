def test_category_init(get_category):
    assert get_category.name == 'Paper for office and artist'
    assert get_category.description == 'These products are for office(printing) and artists works'
    assert get_category.products_count == 3
    assert get_category.category_count == 1
