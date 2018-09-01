# Pytesseract Reference: https://pypi.org/project/pytesseract/
# Tesseract Reference: https://github.com/tesseract-shadow/tesseract-ocr-re

from flask import Flask, request

import pytesseract
from PIL import Image

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/image_to_string", methods=["POST"])
def image_to_string():
	print(request.files)
	file = request.files.getlist("file")
	image = Image.open(file[0])
	result = pytesseract.image_to_string(image)

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