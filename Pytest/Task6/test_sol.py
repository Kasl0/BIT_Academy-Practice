from solution import is_prime as function
from random import randint
from math import sqrt

def is_prime2(n):
    if n <= 1:
        return False
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

class TestMini:
    def test_A(self):
        for _ in range(6):
            x = randint(-10, 10)
            assert function(x) == is_prime2(x)

class TestMid:
    def test_A(self):
        for _ in range(6):
            x = randint(-1000000, 1000000)
            assert function(x) == is_prime2(x)

class TestMaxi:
    def test_A(self):
        for _ in range(6):
            x = randint(-1000000000000, 1000000000000)
            assert function(x) == is_prime2(x)
