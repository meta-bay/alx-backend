#!/usr/bin/env python3
'''
1-app module
'''
from flask import Flask, render_template
from flask_babel import Babel
from typing import List
from flask import request


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    '''get locale from request'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])
