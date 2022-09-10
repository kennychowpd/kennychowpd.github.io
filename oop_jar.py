class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0
        
    def __str__(self):
        cookies = ""
        for _ in range(self._size):
            cookies += "🍪"
        return cookies

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            self.size -= n
            raise ValueError

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            self._size += n
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    



def main():
    jar = Jar()
    jar
    print(jar)


if __name__ == "__main__":
    main()