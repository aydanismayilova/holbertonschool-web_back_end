#!/usr/bin/env python3
"""
This module is for Babel object instantiation
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    This class is for configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """
    Determines the best match for supported languages
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app, locale_selector=get_locale)


def get_user():
    """
    Returns a user dictionary or None if ID is invalid
    """
    login_id = request.args.get("login_as")
    if login_id is None:
        return None

    try:
        return users.get(int(login_id))
    except (ValueError, TypeError):
        return None


@app.before_request
def before_request():
    """
    Sets the found user as a global on flask.g.user
    """
    g.user = get_user()


@app.route("/")
def home():
    """
    Renders the index template
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
