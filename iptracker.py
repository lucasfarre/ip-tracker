# Python IP Tracker
# by Lucas Andres Farre

import urllib2, json, sys, math
from datetime import tzinfo, timedelta, datetime

# A class building tzinfo objects for fixed-offset time zones.
# Note that FixedOffset(0, "UTC") is a different way to build a
# UTC tzinfo object.
class FixedOffset(tzinfo):
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

ip = raw_input('Type the IP address to trace: ')

# Get country code from ip2country API.
ip2country_api_url = 'https://api.ip2country.info/'
ip2country_api_url += 'ip?' + ip
response = urllib2.urlopen(ip2country_api_url)
ip_info = json.loads(response.read())
country_code = ip_info['countryCode']

# Get country info from REST Countries API.
countries_api_url = 'https://restcountries.eu/rest/v2/alpha/'
country_fields = 'fields=name;languages;timezones;latlng;currencies'
countries_api_url += country_code + '?' + country_fields
response = urllib2.urlopen(countries_api_url)
country_info = json.loads(response.read())

# Get currency rates for the given country
currency_rates_api_url = 'http://api.fixer.io/latest'
currency_code = country_info['currencies'][0]['code']
currency_rates_api_url += '?base=USD&symbols=' + currency_code
response = urllib2.urlopen(currency_rates_api_url)
currency_rates = json.loads(response.read())['rates']
currency_rate = 0
if currency_code in currency_rates:
    currency_rate = currency_rates[currency_code]

# Show info
print('IP: ' + ip)
print('Country: ' + country_info['name'])
print('ISO code: ' + country_code)

sys.stdout.write('Languages: ')
languages = country_info['languages']
for i in range(0, len(languages)):
    sys.stdout.write(languages[i]['name'] + ' (' + languages[i]['iso639_1'] + ')')
    if i != len(languages) - 1:
        sys.stdout.write(', ')
sys.stdout.write('\n')

print('Currency: ' + currency_code + ' (1 ' + currency_code + ' = ' + str(currency_rate) + ' USD)')

sys.stdout.write('Time: ')
timezones = country_info['timezones'];
now = datetime.now(tz=FixedOffset())
for i in range (0, len(timezones)):
    # UTC-06:00, UTC+05:00
    # 012345678
    timezone = timezones[i]
    offset = 0
    if timezone != 'UTC':
        is_minus = timezone[3] == '-'
        hours = int(timezone[4:6])
        minutes = int(timezone[7:9])
        offset = hours * 60 + minutes
        if is_minus:
            offset = -offset;
    now = now.astimezone(tz=FixedOffset(offset=offset))
    sys.stdout.write(now.strftime('%H:%M:%S') + ' (' + timezone + ')')
    if i != len(timezones) - 1:
        sys.stdout.write(', ')
sys.stdout.write('\n')

def deg2rad(deg):
    return deg * (math.pi/180)

def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
  earth_radius = 6371; # Radius of the earth in km
  d_lat = deg2rad(lat2-lat1)
  d_lon = deg2rad(lon2-lon1)
  a = math.sin(d_lat/2) * math.sin(d_lat/2) + math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2)) * math.sin(d_lon/2) * math.sin(d_lon/2)
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
  d = earth_radius * c # Distance in km
  return d

bs_as_lat = -34.6
bs_as_lon = -58.4
country_lat = country_info['latlng'][0]
country_lon = country_info['latlng'][1]
print('Estimated distance: ' + str(int(getDistanceFromLatLonInKm(bs_as_lat, bs_as_lon, country_lat, country_lon))) + ' km')
