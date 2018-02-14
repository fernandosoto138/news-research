import unittest
from newsresearch.data_validations import RegexInclude


class TestRegexIncluder(unittest.TestCase):

    def test_process_list(self):
        string_list = ["abcd", "  ", "", "qwerty"]
        expected_output = ["abcd", "qwerty"]
        validator = RegexInclude("\w")
        self.assertEqual(validator.process_list(string_list), expected_output)
        

if __name__ == '__main__':
    unittest.main()