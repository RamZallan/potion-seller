import secrets
import socket
from os import environ as env

ENV = env.get("POTION_SELLER_ENV", default="production")
DEBUG = env.get("POTION_SELLER_DEBUG", "false").lower() == "true"
IP = env.get("POTION_SELLER_IP", "0.0.0.0")
PORT = env.get("POTION_SELLER_PORT", 5000)
SECRET_KEY = env.get("POTION_SELLER_SECRET_KEY", default="".join(secrets.token_hex(16)))

MACHINE_NAME = env.get("POTION_SELLER_MACHINE_NAME", socket.gethostname().split(".")[0])
API_KEY = env.get("POTION_SELLER_API_KEY", default="".join(secrets.token_hex(16)))
SLOT_ADDRESSES = [
    addr for addr in env.get("POTION_SELLER_SLOT_ADDRESSES", "").split(",") if addr
]
TEMP_ADDRESS = env.get("POTION_SELLER_TEMP_ADDRESS", None)
DROP_TIMING = float(env.get("POTION_SELLER_DROP_TIMING", "0.5"))
