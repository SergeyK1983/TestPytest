import json
import pytest
from django.urls import reverse
from rest_framework import status
from django.test.client import encode_multipart

from ..models import CurrentModel


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


@pytest.mark.django_db
def test_current_create(api_client, current_model_factory, rel_current_factory):
    endpoint = f"{reverse('current-create')}"

    data = {'name': 'serg', 'description': 'sfsdfsdf', 'count': 2}
    content = encode_multipart('BoUnDaRyStRiNg', data)
    content_type = 'multipart/form-data; boundary=BoUnDaRyStRiNg'

    response = api_client().post(endpoint, data=content, content_type=content_type)
    cur = CurrentModel.objects.all().last()

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == data
    assert cur.name == data["name"]
