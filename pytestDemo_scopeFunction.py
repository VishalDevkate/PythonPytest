import pytest

@pytest.fixture(scope="function")
def setup():
    print("setup")
    yield
    print("teardown")

def test_firstTC(setup):
    print("This is first test case")

def test_secondTC(setup):
    print("This is second test Case")

def test_thirdTC(setup):
    print("This is third Test Case")

def test_fourthTC():     #setup and teardown not called here
    print("This is fourth Test Case")
