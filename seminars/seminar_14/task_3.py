import unittest
from task_1 import string_cleaner


class TestRemoval(unittest.TestCase):

    def test_ret_same(self):
        self.assertEqual(string_cleaner('language'), 'language')

    def test_lower(self):
        self.assertEqual(string_cleaner('La$ngu$agE'), 'language')

    def test_punt(self):
        self.assertEqual(string_cleaner('l,an.gu:a!g?e'), 'language')

    def test_non_rus(self):
        self.assertEqual(string_cleaner('lф$an$gu$age'), 'language')

    def test_non_all(self):
        self.assertEqual(string_cleaner('Lфв,an.gu:a!g?E'), 'language')


if __name__ == '__main__':
    unittest.main(verbosity=2)
