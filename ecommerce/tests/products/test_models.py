import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModels:
    def test_str_method(self, category_factory):
        # Arrange

        # Act
        category = category_factory(name="test_category")

        # Assert
        assert category.__str__() == "test_category"

class TestBrandModels:
    def test_str_method(self, brand_factory):
        # Arrange

        # Act
        brand = brand_factory(name="test_brand")

        # Assert
        assert brand.__str__() == "test_brand"


class TestProductModels:
    def test_str_method(self, product_factory):
        # Arrange

        # Act
        product = product_factory(name="test_product")

        # Assert
        assert product.__str__() == "test_product"
