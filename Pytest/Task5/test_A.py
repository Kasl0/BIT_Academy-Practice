import pytest
from function import count_chars

# Napisać testy dla funkcji count_chars za pomocą
# markera "parametrize"

# Funkcja count_chars zwraca trzyelementową tablicę
# która zawiera odpowiednio liczbę wystąpień znaku 'a', 'b' i 'c'

@pytest.mark.parametrize("test_input, expected",
[("abc", [1,1,1]), ("aaa", [3,0,0]), ("xyz", [0,0,0]), ("abccabcbabca", [4,4,4]), ("bbbbbbb", [0,7,0]), ("xytmunbz", [0,1,0])])

def test(test_input, expected):
    assert count_chars(test_input) == expected