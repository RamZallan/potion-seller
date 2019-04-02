from flask import Blueprint, jsonify, request
from potion_seller import app

drop_bp = Blueprint('drop_bp', __name__)


@drop_bp.route('/drop/', methods=['POST'])
def drop_drink():
    slot = request.get_json()['slot']
    if slot > len(app.config['W1_ADDRESSES']): # slot index doesn't exist
        return jsonify('Could not find slot ' + str(slot)), 400
    else:
        return jsonify('dropping drink at slot: ' + str(slot)), 200

