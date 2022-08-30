from calculator import square
import pytest

def main():
    test_square()
    
    
def test_positive():
    for i in range(1, 10):
        assert square(i) == i * i
    
        
def test_negative():
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")
    
    
if __name__ == "__main__":
    main()