import unittest
from newsresearch.data_validations import RegexExclude


class TestRegexExcluder(unittest.TestCase):

    def test_process_list(self):
        string_list = ["abcd", "  ", "", "qwerty"]
        expected_output = ["abcd", "  ", ""]
        validator = RegexExclude("qwe")
        self.assertEqual(validator.process_list(string_list), expected_output)    

if __name__ == '__main__':
    unittest.main()