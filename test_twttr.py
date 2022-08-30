from twttr import shorten


def main():

    test_upper()
    test_lower()


def test_upper():
    try:
        assert shorten("KENNY CHOW") == "KNNY CHW"
        assert shorten("AEIOU123") == "123"
    except AssertionError:
        print("Test failed with uppercase")


def test_lower():
    try:
        assert shorten("what is your name") == "wht s yr nm"
        assert shorten("aeiou123") == "123"
    except AssertionError:
        print("Test failed with lowercase")


if __name__ == "__main__":
    main()
