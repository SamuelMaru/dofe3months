from bank import value

def value_hello():
    assert value("Hello") == "$0"

def value_hello():
    assert value("Hello, Newman") == "$0"

def value_hello():
    assert value("How you doing?") == "$20"

def value_hello():
    assert value("What's happening?") == "$100"