from datetime import tzinfo, timedelta
# Taken from https://docs.python.org/2.7/library/datetime.html
# A class building tzinfo objects for fixed-offset time zones.
# Note that FixedOffset(0, "UTC") is a different way to build a
# UTC tzinfo object.
class FixedTimeZoneOffset(tzinfo):
    """Fixed offset in minutes east from UTC."""

    def __init__(self, offset=0, name='UTC'):
        self.__offset = timedelta(minutes = offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return timedelta(0)
