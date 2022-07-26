from cmplex import C

# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku

class TestMini:
    def test_A(self):
        assert C(0,0).__sub__(C(1,1)) == C(-1,-1)
    def test_B(self):
        assert C(-1,-2).__sub__(C(-3,-4)) == C(2,2)
    def test_C(self):
        assert C(0,0).__sub__(C(0,0)) == C(0,0)

class TestMid:
    def test_A(self):
        assert C(45,67).__sub__(C(-23,98)) == C(68,-31)
    def test_B(self):
        assert C(893,-1933).__sub__(C(0,2999)) == C(893,-4932)

class TestMaxi:
    def test_A(self):
        assert C(91823434,1243344).__sub__(C(541313435,90710973)) == C(-449490001,-89467629)