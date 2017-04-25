import urllib2, json

class Countries:
    COUNTRIES_API_URL = 'https://restcountries.eu/rest/v2/alpha/'

    def get_country_info(self, country_code, fields):
        """
        country_code: 2-character ISO country code
        fields: array with different fields such as name, languages, etc.
        All available fields are specified in restcountries.eu

        Returns a dict with all requested fields
        """
        country_fields = 'fields='
        for f in fields:
            country_fields += f + ';'
        request_url = Countries.COUNTRIES_API_URL + country_code + '?' + country_fields
        try:
            response = urllib2.urlopen(request_url)
            country_info = json.loads(response.read())
            return country_info
        except urllib2.URLError as e:
            raise e
