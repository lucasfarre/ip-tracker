# Python IP Tracker
# by Lucas Andres Farre
import argparse, urllib2, sys
from api.ip_to_country import IPToCountry
from api.countries import Countries
from api.exchange_rates import ExchangeRates
from model.country import Country
from exception.invalid_public_ip_error import InvalidPublicIPError

# Parse arguments
parser = argparse.ArgumentParser(description='IP Tracker. Track an IP and get information about the country of origin.')
parser.add_argument('ip', metavar='ip', type=str, nargs=1, help='the IP to be tracked')
args = parser.parse_args()
ip = args.ip[0]

try:
    # Get data from the APIs
    print 'Tracking IP location...'
    try:
        country_basic_info = IPToCountry().get_country_basic_info_from_ip(ip)
    except urllib2.HTTPError as e:
        if e.code == 400:
            raise InvalidPublicIPError('Error: ' + ip + ' is not a valid public IP')
    country_code = country_basic_info['countryCode']
    if country_code == '': # ip2country returns an object with empty fields if the given IP is private e.g. 192.168.1.1
        raise InvalidPublicIPError('Error: ' + ip + ' is a private IP')
    country_emoji = country_basic_info['countryEmoji']
    print 'Getting country data...'
    country_fields = ['name','languages','timezones','latlng','currencies']
    country_info = Countries().get_country_info(country_code=country_code, fields=country_fields)
    print 'Getting currency latest rate...'
    currency_code = country_info['currencies'][0]['code']
    currency_rate = ExchangeRates().get_latest_rate(currency_code=currency_code, base_currency_code='USD')

    # Build and populate country object
    country_currency = {'code': currency_code, 'rate_against_usd': currency_rate}
    country_location = {'lat': country_info['latlng'][0], 'lon': country_info['latlng'][1]}
    country = Country(code=country_code, name=country_info['name'], emoji=country_emoji,
    languages=country_info['languages'], currency=country_currency,
    timezones=country_info['timezones'], location=country_location)

    # Show info
    print ('\n\n')
    print('IP: ' + ip)
    country.print_name_and_emoji()
    country.print_code()
    country.print_languages()
    country.print_currency()
    country.print_time()
    country.print_distance(lat=-34.6, lon=-58.4)

except InvalidPublicIPError as e:
    print e.message
except Exception:
    print 'Unknown Error: Verify your internet connection or try later'
