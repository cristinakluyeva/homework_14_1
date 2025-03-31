import pytest


def test_lawngrass_init(lawngrass_1):
    assert lawngrass_1.name == 'Green field'
    assert lawngrass_1.description == 'Short and soft cover'
    assert lawngrass_1.price == 1200
    assert lawngrass_1.quantity == 10
    assert lawngrass_1.color == 'green'
    assert lawngrass_1.country == 'Russia'
    assert lawngrass_1.germination_period == '30 days'


def test_smartphone_add(lawngrass_1, lawngrass_2):
    assert lawngrass_1 + lawngrass_2 == 362000


def test_smartphone_add_error(lawngrass_2, smartphone_2):
    with pytest.raises(TypeError):
        smartphone_2 + lawngrass_2
