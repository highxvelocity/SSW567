import unittest

from hw01.ccorrado_hw01_triangle import classify_triangle


class TriangleTests(unittest.TestCase):
    def test_right_triangle(self):
        triangle = classify_triangle(1, 2, 5)
        self.assertTrue(triangle.is_right(), "Triangle is Right")
        self.assertTrue(triangle.is_scalene(), "Triangle is Scalene")
        self.assertFalse(triangle.is_equilateral(), "Triangle is NOT Equilateral")
        self.assertFalse(triangle.is_isosceles(), "Triangle is NOT Isosceles")

    def test_isosceles_triangle(self):
        triangle = classify_triangle(1, 1, 5)
        self.assertTrue(triangle.is_isosceles(), "Triangle is Isosceles")
        self.assertFalse(triangle.is_scalene(), "Triangle is NOT Scalene")
        self.assertFalse(triangle.is_equilateral(), "Triangle is NOT Equilateral")
        self.assertFalse(triangle.is_right(), "Triangle is NOT Right")

    def test_scalene_triangle(self):
        triangle = classify_triangle(1, 9, 5)
        self.assertTrue(triangle.is_scalene(), "Triangle is Scalene")
        self.assertFalse(triangle.is_equilateral(), "Triangle is NOT Equilateral")
        self.assertFalse(triangle.is_right(), "Triangle is NOT Right")
        self.assertFalse(triangle.is_isosceles(), "Triangle is NOT Isosceles")

    def test_equilateral_triangle(self):
        triangle = classify_triangle(3, 3, 3)
        self.assertTrue(triangle.is_equilateral(), "Triangle is Equilateral")
        self.assertFalse(triangle.is_scalene(), "Triangle is NOT Scalene")
        self.assertFalse(triangle.is_right(), "Triangle is NOT Right")
        self.assertFalse(triangle.is_isosceles(), "Triangle is NOT Isosceles")

    def test_not_a_triangle(self):
        triangle = classify_triangle(0, 0, 0)
        self.assertEqual(str(triangle), "Invalid")

    def test_neg_triangle(self):
        triangle = classify_triangle(-1, 1, 1)
        self.assertEqual(str(triangle), "Invalid")

    def test_neg_triangle_2(self):
        triangle = classify_triangle(1, -2, 1)
        self.assertEqual(str(triangle), "Invalid")

    def test_neg_triangle_3(self):
        triangle = classify_triangle(1, 1, -1)
        self.assertEqual(str(triangle), "Invalid")

    def test_str_triangle(self):
        triangle = classify_triangle("not", "a", "triangle")
        self.assertEqual(str(triangle), "Invalid")


if __name__ == "__main__":
    unittest.main()
