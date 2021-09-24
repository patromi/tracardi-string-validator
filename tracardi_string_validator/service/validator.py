import re

from tracardi_string_validator.model.configuration import Configuration


class Validator:
    def __init__(self, config: Configuration):
        self.config = config

    def _get_regex(self):
        """Get a actual regex with dict from validation_type."""
        dict_regex = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_:#]+\.([a-zA-Z]){2,'
                   r'6}([a-zA-Z0-9\.\&\/\?\:@\-_:#])*',
            'ipv4': r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
            'date': r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))("
                    r"?:(?:1[ "
                    r"6-9]|["
                    r"2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579]["
                    r"26])|(?:("r"?:16|["
                    r"2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4("
                    r"?:(?:1["
                    r"6-9]|["
                    r"2-9]\d)?\d{2})$",
            'time': r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9](:?)([0-5]?[0-9]?)$',
            'int': r'^[0-9]+$',
            'float': r'^[+-]?([0-9]{1,})[.,]([0-9]{1,})$',
            'number_phone': r'\(?\+[0-9]{1,3}\)? ?-?[0-9]{1,3} ?-?[0-9]{3,5} ?-?[0-9]{4}( ?-?[0-9]{3})? ?(\w{1,'
                            r'10}\s?\d{1,6})?'}
        return dict_regex[self.config.validation_name]

    def check(self) -> bool:
        """Check the validation"""
        if re.match(self._get_regex(), self.config.data):
            return True
        else:
            return False