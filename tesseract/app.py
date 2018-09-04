# Pytesseract Reference: https://pypi.org/project/pytesseract/
# Tesseract Reference: https://github.com/tesseract-shadow/tesseract-ocr-re

from flask import Flask, request, send_file

import os
import pytesseract
from PIL import Image
import subprocess

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/image_to_readable_pdf", methods=["POST"])
def get_readable_pdf():
	file = request.files.getlist("file")
	file = file[0]
	filename = file.filename
	file.save(filename)

	if 'output_file.pdf' in os.listdir('.'):
		os.remove('output_file.pdf')

	subprocess.call(
		"tesseract " + \
		filename + \
		" output_file --psm 6 --oem 3 pdf",
		shell=True
	)
	os.remove(filename)

	res = None
	if 'output_file.pdf' in os.listdir('.'):
		return send_file('output_file.pdf')

	return 'None'


@app.route("/image_to_string", methods=["POST"])
def image_to_string():
	file = request.files.getlist("file")
	image = Image.open(file[0])
	result = pytesseract.image_to_string(image, config="--psm 4")

	return result

@app.route("/image_to_boxes", methods=["POST"])
def image_to_boxes():
	file = request.files.getlist("file")
	image = Image.open(file[0])
	result = pytesseract.image_to_boxes(image)

	return result

@app.route("/image_to_data", methods=["POST"])
def image_to_data():
	file = request.files.getlist("file")
	image = Image.open(file[0])
	result = pytesseract.image_to_data(image)

	return result

@app.route("/image_to_osd", methods=["POST"])
def image_to_osd():
	file = request.files.getlist("file")
	image = Image.open(file[0])
	result = pytesseract.image_to_osd(image)

	return result

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)
