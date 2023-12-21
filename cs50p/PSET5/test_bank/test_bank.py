from bank import value


def main():
    test_value()


def test_value():
    # Uppercase Hello
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    # Lowercase hello
    assert value("hello") == 0
    assert value("hello, world") == 0

    # Uppercase H
    assert value("How you doing?") == 20
    assert value("Hi") == 20
    # Lowercase h
    assert value("hi") == 20
    assert value("hey how ya doin") == 20

    # Uppercase
    assert value("What's happening?") == 100
    assert value("What") == 100
    # Lowercase
    assert value("good morning") == 100
    assert value("god this test sucks") == 100


if __name__ == "__main__":
    main()