import pytest

@pytest.fixture(scope="function")
def setup_conftest():
    print("executing setup from conftest.py file")