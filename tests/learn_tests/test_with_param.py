# Функция из проекта
import pytest


def sum(a, b):
    return a + b


# Тест который проверяет это , параметризированый
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 1, 3),
    (23, 5, 28)
])
def test_sum(a, b, expected):
    assert sum(a, b) == expected
