from typing import Optional, Tuple


class Rectangle:
    def __init__(self, x: float, y: float, w: float, h: float):
        if w < 0 or h < 0:
            raise ValueError("Width and height must be non-negative")
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_coordinates(self) -> Tuple[float, float, float, float]:
        """Возвращает координаты углов прямоугольника (x1, y1, x2, y2)"""
        return (self.x, self.y, self.x + self.w, self.y + self.h)


def calculate_intersection(
    rect_b: Rectangle,
) -> Optional[Tuple[float, float, float, float]]:
    """
    Вычисляет пересечение заданного прямоугольника A (0, 0, 1000, 500)
    с произвольным прямоугольником B.
    Возвращает координаты (x, y, w, h) пересечения или None,
    если пересечения нет.
    """
    # Заданный прямоугольник A
    rect_a = Rectangle(0, 0, 1000, 500)

    # Получаем координаты углов
    a_x1, a_y1, a_x2, a_y2 = rect_a.get_coordinates()
    b_x1, b_y1, b_x2, b_y2 = rect_b.get_coordinates()

    # Находим пересечение
    x1 = max(a_x1, b_x1)
    y1 = max(a_y1, b_y1)
    x2 = min(a_x2, b_x2)
    y2 = min(a_y2, b_y2)

    # Проверяем наличие пересечения
    if x1 >= x2 or y1 >= y2:
        return None

    return (x1, y1, x2 - x1, y2 - y1)
