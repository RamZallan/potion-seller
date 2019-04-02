# Potion Seller

> Fit for a beast, let alone a man


Potion Seller is a Flask app meant to run on each Raspberry Pi of the [CSH](https://csh.rit.edu) Drink machines, which interfaces with [Mizu](https://github.com/zthart/mizu/), the latest Drink Server.


## Development

1. `$ make` to install dependencies

2. `$ pipenv shell`

3. `$ cp config.ini.sample config.ini` and fill in the variables in your new `config.ini`

4. `$ chmod +x ./wsgi.py`

5. `$ ./wsgi.py`

