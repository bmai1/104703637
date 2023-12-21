import pytest
from working import convert


def main():
    test_convert()


def test_convert():
    # NEED TO DO SEPERATE EXCEPTION HANDLING TESTS FOR CHECK50
    with pytest.raises(ValueError):
        # ValueError omitting "to"
        convert("09:00 AM - 17:00 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM - 5:00 PM")
    with pytest.raises(ValueError):
        convert("9 - 10")
    with pytest.raises(ValueError):
        convert("9 / 10")
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
        # ValueError out of range
    with pytest.raises(ValueError):
        convert("9:00 AM to 13:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        convert("3:72 PM to 2:41 AM")

    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:05 AM to 5:05 PM") == "09:05 to 17:05"


if __name__ == "__main__":
    main()