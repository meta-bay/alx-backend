#!/usr/bin/env python3
'''
0-app module
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    '''returns the index'''
    return render_template('0-index.html')
