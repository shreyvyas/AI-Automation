import pytest

@pytest.fixture
def sample_data():
    return "joy"


@pytest.fixture
def test_data():
    return {
        "username": "shrey",
        "password": "test"
    }


def test_printName(sample_data):
    assert "joy" == sample_data


def test_printUserDetails(test_data):
    print(test_data["username"])
    print(test_data["password"])