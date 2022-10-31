# affirmations

Using AI's superpowers to help us in our darkest times

## Backend Build Setup

```bash
# Install pip if "pip" not installed
pip -V || brew install python

# Setup python virtual env
python3.10 -m venv env
source ./env/bin/activate
python -m pip install --upgrade pip

# Install reqs
pip install -r requirements.txt

# Add you OPENAI_API_KEY and MONGODB_URL to a SECRETS.sh file at root
source SECRETS.sh

# Run backend
python -m uvicorn backend.app:app --host 127.0.0.1 --port 5000 --reload
```

Access website from http://127.0.0.1:5000
Swagger Docs from http://127.0.0.1:5000/docs
Redoc Docs from http://127.0.0.1:5000/redoc

## Testing

### Test Backend

```bash
python -m pytest tests/tests.py
```

## Backend Development Guide

Following steps on <https://tutlinks.com/create-and-deploy-fastapi-app-to-heroku/>

```bash
# Setup ptyhon and virtual env
python3.10 -m venv env
source ./env/bin/activate
python -m pip install --upgrade pip

# Install fast api with all reqs
pip install "fastapi[all]"

# OR install min reqs
pip install fastapi
pip install uvicorn

# To serve on heroku
pip install gunicorn

# Free all reqs
pip freeze > requirements.txt
```
