from plate import is_valid


def main():
    test_7char()
    test_start_w_letter()
    test_punctuation()
    test_firstnum_zero()
    test_digit_in_mid()


def test_7char():
    try:
        assert is_valid("ASDFGHE") == False
    except AssertionError:
        print("Test failed with test_7char")


def test_start_w_letter():
    try:
        assert is_valid("00FSAS") == False
    except AssertionError:
        print("Test failed with test_start_w_letter")


def test_punctuation():
    try:
        assert is_valid("AAA,AA") == False
    except AssertionError:
        print("Test failed with test_punctuation")


def test_firstnum_zero():
    try:
        assert is_valid("AAAA02") == False
    except AssertionError:
        print("Test failed with test_firstnum_zero")


def test_digit_in_mid():
    try:
        assert is_valid("AA123A") == False
    except AssertionError:
        print("Test failed with test_digit_in_mid")


if __name__ == "__main__":
    main()
