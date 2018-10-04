# Requirements

* Docker
* Python 3
* Virtualenv (or your preferred Python environment)

# Setup

Create a virtual environment for this project.

```
virtualenv -p $(which python3) ~/venv/flask-mongo
```

Activate your virtual environment.

```
source ~/venv/flask-mongo
```

Install project requirements.

```
pip install -r requirements.txt
```

# Run

## App

Run the app at `localhost:5000`.

```
python -m api.main
```

## Docker

This project uses Docker to run a local MongoDB instance.

### Commands

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
