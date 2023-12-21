from numb3rs import validate


def main():
    test_false()

def test_false():
    # outside bounds
    assert validate("256.0.0.0") == False
    assert validate("-1.0.0.0") == False
    assert validate("0.256.0.0") == False

    # alphabetical
    assert validate("a.0.0.0") == False
    assert validate("cat") == False

    # not enough integers
    assert validate("0.0.0") == False


def test_true():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("100.100.100.100") == True


if __name__ == "__main__":
    main()