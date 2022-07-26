from solution import function
from random import randint

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def function2(start, n):
    if is_prime(n) == False:
        return False
    n -= 1
    while start < n:
        if is_prime(n):
            return False
        n -= 1
    return True


class TestMini:
    def test_A(self):
        for _ in range(10):
            x = randint(-10, 10)
            assert function2(x, function(x)) == True
    def test_B(self):
        for _ in range(10):
            x = randint(30, 100)
            assert function2(x, function(x)) == True
    def test_C(self):
        for _ in range(10):
            x = randint(-100, -25)
            assert function2(x, function(x)) == True

class TestMid:
    def test_A(self):
        for _ in range(10):
            x = randint(-1000, 1000)
            assert function2(x, function(x)) == True
    def test_B(self):
        for _ in range(10):
            x = randint(-10000, 1)
            assert function2(x, function(x)) == True
    def test_C(self):
        for _ in range(10):
            x = randint(-10, 900)
            assert function2(x, function(x)) == True

class TestMaxi:
    def test_A(self):
        for _ in range(10):
            x = randint(10, 1000000)
            assert function2(x, function(x)) == True
    def test_B(self):
        for _ in range(10):
            x = randint(-100000, 0)
            assert function2(x, function(x)) == True
    def test_C(self):
        for _ in range(10):
            x = randint(100000, 1000000)
            assert function2(x, function(x)) == True