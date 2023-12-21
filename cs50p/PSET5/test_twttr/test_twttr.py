from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("aeioux") == "x"
    assert shorten("AEIOUx") == "x"
    assert shorten("aeiouX") == "X"
    assert shorten("aeiou1") == "1"
    assert shorten("aeiou.") == "."

if __name__ == "__main__":
    main()