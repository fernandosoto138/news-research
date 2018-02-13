import unittest

from newsresearch.data_validations import SimpleListValidator


class TestSimpleListValidator(unittest.TestCase):

    def test_includer(self):
        string_list = ["abcd", "  ", "", "qwerty"]
        expected_output = ["abcd", "qwerty"]
        includer = SimpleListValidator("\w", False)
        self.assertEqual(includer.process_list(string_list), expected_output)

if __name__ == '__main__':
    unittest.main()