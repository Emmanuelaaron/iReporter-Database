import re
class Validating_string:

    @staticmethod
    def is_string(string):
        return type(string) == str
    
    @staticmethod
    def is_space(string):
        return string.isspace()

    @staticmethod
    def characters(string):
        return len(string) > 0

class email_validator:

    @staticmethod
    def validate_email(email_to_be_validated):
        email_validate = re.compile("(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)")
        return email_validate.match(email_to_be_validated)

def No_space(lst):
    for item in lst:
        return(Validating_string.is_space(item) or\
         not Validating_string.characters(item))
