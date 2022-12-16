from twttr import shorten


def test_no_vowel():
    assert shorten("nvls") == "nvls"


def test_cap_vowel():
    assert shorten("CAPSVOWELS") == "CPSVWLS"


def test_low_vowel():
    assert shorten("assert") == "ssrt"


def test_nums():
    assert shorten("20915CSUHt2") == "20915CSHt2"


def test_punc():
    assert shorten("hi, testing!") == "h, tstng!"