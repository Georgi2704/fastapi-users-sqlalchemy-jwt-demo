# fastapi-users-sqlalchemy-jwt-demo
A demo for authentication with FastAPI Users using SQLAlchemy and JWT tokens.


If you want to use a virtual environment first create the environment:

```bash
python3 -m venv .venv
source venv/bin/activate
```

You can install the required libraries with pip. The following command will install all the required
libraries for the project.

```bash
pip install -r ./requirements.txt
```

Start the server by running main.py or a hot reloading, api server:

```bash
uvicorn main:app --reload --port 5000
```

Swagger docs/GUI at:

```
http://127.0.0.1:5000/api/docs
```