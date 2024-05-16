import factory
from faker import Faker

from ..models import CurrentModel, RelCurrent

fake = Faker()


class CurrentModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CurrentModel

    name = fake.name()
    count = fake.random_digit()


class RelCurrentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RelCurrent

    current = factory.SubFactory(CurrentModelFactory)
    text = fake.text()
