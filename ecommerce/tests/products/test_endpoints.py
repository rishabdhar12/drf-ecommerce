import factory
import pytest
import json

pytestmark = pytest.mark.django_db

class TestCategoryEndpoints:
    endpoint = "/api/category/"

    def get_test_category(self, category_factory, api_client):
        category_factory.create_batch(4)
        response = api_client().get(self.endpoint)
        print(json.loads(response.content))
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4

class TestBrandEndpoints:
    pass

class TestProductEndpoints:
    pass
