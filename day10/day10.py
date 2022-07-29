import pytest

def divide(a,b):
  if b == 0:
    raise ZeroDivisionError("Second arguement cannot be 0")
  return (a//b,a%b)



@pytest.mark.parametrize("x, y" [(list(zip([ele for ele in range(1000)], [ele for ele in range(1000)])))])
def test_divide(x,y):
    assert divide(x,y) == True
