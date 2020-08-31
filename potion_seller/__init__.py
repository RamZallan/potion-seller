from flask import Flask, jsonify

from potion_seller import config
from potion_seller.machine import Machine
from potion_seller.machine_test import mock_machine

app = Flask(__name__)
app.config.from_object(config)
app.secret_key = app.config["SECRET_KEY"]


def init_machine():
    if app.config["ENV"] in ("test", "staging"):
        mach = Machine(
            app.config["MACHINE_NAME"],
            ["SLOT1", "SLOT2", "SLOT3"],
            ["TEMP0"],
            app.config["DROP_TIMING"],
        )

        return mock_machine(mach)

    return Machine(
        app.config["MACHINE_NAME"],
        app.config["SLOT_ADDRESSES"],
        app.config["TEMP_ADDRESS"],
        app.config["DROP_TIMING"],
    )


machine = init_machine()

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
