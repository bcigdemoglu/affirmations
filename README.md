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

# Run backend
uvicorn backend.app:app --host 127.0.0.1 --port 5000 --reload
```

## Backend Development History

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
