from bank import value


def main():
    test_hello()
    test_h()
    test_other()
    
    
def test_hello():
    try:
        assert value("hello") == "$0"
    except AssertionError:
        print("Test failed for the phrase \"hello\"")

        
def test_h():
    try:
        assert value("h") == "$20"
    except AssertionError:
        print("Test failed for the phrase \"h\"")

        
def test_other():
    try:
        assert value("sup") == "$100"
    except AssertionError:
        print("Test failed for the phrase \"sup\"")
        
    
if __name__ == "__main__":
    main()
