from .generic_string_validator import GenericStringValidator
import re


class RegexInclude(GenericStringValidator):

    def __init__(self, expression, excluder=True):
        self.validator = re.compile(expression)

    def check_string(self, string):
        match = self.validator.match(string)
        if match:
            return True
        return False

    def process_list(self, string_list):
        valid_list = []
        for string in string_list:
            if self.check_string(string):
                valid_list.append(string)
        return valid_list
