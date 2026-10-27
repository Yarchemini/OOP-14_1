from src.product import Product


class Category:
    """Класс для представления категории товаров."""

    # Атрибуты класса для автоматического подсчета количества
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # Автоматически увеличиваем счетчик категорий при создании нового объекта
        Category.category_count += 1
        # Считаем количество уникальных товаров (длину списка), добавленных в эту категорию
        Category.product_count += len(self.products)
