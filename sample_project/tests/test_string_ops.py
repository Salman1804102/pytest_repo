from string_ops import reverse, to_upper

def test_reverse():
    assert reverse("abc") == "cba"
    assert reverse("") == ""

def test_to_upper():
    assert to_upper("abc") == "ABC"
    assert to_upper("PyTest") == "PYTEST"
