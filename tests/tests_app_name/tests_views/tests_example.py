import pytest

from app_name.models.example import Example
from app_name.views.example import ExampleApiView


@pytest.mark.django_db
def test_example_get():
    Example.objects.bulk_create([
        Example(name='Larry', choice=Example.CHOICE_1, is_something=True),
        Example(name='Curly', choice=Example.CHOICE_2, is_something=False),
        Example(name='Moe', choice=Example.CHOICE_3, is_something=True)])

    example_api_view = ExampleApiView()
    data = example_api_view._get_list()

    assert len(data) == 3
