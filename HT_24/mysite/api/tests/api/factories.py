import factory

from products.models import Product, Category


class CategoryFactory(factory.django.DjangoModelFactory):
    
    name = factory.Sequence(lambda n: f"Category {n}")
    
    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    
    name = factory.Sequence(lambda n: f"Product {n}")
    price = factory.Faker('random_number', digits=2)
    product_id = factory.Faker('uuid4')
    description = factory.Faker('text')
    brand = factory.Faker('company')
    category = factory.SubFactory(CategoryFactory)
    link = factory.Faker('url')
    
    class Meta:
        model = Product