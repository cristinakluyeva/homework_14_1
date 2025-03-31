import pytest


def test_smartphone_init(smartphone_1):
    assert smartphone_1.name == 'Nokia G400 5G'
    assert smartphone_1.description == 'Android system'
    assert smartphone_1.price == 25000
    assert smartphone_1.quantity == 19
    assert smartphone_1.efficiency == 'Snapgragon 480 Plus, 4'
    assert smartphone_1.model == 'Nokia'
    assert smartphone_1.memory == '64Gb'
    assert smartphone_1.color == None


def test_smartphone_add(smartphone_1, smartphone_2):
    assert smartphone_1 + smartphone_2 == 725000


def test_smartphone_add_error(smartphone_1, lawngrass_1):
    with pytest.raises(TypeError):
        smartphone_1 + lawngrass_1

