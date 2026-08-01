import unittest

from evaluate import evaluate


class EvaluateTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate("2+3"), 5.0)

    def test_precedence(self):
        self.assertEqual(evaluate("2+3*4"), 14.0)

    def test_parentheses(self):
        self.assertEqual(evaluate("(2+3)*4"), 20.0)

    def test_division(self):
        self.assertEqual(evaluate("10/4"), 2.5)

    def test_unary_minus(self):
        self.assertEqual(evaluate("-5+2"), -3.0)

    def test_rejects_names(self):
        with self.assertRaises(ValueError):
            evaluate("__import__('os').system('echo hi')")

    def test_empty(self):
        with self.assertRaises(ValueError):
            evaluate("   ")


if __name__ == "__main__":
    unittest.main()
