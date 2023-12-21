from plates import is_valid


def main():
    test_1()
    test_2()
    test_3()
    test_4()


# All vanity plates must start with at least two letters
def test_1():
    assert is_valid("1AABB") == False
    assert is_valid("1") == False
    assert is_valid("11") == False
    assert is_valid("11AABB") == False
    assert is_valid("AAA222") == True


# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
def test_2():
    assert is_valid("AAAAAAA") == False
    assert is_valid("AA11111") == False
    assert is_valid("A") == False


# Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.
def test_3():
    assert is_valid("AA22AA") == False
    assert is_valid("AA00AA") == False
    assert is_valid("AA01AA") == False
    assert is_valid("AAAA0") == False


# No periods, spaces, or punctuation marks are allowed.
def test_4():
    assert is_valid("AA2 2AA") == False
    assert is_valid("!AA22AA") == False
    assert is_valid(".AA22AA") == False
    assert is_valid("?AA22AA") == False
    assert is_valid("'AA22AA") == False
    assert is_valid(",AA22AA") == False
    assert is_valid(" AA") == False
    assert is_valid("AA'AA") == False
    assert is_valid("AA-AA") == False
    assert is_valid("AA(AA") == False
    assert is_valid("AA:AA") == False
    assert is_valid("AA;AA") == False


if __name__ == "__main__":
    main()