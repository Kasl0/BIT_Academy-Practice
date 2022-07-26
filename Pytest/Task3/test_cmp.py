from cmplex import C

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

class TestMini:
    def test_A(self):
        assert C(0,0).__eq__(C(1,1)) == False
    def test_B(self):
        assert C(-1,-2).__eq__(C(-3,-4)) == False
    def test_C(self):
        assert C(0,0).__eq__(C(0,0)) == True

class TestMid:
    def test_A(self):
        assert C(45,67).__eq__(C(-23,98)) == False
    def test_B(self):
        assert C(893,-1933).__eq__(C(893,-1933)) == True

class TestMaxi:
    def test_A(self):
        assert C(91823434,1243344).__eq__(C(91823434,1243344)) == True