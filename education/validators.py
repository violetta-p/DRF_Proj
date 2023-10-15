import re

from rest_framework.exceptions import ValidationError


class URLValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        url_pattern = r'https?://\S+|www\.\S+'
        youtube_pattern = r'(?:https?://)?(?:www\.)?youtube\.com'

        links = re.findall(url_pattern, val)
        for link in links:
            if not bool(re.match(youtube_pattern, link)):
                raise ValidationError('Only YouTube links are allowed!')

