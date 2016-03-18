FROM python:onbuild

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
RUN pip install gunicorn

# Install Node.js
RUN \
  curl -sL https://deb.nodesource.com/setup_5.x | bash - \
  apt-get update \
  apt-get install -y nodejs

RUN npm install apidoc -g
