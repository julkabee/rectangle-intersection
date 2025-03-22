import pytest

from src.geometry import Rectangle, calculate_intersection


@pytest.fixture
def fixed_rectangle():
    """Фикстура для создания фиксированного прямоугольника A"""
    return Rectangle(0, 0, 1000, 500)


def test_full_overlap():
    """Тест полного пересечения (B внутри A)"""
    rect_b = Rectangle(100, 100, 200, 200)
    result = calculate_intersection(rect_b)
    assert result == (100, 100, 200, 200)


def test_partial_overlap():
    """Тест частичного пересечения"""
    rect_b = Rectangle(800, 400, 300, 200)
    result = calculate_intersection(rect_b)
    assert result == (800, 400, 200, 100)


def test_no_intersection_right():
    """Тест отсутствия пересечения (B справа от A)"""
    rect_b = Rectangle(1001, 0, 100, 100)
    result = calculate_intersection(rect_b)
    assert result is None


def test_no_intersection_above():
    """Тест отсутствия пересечения (B сверху от A)"""
    rect_b = Rectangle(0, 501, 100, 100)
    result = calculate_intersection(rect_b)
    assert result is None


def test_no_intersection_left():
    """Тест отсутствия пересечения (B слева от A)"""
    rect_b = Rectangle(-200, 0, 100, 100)
    result = calculate_intersection(rect_b)
    assert result is None


def test_no_intersection_below():
    """Тест отсутствия пересечения (B снизу от A)"""
    rect_b = Rectangle(0, -200, 100, 100)
    result = calculate_intersection(rect_b)
    assert result is None


def test_edge_case_touching():
    """Тест касания границ (не считается пересечением)"""
    rect_b = Rectangle(1000, 0, 100, 100)
    result = calculate_intersection(rect_b)
    assert result is None


def test_negative_dimensions():
    """Тест с отрицательными размерами"""
    with pytest.raises(ValueError, match="Width and height must be non-negative"):
        Rectangle(100, 100, -50, -50)