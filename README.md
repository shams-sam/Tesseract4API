# Tesseract4API
Flask-Uwsgi based endpoints for pytesseract wrapper using Tesseract 4

### References:
- [Pytesseract](https://pypi.org/project/pytesseract/)
- [Tesseract 4 Docker](https://github.com/tesseract-shadow/tesseract-ocr-re)
- [Flask on Uwsgi](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04)

### Features:
- built on top of tesseract 4 runtime environment docker image
- exposes functions of pytesseract wrapper
- uses uwsgi for production deployments

### Setup

```
#to build the image 
docker-compose build

# to run the service
docker-compose up -d

# to stop the service
docker-compose down
```

### Python usage

```python
import requests

image = open('path_to_image.file', 'rb').read()

# if calling from another service in docker compose
r = requests.post('http://tesseract:8888/image_to_string', files={'file': image})

# if calling from another elsewhere in docker compose
r = requests.post('http://<local_or_aws_endpoint>:8888/image_to_string', files={'file': image})

print(r.text)
```
