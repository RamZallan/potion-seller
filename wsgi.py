#!/usr/bin/env python3

import os
from potion_seller import app

if __name__ == "__main__":
    cert_path = '/etc/letsencrypt/live/{}.csh.rit.edu/'.format(app.config['MACHINE_NAME'])
    app.debug = app.config['DEBUG']
    if not app.debug:
        app.run(host=app.config['IP'], 
                port=app.config['PORT'], 
                ssl_context=(cert_path+'fullchain.pem', cert_path+'privkey.pem'))
    else:
        app.run(host=app.config['IP'], port=app.config['PORT'])

application = app

