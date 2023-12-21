from emoji import emojize


class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        return emojize(":cookie:") * self.size

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Exceeds capacity.")
        elif n < 0:
            raise ValueError("Negative")
        else:
            self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies.")
        elif n < 0:
            raise ValueError("Negative")
        else:
            self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if not capacity >= 0:
            raise ValueError("Invalid jar capacity.")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Invalid jar size.")
        self._size = size


