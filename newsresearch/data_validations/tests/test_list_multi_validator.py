import unittest
from newsresearch.data_validations import RegexExclude
from newsresearch.data_validations import RegexInclude
from newsresearch.data_validations import ListMultiValidator


class TestListMultiValidator(unittest.TestCase):

    def test_process_list(self):
        string_list = ["abcd", "  ", "", "qwerty"]
        expected_output = ["abcd"]
        validator = ListMultiValidator()
        valid1 = RegexInclude("\w")
        valid2 = RegexExclude("qwer")
        validator.add_rule(valid1)
        validator.add_rule(valid2)
        self.assertEqual(validator.process_list(string_list), expected_output)
    

if __name__ == '__main__':
    unittest.main()