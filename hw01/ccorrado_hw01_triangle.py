"""
HW01: Triangle Classification
Author: Chris Corrado
Date: 8/29/2018

Modified for HW05: 9/29/2018
"""


class Triangle(object):
    """
    The Triangle object class represents a single triangle in memory.
    @:param a: Side 1
    @:param b: Side 2
    @:param c: Side 3
    """
    __slots__ = "a", "b", "c"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_valid(self) -> bool:
        """
        Method to check to see if the triangle is a valid one.
        :return: True if the triangle is valid
        """
        return self._is_ints() and self._is_positive() and self._is_triangle()

    def _is_triangle(self) -> bool:
        """
        The sum of two sides must be strictly greater than the third side.
        :return: True if the triangle is a triangle
        """
        return ((self.b + self.c) > self.a) or ((self.a + self.c) > self.b) or ((self.a + self.b) > self.c)

    def _is_positive(self) -> bool:
        return self.a > 0 and self.b > 0 and self.c > 0

    def _is_ints(self) -> bool:
        return isinstance(self.a, int) and isinstance(self.b, int) and isinstance(self.c, int)

    def is_right(self) -> bool:
        return self.is_valid() and self.a ^ 2 + self.b ^ 2 == self.c ^ 2

    def is_equilateral(self) -> bool:
        return self.is_valid() and self.a == self.b == self.c

    def is_isosceles(self) -> bool:
        return self.is_valid() and (not self.is_equilateral()) and (
                self.a == self.b or self.a == self.c or self.b == self.c)

    def is_scalene(self) -> bool:
        return self.is_valid() and self.a != self.b != self.c

    def __str__(self):
        text_to_print = []
        if not self.is_valid():
            text_to_print = "Invalid"
        else:
            if self.is_right():
                text_to_print.append("Right")
            if self.is_equilateral():
                text_to_print.append("Equilateral Triangle")
            elif self.is_isosceles():
                text_to_print.append("Isosceles Triangle")
            elif self.is_scalene():
                text_to_print.append("Scalene Triangle")

        return str(text_to_print)


def classify_triangle(a, b, c) -> Triangle:
    print("Classification: " + str(Triangle(a, b, c)))
    return Triangle(a, b, c)
