import pytest


@pytest.fixture(scope="function")
def setup_demo1():
    print("demo1 setup")
    return "pass"

@pytest.mark.smoke
def test_firstTC(setup_conftest):
    print("This is first test case")

@pytest.mark.skip(reason="skip test")
def test_secondTC(setup_conftest):
    print("This is second test case")

def test_fifthTC(setup_demo1):
    print("This is fifth test case")
    assert setup_demo1 == "pass"

