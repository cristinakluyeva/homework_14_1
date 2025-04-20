from src.product import Product
from src.smartphone import Smartphone
from src.lawngrass import LawnGrass


def test_print_mixin_product(capsys):
    Product("Спаржа", "Соевый продукт", 256, 10, "бежевый")
    message1 = capsys.readouterr()
    assert message1.out.strip() == 'Product(Спаржа, Соевый продукт, 256, 10)'


def test_print_mixin_smartphone(capsys):
    Smartphone("LG", "Mobile device", 30000, 10, "Super", "LG", "128Gb", "black")
    message1 = capsys.readouterr()
    assert message1.out.strip() == 'Smartphone(LG, Mobile device, 30000, 10)'


def test_print_mixin_lawngrass(capsys):
    LawnGrass("long grass", "For decoration", 5000, 250, "Sweden", "40-50 days", "blue and green")
    message1 = capsys.readouterr()
    assert message1.out.strip() == 'LawnGrass(long grass, For decoration, 5000, 250)'
