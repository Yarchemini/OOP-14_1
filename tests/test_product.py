import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5)


def test_product_init(sample_product):
    """Тест корректности инициализации объекта Product."""
    assert sample_product.name == "Samsung Galaxy S23 Ultra"
    assert sample_product.description == "256GB, Gray"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5
