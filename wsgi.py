#!/usr/bin/env python3

import os
from potion_seller import app

if __name__ == "__main__":
    app.debug = app.config['DEBUG']
    app.run(host=app.config['IP'], port=app.config['PORT'])

application = app

