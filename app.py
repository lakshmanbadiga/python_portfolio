# coding: utf-8

import os, sys
from importlib import reload

from flask import Flask, render_template, request, url_for
from datetime import datetime

_wd = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
	return render_template('home.html')
@app.route('/project')
def project():
	return render_template('project.html')
@app.route('/aboutme')
def aboutme():
	return render_template('aboutme.html')
@app.route('/tictoctoe')
def ticitoctoe():
        return render_template('index.html')
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
