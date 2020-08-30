# Potion Seller

<a href="https://github.com/RamZallan/potion-seller/blob/master/LICENSE"><img alt="License: GPL-3.0" src="https://img.shields.io/github/license/RamZallan/potion-seller"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

> Fit for a beast, let alone a man


Potion Seller is a Flask app meant to run on each Raspberry Pi of the [CSH](https://csh.rit.edu) Drink machines, which interfaces with [Mizu](https://github.com/zthart/mizu/), the latest Drink Server.


## Development

Follow the instructions below to start the server. In either case, the server will listen on: `http://localhost:5000`

### Docker (recommended)

Simply run `docker-compose up --build` to build and start the server.

The default API key (for development use only!) is: `drinkwilleatyourchildren`

### Native

1. Ensure you have Python 3.8 installed
1. `make` to install dependencies (or run the commands inside the Makefile manually)
1. `pipenv shell`
1. At a minimum, set the following configuration variables (see `potion_seller/config.py`):
    - `export POTION_SELLER_API_KEY=<key>`, replacing `<key>` with the desired API key
1. If running on an actual drink machine, these additional configuration variables should be set:
    - `export POTION_SELLER_SLOT_ADDRESSES=<addrs>`, replacing `<addrs>` with a comma-separated list of each slot's OneWire addresses as they appear in `/mnt/w1`
    - `export POTION_SELLER_TEMP_ADDRESS=<addr>`, replacing `<addr>` with the temperature sensor's OneWire address as it appears in `/mnt/w1`
1. `FLASK_APP=potion_seller flask run`
