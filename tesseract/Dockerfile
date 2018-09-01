# use tesseract 4 
# reference: https://github.com/tesseract-shadow/tesseract-ocr-re
FROM tesseractshadow/tesseract4re

RUN apt-get update && \
	apt-get -y upgrade && \
	apt-get -y install \
	python \
	python-pip

# Set the working directory to /app
WORKDIR /app

ADD ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8888 available to the world outside this container
EXPOSE 8888
