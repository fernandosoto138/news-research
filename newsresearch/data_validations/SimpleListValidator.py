"""
This is a simple regullar expression checker. 

Allows to decide if you needs to include or exclude a string according a
regular expression.

Excluders removes a string if the pattern matches
Includers keep a string if the pattern matches

"""
import re


class SimpleListValidator(object):
    validator = None
    is_excluder = True

    def __init__(self, expression, excluder=True):
        self.validator = re.compile(expression)
        self.is_excluder = excluder

    def process_list(self, string_list):
        valid_list = []
        for string in string_list:
            match = self.validator.match(string)
            if self.is_excluder:
                if match:
                    continue
                valid_list.append(string)
            else:
                if match:
                    valid_list.append(string)
                continue
        return valid_list
