import pytest
from pytest_factoryboy import register

from .factories import CurrentModelFactory, RelCurrentFactory

register(CurrentModelFactory)  # => current_model_factory
register(RelCurrentFactory)  # => rel_current_factory
