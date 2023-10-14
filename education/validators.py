import re

from rest_framework.exceptions import ValidationError


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        url_str = re.match(r'https://www.youtube.com', val)
        if not bool(url_str):
            raise ValidationError('Only YouTube links are allowed!')

