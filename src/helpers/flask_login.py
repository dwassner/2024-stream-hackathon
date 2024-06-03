import secrets

from flask import Flask

WEEKS = 2
SECONDS_PER_WEEK = 60 * 60 * 24 * 7
FLASK_SECRET_KEY = secrets.token_hex()

server = Flask(__name__)
server.config.update(SECRET_KEY=FLASK_SECRET_KEY)
server.config["REMEMBER_COOKIE_DURATION"] = WEEKS * SECONDS_PER_WEEK
