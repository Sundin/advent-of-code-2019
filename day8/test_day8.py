from day8 import *


def test_count_digits():
    assert count_digits("11122", 1) == 3
    assert count_digits("01230123", 3) == 2


def test_get_image_layers():
    assert get_image_layers("123456789012", 3, 2) == ["123456", "789012"]


def test_get_pixel_in_position():
    data = "0222112222120000"
    width = 2
    height = 2
    assert get_pixel_in_position(data, width, height, 0) == "0"
    assert get_pixel_in_position(data, width, height, 1) == "1"
    assert get_pixel_in_position(data, width, height, 2) == "1"
    assert get_pixel_in_position(data, width, height, 3) == "0"
