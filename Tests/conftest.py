import pytest

@pytest.fixture
def setup_testdata():
    return {
        "username": "testuser",
        "password": "test123"
    }

@pytest.fixture
def setup():
    print("Opening the Browser")

    yield

    print("Closing the Browser")