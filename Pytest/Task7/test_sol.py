import pytest
from solution import sort as function
from random import randint

class Node:
    def __init__(self, v=-1):
        self.val = v
        self.next = None

def stworz(n, a, b):
    head = Node()
    f = head
    for _ in range(n):
        f.next = Node(randint(a, b))
        f = f.next
    return head

def pytest_check(ll):
    ll = ll.next
    while ll.next != None:
        if ll.val > ll.next.val:
            pytest.fail()
        ll = ll.next


class TestMini:
    def test_A(self):
        l1 = stworz(8, 1, 100)
        function(l1)
        pytest_check(l1)
    def test_B(self):
        l1 = stworz(80, -100, 100)
        function(l1)
        pytest_check(l1)
    def test_C(self):
        l1 = stworz(30, 10, 1000)
        function(l1)
        pytest_check(l1)

class TestMid:
    def test_A(self):
        l1 = stworz(50, -100000, 100000)
        function(l1)
        pytest_check(l1)
    def test_B(self):
        l1 = stworz(500, 1, 100000)
        function(l1)
        pytest_check(l1)
    def test_C(self):
        l1 = stworz(100, -100000, -100)
        function(l1)
        pytest_check(l1)

class TestMax:
    def test_A(self):
        l1 = stworz(1000, 2839474, 9848288)
        function(l1)
        pytest_check(l1)
    def test_B(self):
        l1 = stworz(100, -10000000000, 1000000000)
        function(l1)
        pytest_check(l1)
    def test_C(self):
        l1 = stworz(10000, 1, 10000000)
        function(l1)
        pytest_check(l1)