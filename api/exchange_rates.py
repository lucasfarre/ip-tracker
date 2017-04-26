import urllib2, json

class ExchangeRates:
    EXCHANGE_RATES_API_URL = 'http://api.fixer.io/'

    def get_latest_rate(self, currency_code='EUR', base_currency_code='USD'):
        """
        Returns the latest rate of the given currency_code for the given
        base_currency_code. Returns None if there is no rate available.
        """
        request_url = ExchangeRates.EXCHANGE_RATES_API_URL + 'latest?base=' + base_currency_code + '&symbols=' + currency_code
        try:
            response = urllib2.urlopen(request_url)
            currency_rates = json.loads(response.read())['rates']
            currency_rate = None
            if currency_code in currency_rates:
                currency_rate = 1 / currency_rates[currency_code]
            return currency_rate
        except urllib2.URLError as e:
            raise e
