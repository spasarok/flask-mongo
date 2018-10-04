# Flask-Mongo

A REST API powered by Flask and MongoDB.

# Requirements

* Docker
* Python 3
* Virtualenv (or your preferred Python environment)

## Suggested Tools

* Robo3T

# Setup

Create a virtual environment for this project.

```
virtualenv -p $(which python3) ~/venv/flask-mongo
```

Activate your virtual environment.

```
source ~/venv/flask-mongo/bin/activate
```

Install project requirements.

```
pip install -r requirements.txt
```

# Run

## App

Add the app to your Python path.

```
export PYTHONPATH=$(pwd)
```

Run the app at `localhost:5000`.

```
python api/main.py
```

## Docker

Start MongoDB in a docker container.

```
docker-compose up
```

Stop MongoDB container but do not clear data (start with same data on container restarts).

```
docker-compose down
```

Stop MongoDB container and clear data (start with fresh data on container restart).

```
docker-compose down -v
```
