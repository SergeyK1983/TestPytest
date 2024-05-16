import pytest


@pytest.mark.django_db
def test_current_model_factory(current_model_factory, rel_current_factory):
    model_cu = current_model_factory.create()
    # rm = rel_current_factory.create()

    print("model_cu: ", model_cu.id)
    # print("rm: ", rm.current)

    assert model_cu.id


@pytest.mark.django_db
def test_current_model_factory(rel_current_factory):
    rm = rel_current_factory.create()

    assert rm.current
