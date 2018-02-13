import unittest
from newsresearch.data_validations import MultipleListValidator


class TestMultipleListValidator(unittest.TestCase):

    def test_multi_rule_checking(self):
        string_list = ["abcd", "  ", "", "qwerty"]
        expected_output = ["abcd"]
        validator = MultipleListValidator()
        validator.add_rule("\w", False)
        validator.add_rule("qwer")
        self.assertEqual(validator.process_list(string_list), expected_output)
        

if __name__ == '__main__':
    unittest.main()