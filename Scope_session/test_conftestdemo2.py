import pytest


@pytest.fixture(scope="module")
def demo2_setup():
    print("demo2_setup")

def test_thirdTC(setup_conftest):
    print("This is third test case")

def test_fourthTC(demo2_setup):
    print("This is fourth test case")