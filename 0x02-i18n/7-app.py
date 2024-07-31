#!/usr/bin/env python3
'''
7-app module
'''
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app,)


@babel.localeselector
def get_locale() -> str:
    '''get locale from request'''
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    if g.user:
        user_locale = g.user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ get the timezone """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.exceptions.UnknownTimeZoneError:
                pass
    return 'UTC'


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('7-index.html')


def get_user(login_as):
    """ get user """
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """ excuted before all other functions """
    login_as = request.args.get('login_as')
    g.user = get_user(login_as)


if __name__ == '__main__':
    app.run()
