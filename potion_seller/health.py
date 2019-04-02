from flask import Blueprint, jsonify
from potion_seller import app

health_bp = Blueprint('health_bp', __name__)


@health_bp.route('/health', methods=['GET'])
def health_check():
    result = {
        "slots": [],
    }
    for addr in app.config['W1_ADDRESSES']:
        result['slots'].append('Get value for: ' + addr)
    return jsonify(result), 200


