import sys
import pytest
from numb3rs import validate

def main():
    test_num()
    test_nondigit()
    


def test_num():
    assert validate("32.0.255.67") == True
    assert validate("323.1.3.4") == False
    
def test_nondigit():
    assert validate("a.d.f.g") == False
    assert validate("") == False
    assert validate("fsadfdafda") == False
    
        
if __name__ == "__main__":
    main()
         
         