"""
TestTriangle.py
Junyao Li 
Unit tests for Triangle.py
"""

import unittest
from Triangle import classifyTriangle


class TestTriangle(unittest.TestCase):
    """Tests for classifyTriangle()."""

    # ---------- Equilateral ----------
    def test_equilateral_small(self):
        """All three sides equal should be Equilateral."""
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")

    def test_equilateral_larger(self):
        """Another equilateral triangle case."""
        self.assertEqual(classifyTriangle(10, 10, 10), "Equilateral")

    # ---------- Isosceles ----------
    def test_isosceles_first_two_equal(self):
        """First two equal sides should be Isosceles."""
        self.assertEqual(classifyTriangle(5, 5, 3), "Isosceles")

    def test_isosceles_first_and_third_equal(self):
        """First and third equal sides should be Isosceles."""
        self.assertEqual(classifyTriangle(5, 3, 5), "Isosceles")

    def test_isosceles_last_two_equal(self):
        """Last two equal sides should be Isosceles."""
        self.assertEqual(classifyTriangle(3, 5, 5), "Isosceles")

    # ---------- Scalene ----------
    def test_scalene_valid(self):
        """Three different valid sides should be Scalene."""
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_scalene_another_valid(self):
        """Another scalene triangle case."""
        self.assertEqual(classifyTriangle(7, 8, 9), "Scalene")

    # ---------- Invalid: zero ----------
    def test_zero_first_side(self):
        """Zero side length is invalid."""
        self.assertEqual(classifyTriangle(0, 4, 5), "NotATriangle")

    def test_zero_second_side(self):
        """Zero side length is invalid."""
        self.assertEqual(classifyTriangle(4, 0, 5), "NotATriangle")

    def test_zero_third_side(self):
        """Zero side length is invalid."""
        self.assertEqual(classifyTriangle(4, 5, 0), "NotATriangle")

    # ---------- Invalid: negative ----------
    def test_negative_first_side(self):
        """Negative side length is invalid."""
        self.assertEqual(classifyTriangle(-1, 4, 5), "NotATriangle")

    def test_negative_second_side(self):
        """Negative side length is invalid."""
        self.assertEqual(classifyTriangle(4, -1, 5), "NotATriangle")

    def test_negative_third_side(self):
        """Negative side length is invalid."""
        self.assertEqual(classifyTriangle(4, 5, -1), "NotATriangle")

    # ---------- Invalid: triangle inequality ----------
    def test_triangle_inequality_equal_case(self):
        """If two sides add exactly to the third, it is not a triangle."""
        self.assertEqual(classifyTriangle(1, 2, 3), "NotATriangle")

    def test_triangle_inequality_violation_1(self):
        """Triangle inequality violation should be invalid."""
        self.assertEqual(classifyTriangle(1, 2, 10), "NotATriangle")

    def test_triangle_inequality_violation_2(self):
        """Triangle inequality violation in another order should be invalid."""
        self.assertEqual(classifyTriangle(10, 1, 2), "NotATriangle")

    def test_triangle_inequality_violation_3(self):
        """Triangle inequality violation in another order should be invalid."""
        self.assertEqual(classifyTriangle(2, 10, 1), "NotATriangle")

    # ---------- Boundary / edge valid ----------
    def test_boundary_valid_isosceles(self):
        """A near-boundary valid case should still be classified correctly."""
        self.assertEqual(classifyTriangle(2, 2, 3), "Isosceles")

    def test_boundary_valid_scalene(self):
        """A near-boundary valid scalene case should be valid."""
        self.assertEqual(classifyTriangle(2, 3, 4), "Scalene")

    # ---------- Non-integer input ----------
    def test_float_input(self):
        """Float input should be rejected."""
        self.assertEqual(classifyTriangle(3.5, 3.5, 3.5), "NotATriangle")

    def test_string_input(self):
        """String input should be rejected."""
        self.assertEqual(classifyTriangle("3", 3, 3), "NotATriangle")

    def test_mixed_invalid_type(self):
        """Mixed invalid type input should be rejected."""
        self.assertEqual(classifyTriangle(3, None, 3), "NotATriangle")


if __name__ == "__main__":
    unittest.main()