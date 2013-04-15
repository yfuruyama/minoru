# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from flask import render_template

from fontimage import get_font_image
from minoru import write_minoru

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/create')
def create():
	word = request.args.get('word', ' ')
	image = get_font_image(word)
	minoru_str = write_minoru(image)
	return render_template('create.html', minoru_str=minoru_str)

if __name__ == '__main__':
	app.run(debug=True)
