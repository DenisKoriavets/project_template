import unittest
import os
from unittest.mock import patch
from app.io.input import input_from_console, read_from_file, read_from_file_pandas


class TestInput(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_sample.txt"
        self.empty_file = "test_empty.txt"
        self.content = "line1\nline2\nline3"

        with open(self.test_file, "w", encoding="utf-8") as f:
            f.write(self.content)

        with open(self.empty_file, "w", encoding="utf-8") as f:
            pass

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.empty_file):
            os.remove(self.empty_file)

    @patch('builtins.input', return_value='test text')
    def test_input_from_console(self, mock_input):
        self.assertEqual(input_from_console(), 'test text')

    def test_read_from_file_success(self):
        self.assertEqual(read_from_file(self.test_file), self.content)

    def test_read_from_file_empty(self):
        self.assertEqual(read_from_file(self.empty_file), "")

    def test_read_from_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file("non_existent.txt")

    def test_read_from_file_pandas_success(self):
        result = read_from_file_pandas(self.test_file)
        self.assertEqual(result, self.content)

    def test_read_from_file_pandas_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file_pandas("non_existent.txt")

    def test_read_from_file_pandas_multiline(self):
        result = read_from_file_pandas(self.test_file)
        self.assertTrue("\n" in result)
        self.assertEqual(len(result.split("\n")), 3)


if __name__ == '__main__':
    unittest.main()