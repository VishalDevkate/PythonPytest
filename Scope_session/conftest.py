import pytest

@pytest.fixture(scope="session")
def setup_conftest():
    print("executing setup from conftest.py file")