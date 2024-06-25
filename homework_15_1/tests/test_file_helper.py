from datetime import datetime
import unittest
from pathlib import Path
import shutil

from homework_15_1.file_helper import write_to_file, read_from_file


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.files_dir = './files/'
        self.correct_file_name = 'correct_file.txt'
        self.empty_file_name = 'empty_file.txt'
        self.non_existing_file_name = 'non_existing_file.txt'
        self.bad_data_file_name = 'bad_data_file.txt'

        self.correct_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [
                1,
                2
            ]
        }
        self.bad_data = {'timestamp': datetime.now()}

        Path(self.files_dir).mkdir()

    def test_write_and_read_file(self):
        full_path = self.files_dir + self.correct_file_name
        write_to_file(full_path, self.correct_data)
        self.assertTrue(Path(full_path).exists(), 'File was not created')

        file_content = read_from_file(full_path)
        self.assertEqual(file_content, self.correct_data)

        self.assertIsInstance(
            file_content['pk'],
            int,
            'pk should be an integer'
        )
        self.assertIsInstance(
            file_content['publisher'],
            int,
            'publisher should be an integer'
        )
        self.assertIsInstance(
            file_content['title'],
            str,
            'title should be a string'
        )
        self.assertIsInstance(
            file_content['author'],
            str,
            'author should be a string'
        )
        self.assertIsInstance(
            file_content['price'],
            float,
            'price should be a float'
        )
        self.assertIsInstance(
            file_content['discounted_price'],
            float,
            'discounted_price should be a float'
        )
        self.assertIsInstance(
            file_content['is_bestseller'],
            int,
            'is_bestseller should be a boolean'
        )
        self.assertIsInstance(
            file_content['is_banned'],
            int,
            'is_banned should be a boolean'
        )
        self.assertIsInstance(
            file_content['genres'],
            list,
            'genres should be a list'
        )
        self.assertIsInstance(
            file_content['published_date'],
            str,
            'published_date should be a date-string'
        )
        self.assertTrue(
            is_valid_date(file_content['published_date']),
            'Incorrect date format. Must be YYYY-MM-DD'
        )

    def test_write_and_read_empty_file(self):
        full_path = self.files_dir + self.empty_file_name
        write_to_file(full_path, {})
        self.assertTrue(Path(full_path).exists(), 'File was not created')

        file_content = read_from_file(full_path)
        self.assertEqual(file_content, {})

    def test_read_nonexistent_file(self):
        full_path = self.files_dir + self.non_existing_file_name
        self.assertRaises(FileNotFoundError, read_from_file, full_path)

    def test_write_bad_data_into_file(self):
        full_path = self.files_dir + self.bad_data_file_name
        self.assertRaises(TypeError, write_to_file, full_path, self.bad_data)

    def tearDown(self):
        shutil.rmtree(self.files_dir)

        del self.files_dir
        del self.correct_file_name
        del self.empty_file_name
        del self.non_existing_file_name
        del self.bad_data_file_name
        del self.correct_data
        del self.bad_data
