from calculator import square
    

def main():
    test_square()
    
    
def test_positive():
    assert square(2) == 4
    assert square(11) == 121
    
        
def test_negative():
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0
    
    
    
if __name__ == "__main__":
    main()