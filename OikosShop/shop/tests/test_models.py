from unicodedata import name
from django.test import TestCase

import shop.models as models

class CategoryTests(TestCase):
    """Тесты для модели категорий"""
    
    @classmethod
    def setUpTestData(cls) -> None:
        """Заполняет тестовые данные перед запуском тестов"""
        cls.category = models.Category.objects.create(
            name = "Профиль KS"
        )
        return super().setUpTestData()
    
    def test_verbose_name(self):
        pass
    
    
class ProductTests(TestCase):
    """Тесты для модели продуктов"""
    
    def test_verbose_name(self):
        pass