# Open Campus API
[![Build Status](https://travis-ci.org/Tri-Try/REST.svg?branch=master)](https://travis-ci.org/Tri-Try/REST)
[ ![Codeship Status for Tri-Try/REST](https://codeship.com/projects/5cf75790-dfdc-0133-639f-0e99657653d8/status?branch=master)](https://codeship.com/projects/145102)
# Reqirements:
  - Python 3.4+
  - npm

# Build:
- Local machine:

  First, you need to install dependencies and crawling the data.

  ```bash
  # Install dependencies
  npm install apidoc -g
  pip install -r requirements.txt

  python manage.py syncdb
  python manage.py crawl

  # generate static documents
  make apidoc

  # Run server
  python manage.py runserver
  ```

  Open `http://127.0.0.1:5000` in your browser!

- Docker build:
  ```bash
  # Build all depencies in docker environment.
  docker-compose build

  # Start a running container
  docker-compose up -d

  docker-compose run web python manage.py syncdb
  docker-compose run web python manage.py crawl

  # generate static documents
  docker-compose run web make apidoc
  ```

  In docker build, doesn't need to specify port number, `nginx` will make it.
  Just open `http://${DOCKER_CONTAINER_IP}` in browser.
