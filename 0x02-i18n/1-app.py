#!/usr/bin/env python3
'''
1-app module
'''
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''config class'''
    LANGUAGES = ['en', 'fr']


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('1-index.html')
