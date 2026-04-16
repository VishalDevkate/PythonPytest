import pytest

@pytest.fixture
def setup(scope="function"):
    print("setup")

def teardown():
    print("teardown")

def test_firstTC(setup):
    print("This is first test case")

def test_secondTC(setup):
    print("This is second test Case")

def test_thirdTC(setup):
    print("This is third Test Case")