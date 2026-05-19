#!/usr/bin/env python3
"""
This module is for Babel object instantiation
"""

from flask import Flask, request, render_template, g
from flask_babel import Babel
import pytz


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

    user = getattr(g, "user", None)
    if user:
        user_locale = user.get("locale")
        if user_locale in app.config["LANGUAGES"]:
            return user_locale

    return (
        request.accept_languages.best_match(app.config["LANGUAGES"])
        or app.config["BABEL_DEFAULT_LOCALE"]
    )


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


def get_timezone():
    """
    Returns a valid URL-provided or user time zone, else UTC
    """
    timezone = request.args.get("timezone")
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass

    user = getattr(g, "user", None)
    if user:
        user_timezone = user.get("timezone")
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass

    return app.config["BABEL_DEFAULT_TIMEZONE"]


babel = Babel(
    app, locale_selector=get_locale, timezone_selector=get_timezone
)


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
    return render_template("7-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
