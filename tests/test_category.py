import pytest
from src.category import Category
from src.product import Product


@pytest.fixture
def products_list():
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Gray", 180000.0, 5),
        Product("Iphone 15 Pro", "128GB, Blue", 210000.50, 3)
    ]


def test_category_init(products_list):
    """Тест корректности инициализации объекта Category."""
    # Перед созданием сбрасываем счетчики, чтобы тесты не зависели друг от друга
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Электронные гаджеты", products_list)

    assert category.name == "Смартфоны"
    assert category.description == "Электронные гаджеты"
    assert len(category.products) == 2


def test_category_counters(products_list):
    """Тест подсчета количества категорий и количества продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    # Создаем первую категорию без сохранения в переменную
    Category("Смартфоны", "Гатжеты", products_list)
    assert Category.category_count == 1
    assert Category.product_count == 2

    # Создаем вторую категорию без сохранения в переменную
    Category("Аксессуары", "Чехлы и зарядки", [])
    assert Category.category_count == 2
    assert Category.product_count == 2

from src.utils import load_data_from_json


def test_load_data_from_json():
    """Тест корректности загрузки данных из JSON."""
    Category.category_count = 0
    Category.product_count = 0

    # Передаем путь к нашему созданному products.json
    categories = load_data_from_json("products.json")

    assert len(categories) == 1
    assert categories[0].name == "Смартфоны"
    assert len(categories[0].products) == 2
    assert categories[0].products[0].name == "Samsung Galaxy S23 Ultra"
