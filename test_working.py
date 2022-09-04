from re_working import search
import pytest

def main():
    test_1()
    test_2()

    
def test_1():
    assert search("9 AM to 5 PM") == "09:00 to 17:00"
    assert search("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert search("10 PM to 8 AM") == "22:00 to 08:00"
    assert search("10:30 PM to 8:50 AM") == "22:30 to 08:50"
    
def test_2():
    with pytest.raises(ValueError):
        search("9:60 AM to 5:60 PM")
    with pytest.raises(ValueError):
        search("9 AM - 5 PM")
    with pytest.raises(ValueError):
        search("09:00 AM to 17:00 PM")
        
        
if __name__ == "__main__":
    main()
