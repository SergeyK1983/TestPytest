import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from .factories import CurrentModelFactory, RelCurrentFactory

register(CurrentModelFactory)  # => current_model_factory
register(RelCurrentFactory)  # => rel_current_factory


@pytest.fixture
def api_client():
    return APIClient
