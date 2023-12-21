import pytest
from seasons import validateDob


def main():
    test_input()


def test_input():
    with pytest.raises(SystemExit):
        validateDob("01-01-1999")
        validateDob("01/01/1999")
        validateDob("01-01-99")
        validateDob("01/01/99")
        validateDob("YYYY-MM-DD")
        validateDob("YYYY/MM/DD")
        validateDob("DD-MM-YYYY")
        validateDob("DD/MM/YYYY")
        validateDob("January 1, 2000")
        validateDob("January 1st, 2000")


if __name__ == "__main__":
    main()