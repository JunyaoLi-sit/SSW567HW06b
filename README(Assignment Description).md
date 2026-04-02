Assignment Description:
The objective of this assignment is for you to
(a) develop a set of test-cases for an existing triangle classification program,
(b) use those test-cases to find and fix defects in that program, and
(c) report on your testing results for the Triangle problem.

Author: Junyao Li

Summary:
In this assignment, I developed a set of unit test cases for the classifyTriangle() function in Triangle.py. I first ran the tests against the original buggy implementation to identify defects in the triangle classification logic. After analyzing the failed test cases, I updated the function to fix the defects and reran the full test set.

The initial version failed some test cases related to invalid triangle detection and/or triangle type classification. After fixing the logic in Triangle.py, the improved version passed all of the test cases. This shows that the updated implementation correctly handles valid triangles, invalid triangles, and important edge cases.

Reflection:
This assignment helped me understand the importance of designing complete test cases instead of only checking common inputs. I learned that edge cases such as zero, negative values, and triangle inequality violations are very important for finding defects. I also learned that testing should be done before fixing the code so that the test results can clearly show what was wrong in the original implementation.

Honor Pledge:
I pledge my honor that I have abided by the Stevens Honor System.
