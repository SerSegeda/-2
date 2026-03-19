import unittest
from lab2main import *
class TestNavivorit(unittest.TestCase):

    def test_normal_behavior(self):
        app = Navivorit("Один два три. 1 лабораторна краща за 2.")
        expected_result = "три два Один. 2 лабораторна краща за 1."
        self.assertEqual(app.diya(), expected_result)

    def test_single_word_sentence(self):
        app = Navivorit("Слово.")
        expected_result = "Слово."
        self.assertEqual(app.diya(), expected_result)

    def test_missing_dot(self):
        app = Navivorit("Речення без крапки")
        expected_result = "введіть повноцінне речення"
        self.assertEqual(app.diya(), expected_result)

    def test_wrong_data_type(self):
        app = Navivorit(12345)
        expected_result = "введіть повноцінне речення"
        self.assertEqual(app.diya(), expected_result)