import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from .factories import CurrentModelFactory, RelCurrentFactory

register(CurrentModelFactory)  # => current_model_factory
register(RelCurrentFactory)  # => rel_current_factory

# примечание стереть
@pytest.fixture
def api_client():
    return APIClient


@pytest.fixture(scope="session")
@pytest.mark.django_db
def get_some_current_obj(current_model_factory, rel_current_factory) -> None:
    instance = current_model_factory.create()
    rel_current_factory.create(current=instance)
    rel_current_factory.create(current=instance)

    return None
