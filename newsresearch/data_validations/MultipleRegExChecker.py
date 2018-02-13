"""
This module allows you to perform multiple checks on lists of strings
"""
import re

class MultipleRegExChecker(object):
    def __init__(self):
        self.validators = []

    def add_rule(regular_expression, exclude=True):
        """This functions adda regullar expression checker
        if exclude = false will exclude all elements that does not match
        if exclude = true will exclude the element if the expression matches.
        """
        self.validators.append([re.compile(regular_expression), exclude])
    
    def process_list(string_list):
        valid_items = []
        for validator in self.validators:
            for item in string_list:
                check = validator[0].match(item)
                if validator[1] is True:
                    if check is True:
                        continue
                    valid_items.append(item)
                if validator[1] is False:
                    if check is False:
                        continue
                    valid_items.append(True)
                


