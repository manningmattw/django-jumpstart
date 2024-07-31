import pytest
from app_name.models.example import Example


@pytest.mark.django_db
def test_example_model_values_phrase():
    example = Example.objects.create(
        name='Bob',
        choice=Example.CHOICE_2,
        is_something=True)

    assert example.values_phrase == "Bob (2nd) is something"
