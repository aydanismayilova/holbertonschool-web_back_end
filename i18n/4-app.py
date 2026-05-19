#!/usr/bin/env python3
"""
This module is for Babel object instantiation
"""
from flask import Flask, request, render_template
from flask_babel import Babel


class Config:
    """
    This class is for configuring the languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale():
    """
    Determines the best match for supported languages
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def home():
    """
    Renders the template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
