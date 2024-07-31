#!/usr/bin/env python3
'''
4-app module
'''
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


def get_locale() -> str:
    '''get locale from request'''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app, get_locale)


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('4-index.html')
