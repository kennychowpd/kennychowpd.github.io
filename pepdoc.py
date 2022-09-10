def meow(n: int) -> str:
    """
    Meow n times. 
    
    :param n: Number of times to meow
    :type n: int
    :raise TypeError when n is not int
    :return: A string of n meows, one per line
    :rtype: str
    :This is a docstring for documentation
    """ 
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
