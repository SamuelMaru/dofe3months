from vanity import is_valid

def short(plate):
    assert is_valid("A") == False

def long(plate):
    assert is_valid("1234567") == False

def nums(plate):
    assert is_valid("AAA22A") == False

def punc(plate):
    assert is_valid("AD>!%M,.") == False

