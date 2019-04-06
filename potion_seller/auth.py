from flask import request, jsonify
from functools import wraps
from potion_seller import app


def auth(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        token = request.headers.get('X-Auth-Token')
        if (token == app.config['API_KEY']):
            return func(*args, **kwargs) # valid auth token
        else:
            return jsonify({'error': 'Invalid credentials', 'errorCode': 401}), 401
    return wrapped_function

