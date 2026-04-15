import pytest

@pytest.mark.parametrize("a, b", [(1,2), (3,4), (5,6)])
def test_add(a, b):
    print(a+b)


