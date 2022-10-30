# journey-within-without
Using AI's superpowers to help us in our darkest times

## Build Pre-Setup

Following steps on https://tutlinks.com/create-and-deploy-fastapi-app-to-heroku/
```
# Setup ptyhon and virtual env
python3 -m venv env
source ./env/bin/activate
python -m pip install --upgrade pip

# Install fast api
pip install fastapi
pip install uvicorn

# To serve on heroku
pip install gunicorn

# Free all reqs
pip freeze > requirements.txt
```

## Build Setup

```
pip install -r requirements.txt
```