import pytest


@pytest.fixture(scope="function")
def demo2_setup():
    print("demo2_setup")
    yield
    print("demo2_setup teardown")

def test_thirdTC(setup_conftest):
    print("This is third test case")

@pytest.mark.smoke
def test_fourthTC(demo2_setup):
    print("This is fourth test case")