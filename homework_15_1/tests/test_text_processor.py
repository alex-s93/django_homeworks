import re
import unittest

from homework_15_1.text_processor import TextProcessor


def is_only_letters_and_spaces(string):
    return bool(re.match(r'^[A-Za-z\s]+$', string))


class TestCleanTextFunc(unittest.TestCase):
    def test_clean_text_method(self):
        test_cases = [
            "Hello, World!",
            "123 ABC!!!"
        ]

        for text in test_cases:
            with self.subTest(text=text):
                processor = TextProcessor(text)
                processor.clean_text()

                # Проверить, что метод правильно удаляет небуквенные символы.
                self.assertTrue(is_only_letters_and_spaces(text))
                # Проверить, что текст приводится к нижнему регистру.
                self.assertTrue(text.islower())

        # проверка на пустую строку
        processor = TextProcessor("")
        processor.clean_text()
        self.assertFalse(processor.cleaned_text)

    def test_remove_stop_words(self):
        test_cases = [
            ("this is a test", ["this", 'is'], "a test"),
            ("some another text", ["this", 'is'], "some another text"),
            ("hello world", [], "hello world")
        ]

        for origin_text, stop_words, result in test_cases:
            with self.subTest(text=origin_text):
                processor = TextProcessor(origin_text)
                processor.remove_stop_words(stop_words)
                self.assertEqual(processor.cleaned_text, result)
