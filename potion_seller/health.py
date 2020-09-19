from flask import Blueprint, jsonify
from potion_seller import machine_obj
from potion_seller.auth import auth

health_bp = Blueprint('health_bp', __name__)


@health_bp.route('/health', methods=['GET'])
@auth
def health_check():
    result = {"slots": machine_obj.get_status().rstrip().split('\n'),
              "temp": machine_obj.temperature()}

    return jsonify(result), 200
