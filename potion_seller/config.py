import configparser
import secrets
from os import environ as env
import os

config = configparser.ConfigParser()

DEBUG = True if env.get('POTION_SELLER_DEBUG', 'false').lower() == 'true' else False
IP = env.get('POTION_SELLER_IP', '0.0.0.0')
PORT = env.get('POTION_SELLER_PORT', 8080)
SECRET_KEY = env.get('POTION_SELLER_SECRET_KEY', default=''.join(secrets.token_hex(16)))

MACHINE_CONFIG = env.get('POTION_SELLER_MACHINE_CONFIG', default=os.path.join(os.getcwd(), 'config.ini'))

config.read(MACHINE_CONFIG) # load config.ini
MACHINE_NAME = config['DRINK']['MACHINE_NAME']
API_KEY = config['DRINK']['API_KEY']
W1_ADDRESSES = config['DRINK']['W1_ADDRESSES'].split('\n')
TEMP_ADDRESS = config['DRINK']['TEMP_ADDRESS'] # temperature sensor
DROP_TIMING = float(config['DRINK']['DROP_TIMING'])

