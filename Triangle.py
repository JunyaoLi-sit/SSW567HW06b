"""
Triangle.py

Classify a triangle based on the lengths of its three sides.
"""

def classifyTriangle(a, b, c):
    """
    Return the triangle type as a string.

    Possible results:
    - "Equilateral"
    - "Isosceles"
    - "Scalene"
    - "NotATriangle"
    """

    # Input validation
    if not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int):
        return "NotATriangle"

    if a <= 0 or b <= 0 or c <= 0:
        return "NotATriangle"

    # Triangle inequality check
    if a + b <= c or a + c <= b or b + c <= a:
        return "NotATriangle"

    # Classification
    if a == b == c:
        return "Equilateral"

    if a == b or a == c or b == c:
        return "Isosceles"

    return "Scalene"