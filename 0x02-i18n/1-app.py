#!/usr/bin/env python3
'''
1-app module
'''
from flask import Flask, render_template
from flask_babel import Babel
from typing import List


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('1-index.html')
