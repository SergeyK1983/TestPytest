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
