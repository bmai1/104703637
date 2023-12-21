import pytest
from project import setGuess, guessValidator, hint

def main():
    test_guessValidator()

def test_guessValidator():
    with pytest.raises(ValueError):
        guessValidator("abcde")
        guessValidator("123456")
        guessValidator("1234")
        guessValidator(".1234")


if __name__ == "__main__":
    main()