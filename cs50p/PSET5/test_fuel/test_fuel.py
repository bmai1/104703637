import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("1.5/1")
        convert("a/1")

    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("2/0")

    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"


if __name__ == "__main__":
    main()