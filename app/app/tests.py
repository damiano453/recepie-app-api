from django.test import TestCase

from app.calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """ test that 2 numbers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        """ test that 2 vls are substracted and returned """
        self.assertEqual(substract(5, 11), 6)
