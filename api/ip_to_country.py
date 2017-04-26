import urllib2, json

class IPToCountry:
    IP2COUNTRY_API_URL = 'https://api.ip2country.info/'

    def get_country_code_from_ip(self, ip):
        """
        Returns the ISO country code for the given IP
        """
        request_url = IPToCountry.IP2COUNTRY_API_URL + 'ip?' + ip
        try:
            response = urllib2.urlopen(request_url)
            country_basic_info = json.loads(response.read())
            return country_basic_info
        except urllib2.URLError as e:
            raise e
