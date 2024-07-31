#!/usr/bin/env python3
'''
1-app module
'''
from flask import Flask, render_template
from flask_babel import Babel
from typing import List

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
babel = Babel(app)


class Config:
    '''config class'''
    LANGUAGES: List[str] = ['en', 'fr']


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('1-index.html')
