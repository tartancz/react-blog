import factory
from faker import Faker
from pytest_factoryboy import register
from allauth.account.models import EmailAddress

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


fake = Faker()

class EmailAddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailAddress


@register
class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f"NotHomer{n}")
    first_name = factory.Sequence(lambda n: f"Homer{n}")
    last_name = factory.Sequence(lambda n: f"Simpson{n}")
    email = factory.Sequence(lambda n: f"Homer{n}@simpson.com")
    password = factory.LazyFunction(lambda: make_password('hesloheslo'))

    class Meta:
        model = get_user_model()
