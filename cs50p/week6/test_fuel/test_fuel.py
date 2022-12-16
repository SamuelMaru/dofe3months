from fuel import convert, gauge
def test_convert():
    assert convert("0/1") == 0
    assert convert("1/2") == 50
    assert convert("4/4") == 100

def test_gauge()
    assert gauge(100)=="F"
    assert gauge(0)=="E"


