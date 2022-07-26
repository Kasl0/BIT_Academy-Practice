import pytest
from function import square

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

class MyTestCase():
    skip_all = False

class TestMini:
    def test_A(self):
        assert square(-9) == 81
    def test_B(self):
        assert square(-2) == 4
    def test_C(self):
        assert square(0) == 0
    def test_D(self):
        assert square(5) == 25
            
@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 1")

class TestMid:
    def test_A(self):
        assert square(-90) == 8100
    def test_B(self):
        assert square(-221) == 48841
    def test_C(self):
        assert square(345) == 119025
    def test_D(self):
        assert square(999) == 998001

@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 2")

class TestMaxi:
    def test_A(self):
        assert square(20000) == 400000000
    def test_B(self):
        assert square(543221) == 295089054841
    def test_C(self):
        assert square(843445) == 711399468025
    def test_D(self):
        assert square(953400) == 908971560000
            
MyTestCase.skip_all = True
@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 3")

class TestSuperMaxi:
    def test_A(self):
        assert square(2053540007654) == 2053540007654 * 2053540007654
    def test_B(self):
        assert square(5437978988221) == 5437978988221 * 5437978988221
    def test_C(self):
        assert square(8434278655545) == 8434278655545 * 8434278655545
    def test_D(self):
        assert square(9537864036570) == 9537864036570 * 9537864036570