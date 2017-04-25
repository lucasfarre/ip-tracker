# ip_tracker
IP tracker developed with Python using public APIs.

## How to run it?
Clone the repo, open a terminal and navigate to the folder where is located the **iptracker.py** file:
``` bash
cd path_to_the_directory_where_is_the_iptracker.py_file
```
Then execute for example:
``` bash
python iptracker.py 194.69.254.120
```
This last command will track the given IP and get data about the country of origin, including languages, currency rates, time and estimated distance to Buenos Aires.

For help you can execute:
``` bash
python iptracker.py -h
```

## Public APIs used
[ip2country](https://ip2country.info/) for mapping an IP to a country.

[REST Countries](https://restcountries.eu/) for retrieving basic information about the country.

[Fixer.io](http://fixer.io/) for retrieving exchange rates.
