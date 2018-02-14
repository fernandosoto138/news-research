from newsresearch.data_validations import GenericStringValidator


class ListMultiValidator(object):
    validators = []

    def add_rule(self, validator):
        if isinstance(validator, GenericStringValidator):
            self.validators.append(validator)
        else:
            raise AttributeError("Validator must be a subclass of \
                                  GenericStringValidator")
    
    def process_list(self, string_list):
        valid_list = string_list
        if self.validators == []:
            raise Exception("You must register at least one validator")
        for validator in self.validators:
            valid_list = validator.process_list(valid_list)
        return valid_list
