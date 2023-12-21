import pytest
from jar import Jar
from emoji import emojize


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()



def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

def test_str():
    jar = Jar()
    assert Jar.__str__(jar) == ""
    jar.deposit(1)
    assert Jar.__str__(jar) == emojize(":cookie:") * 1
    jar.deposit(11)
    assert Jar.__str__(jar) == emojize(":cookie:") * 12

def test_deposit():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(1)
    assert jar.size == 1
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(100)

def test_withdraw():
    jar = Jar()
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(100)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.withdraw(6)
    jar.withdraw(5)
    assert jar.size == 0

    # assert jar.withdraw(jar, 1)

if __name__ == "__main__":
    main()