#parameterized fixture and parameterized test demo

import pytest

# Parametrized fixture
@pytest.fixture(params=[("Alice", 30), ("Bob", 25)])
def person(request):
    return request.param

# Parametrized test
@pytest.mark.parametrize("field,expected_type", [
    ("name", str),
    ("age", int),
])
def test_person_fields(person, field, expected_type):
    name, age = person
    data = {"name": name, "age": age}
    assert isinstance(data[field], expected_type)
