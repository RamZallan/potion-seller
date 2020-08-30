from flask import Flask, jsonify

from potion_seller import config
from potion_seller.machine import Machine

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config["SECRET_KEY"]

# Create a machine object from the config values generated in config.py
machine = Machine(
    app.config["MACHINE_NAME"],
    app.config["SLOT_ADDRESSES"],
    app.config["TEMP_ADDRESS"],
    app.config["DROP_TIMING"],
)

# pylint: disable=wrong-import-position
from potion_seller.drop import drop_bp
from potion_seller.health import health_bp

app.register_blueprint(health_bp)
app.register_blueprint(drop_bp)


@app.errorhandler(404)
def handle_404(err):
    error = {
        "message": "What you're looking for does not exist, like a drink admin when drink is empty",
        "error": str(err),
        "errorCode": 404,
    }

    return jsonify(error), 404
