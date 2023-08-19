import unittest
from home_work.home_work_14.program.triangle import Triangle, TriangleException


class TestClassTriangle(unittest.TestCase):


    def test_method(self):
        self.assertEqual(Triangle(6, 7, 3), Triangle(6, 7, 3))


if __name__ == '__main__':
    unittest.main()
