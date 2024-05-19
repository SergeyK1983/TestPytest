import json
import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_app_list(api_client, current_model_factory):
    endpoint = f"{reverse('app-list')}"

    inst = current_model_factory.create()
    current_model_factory.create()

    response = api_client().get(endpoint)
    content = json.loads(response.content)
    assert response.status_code == status.HTTP_200_OK
    assert content[0]["name"] == inst.name
    assert len(content) == 2
    assert len(content[0]) == 5
    assert response.data[0]["name"] == inst.name  # то же самое что и content, но OrderedDict


@pytest.mark.django_db
def test_app_list_id(api_client, current_model_factory, rel_current_factory):
    instance = current_model_factory.create()
    rel_current_factory.create(current=instance)
    rel_current_factory.create(current=instance)

    endpoint = f"{reverse('app-list-id', kwargs={'id': 1})}"
    response = api_client().get(endpoint)
    data = response.data

    assert response.status_code == status.HTTP_200_OK
    assert len(data) == 1
    assert len(data[0]["current"]) == 2
