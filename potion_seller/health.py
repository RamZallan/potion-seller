from flask import Blueprint, jsonify
from potion_seller import app, machine_obj

health_bp = Blueprint('health_bp', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    result = {
        "slots": [],
    }

    result['slots'] = machine_obj.get_status().rstrip().split('\n')
    result['temp'] = machine_obj.temperature()

    return jsonify(result), 200


