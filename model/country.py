import sys
from datetime import datetime
from util.fixed_time_zone_offset import FixedTimeZoneOffset
from util.math_util import MathUtil

class Country:
    def __init__(self, code, name, emoji, languages, currency, timezones, location):
        self.code = code # ISO 2-alpha code e.g. 'ES'
        self.emoji = emoji
        self.name = name # e.g. 'Spain'
        self.languages = languages # array of dicts e.g. [{'code': 'es', 'name': 'Spanish'}]
        self.currency = currency # dict e.g. {'code': 'EUR', 'rate_against_usd': 0.91819}
        self.timezones = timezones # array of strings e.g. ['UTC','UTC+01:00']
        self.location = location # dict e.g. {'lat': 40.0, 'lon': -4.0}

    def print_name_and_emoji(self):
        print('Country: ' + self.name + ' ' + self.emoji)

    def print_code(self):
        print('ISO code: ' + self.code)

    def print_languages(self):
        sys.stdout.write('Languages: ')
        for i in range(0, len(self.languages)):
            sys.stdout.write(self.languages[i]['name'] + ' (' + self.languages[i]['iso639_1'] + ')')
            if i != len(self.languages) - 1:
                sys.stdout.write(', ')
        sys.stdout.write('\n')

    def print_currency(self):
        if self.currency['rate_against_usd'] != None:
            print('Currency: ' + self.currency['code'] + ' (1 ' + self.currency['code'] + ' = ' + str(self.currency['rate_against_usd']) + ' USD)')
        else:
            print('Currency: ' + self.currency['code'] + ' (no rate data available)')

    def print_time(self):
        sys.stdout.write('Time: ')
        now = datetime.now(tz=FixedTimeZoneOffset())
        for i in range (0, len(self.timezones)):
            # UTC-06:00, UTC+05:00
            # 012345678
            timezone = self.timezones[i]
            offset = 0
            if timezone != 'UTC':
                is_minus = timezone[3] == '-'
                hours = int(timezone[4:6])
                minutes = int(timezone[7:9])
                offset = hours * 60 + minutes
                if is_minus:
                    offset = -offset;
            now = now.astimezone(tz=FixedTimeZoneOffset(offset=offset))
            sys.stdout.write(now.strftime('%H:%M:%S') + ' (' + timezone + ')')
            if i != len(self.timezones) - 1:
                sys.stdout.write(', ')
        sys.stdout.write('\n')

    def print_distance(self, lat, lon):
        country_lat = self.location['lat']
        country_lon = self.location['lon']
        distance = MathUtil.get_distance_from_latlon_in_km(lat1=lat, lon1=lon, lat2=country_lat, lon2=country_lon)
        print('Estimated distance: ' + str(int(distance)) + ' km')
