"""
This module allows you to perform multiple checks on lists of strings
"""
from .SimpleListValidator import *


class MultipleListValidator(object):
    def __init__(self):
        self.validators = []

    def add_rule(self, regular_expression, exclude=True):
        """This functions add regullar expression checker
        if exclude = false will exclude all elements that does not match
        if exclude = true will exclude the element if the expression matches.
        """
        self.validators.append(SimpleListValidator(regular_expression, exclude))
    
    def process_list(self, string_list):
        valid_items = string_list
        if self.validators == []:
            raise Exception("You should register at least one Checker, \
                             see add_rule() ")
        for validator in self.validators:
            valid_items = validator.process_list(valid_items)
        return valid_items
                


