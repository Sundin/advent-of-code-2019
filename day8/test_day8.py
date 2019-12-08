from day8 import *


def test_count_digits():
    assert count_digits("11122", 1) == 3
    assert count_digits("01230123", 3) == 2


def test_get_image_layers():
    assert get_image_layers("123456789012", 3, 2) == ["123456", "789012"]
