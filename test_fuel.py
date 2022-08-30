from fuel import convert, gauge
import pytest

def main():
    test_input1()
    test_input2()
    test_low_fuel()
    test_full_tank()
    test_fuel()
    
def test_input1():
    with pytest.raises(ValueError):
        convert("10/1")
    with pytest.raises(ZeroDivisionError):
        convert("10/0")
    

def test_input2():
    try:
        assert convert("1/1") == "100"
        assert convert("4/10") == "40"
    except AssertionError:
        print("test faild with test_input2")    
            
def test_lowfuel():
    try:
        assert gauge(1) == "E"
        assert gauge(0) == "E"
    except AssertionError:
        print("test failed with test_lowfuel") 
        
def test_full_tank():
    try:
        assert gauge(99) == "F"
        assert gauge(100) == "F"
    except AssertionError:
        print("test failed with test_full_tank") 
        
def test_fuel():
    try:
        assert gauge(50) == "51%" 
        assert gauge(33) == "33%"
    except AssertionError:
        print("test failed with test_fuel") 
        

if __name__ == "__main__":
    main()