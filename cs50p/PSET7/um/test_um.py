from um import count


def main():
    test_count()

def test_count():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
    assert count(" um ") == 1
    assert count("Hello um,") == 1
    assert count("Hello um, um") == 2
    assert count("um, um") == 2
    assert count("um?") == 1


def test_num():
    assert count("um0") == 0
    assert count("0um") == 0

def test_pos():

    assert count("yum") == 0
    assert count("umy") == 0
    assert count("umum") == 0

