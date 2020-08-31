from flask import Blueprint, jsonify

from potion_seller import machine
from potion_seller.auth import auth

health_bp = Blueprint("health_bp", __name__)


@health_bp.route("/healthz", methods=["GET"])
def health_check():
    return "healthy", 200


@health_bp.route("/health", methods=["GET"])
@auth
def status():
    result = {
        "slots": machine.get_status().rstrip().split("\n"),
        "temp": machine.temperature(),
    }

    return jsonify(result), 200
