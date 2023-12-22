import factory
from ecommerce.products.models import Brand, Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "test_product"
    description = "test_description"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
