import pytest
import solution
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

class TestMini:
    def test_A(self):
        l1 = stworz(8, 1, 100)
        solution.merge_sort(l1)
        l1 = l1.next
        while l1.next != None:
            if l1.val > l1.next.val:
                pytest.fail()
            l1 = l1.next

class TestMid:
    def test_A(self):
        l1 = stworz(50, -100000, 100000)
        solution.merge_sort(l1)
        l1 = l1.next
        while l1.next != None:
            if l1.val > l1.next.val:
                pytest.fail()
            l1 = l1.next

class TestMax:
    def test_A(self):
        l1 = stworz(10000, -10000000, 10000000)
        solution.merge_sort(l1)
        l1 = l1.next
        while l1.next != None:
            if l1.val > l1.next.val:
                pytest.fail()
            l1 = l1.next