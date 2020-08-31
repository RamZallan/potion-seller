from flask import Blueprint, jsonify, request

from potion_seller import machine
from potion_seller.auth import auth

drop_bp = Blueprint("drop_bp", __name__)


@drop_bp.route("/drop", methods=["POST"])
@auth
def drop_drink():
    if request.headers.get("Content-Type") != "application/json":
        failure = {
            "error": "Please ensure the content-type of your request is valid",
            "errorCode": 400,
        }
        return jsonify(failure), 400

    try:
        slot = int(request.get_json()["slot"])
        if slot < 1:
            raise ValueError
    except ValueError:
        failure = {
            "error": "Ensure that the slot number is a valid, positive integer",
            "errorCode": 400,
        }
        return jsonify(failure), 400

    if slot > len(machine.slots):  # slot index doesn't exist
        failure = {
            "error": "The slot number provided was beyond the range of the machine (slots: {})".format(
                len(machine.slots)
            ),
            "errorCode": 400,
        }

        return jsonify(failure), 400

    if machine.drop(slot):
        success = {"message": "Dropped drink from slot {}".format(slot)}
        return jsonify(success), 200

    failure = {
        "error": "The slot is not mounted, available, or was busy",
        "errorCode": 503,  # Service Unavailable
    }

    return jsonify(failure), 503
