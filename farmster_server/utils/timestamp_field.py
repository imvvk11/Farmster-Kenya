import math
from datetime import datetime

import pytz
from rest_framework import serializers


class TimestampField(serializers.DateTimeField):
    """
    Convert a django datetime to/from timestamp.
    """

    def to_representation(self, value):
        """
        Convert the field to its internal representation (aka timestamp)
        :param value: the DateTime value
        :return: a UTC timestamp integer
        """
        return math.floor(value.timestamp() * 1000)

    def to_internal_value(self, value):
        """
        deserialize a timestamp to a DateTime value
        :param value: the timestamp value
        :return: a django DateTime value
        """
        # converted = datetime.fromtimestamp(float('%s' % value))
        date = datetime.fromtimestamp(float('%s' % value) / 1000)
        return pytz.UTC.localize(date)
