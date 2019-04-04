import os

from flask import Flask, jsonify, request, session

from potion_seller import config

app = Flask(__name__)

app.config.from_object(config)
if os.path.exists(os.path.join(os.getcwd(), 'config.py')):
    app.config.from_pyfile(os.path.join(os.getcwd(), 'config.py'))

app.secret_key = app.config['SECRET_KEY']

from potion_seller.machine import Machine
# Create a machine object from the config values generated in config.py
machine_obj = Machine(app.config['MACHINE_NAME'], 
                      app.config['W1_ADDRESSES'], 
                      app.config['TEMP_ADDRESS'],
                      app.config['DROP_TIMING'])

from potion_seller.health import health_bp
from potion_seller.drop import drop_bp


app.register_blueprint(health_bp)
app.register_blueprint(drop_bp)

@app.errorhandler(404)
def handle_404(e):
    error = {
        "message": "What you're looking for does not exist, like a drink admin when drink is empty",
        "error": str(e),
        "errorCode": 404,
    }

    return jsonify(error), 404

