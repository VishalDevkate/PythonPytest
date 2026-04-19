import pytest

@pytest.fixture(scope="module")
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

def test_fourthTC(setup):
    print("This is fourth Test Case")
