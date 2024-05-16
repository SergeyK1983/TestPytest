import pytest


@pytest.mark.django_db
def test_current_model_factory(current_model_factory):
    model_cu = current_model_factory.create()
    assert model_cu.id


@pytest.mark.django_db
def test_rel_current_factory(rel_current_factory):
    rm = rel_current_factory.create()
    assert rm.current
