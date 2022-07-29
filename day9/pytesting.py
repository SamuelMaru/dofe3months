import pytest
def even(x):
    return x%2 == 0


@pytest.mark.parametrize("x", [
    (40),
    (50),
    (60)
])

def test_1(x):
    assert even(x)==True
