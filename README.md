# Open Campus API
**A demo version.**

# Reqirements:
  - Python 3+
  - npm

# Build:
  - npm install apidoc -g
  - apidoc --input application/ --output application/static/doc/
  - python manage.py crawl

# Usage:
- Local test:
  1. pip install -r requirements.txt
  2. python api-service.py
  3. Open `http://127.0.0.1:5000`

- Docker build:
  1. docker-compose build
  2. docker-compose up `options: -d`
  3. Open `http://YOUR_MACHINE_IP`
