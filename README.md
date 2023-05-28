## Description
This is a FastAPI + PostgreSQL project with basic create/read functionality.
We have `characters` and `items` that we can write in the database with basic pkey and fkey relationship. 

## Setup

Steps to run program:
1. Install python3 (Recommended in project: python3.9)
2. Install python-poetry
```
curl -sSL https://install.python-poetry.org | python3
```
3. Install postgresql
```
brew install postgresql
```

4. Setup postgresql server
```env
SQLALCHEMY_DB_URL="postgresql://username:password@localhost:5432"
```

5. Setup poetry venv and packages
```
poetry env use python3.9
poetry install
```

6. Initialize table/s
```SQL
CREATE TABLE characters (
	id SERIAL PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	is_active BOOL
);

CREATE TABLE items (
	id SERIAL PRIMARY KEY,
	name VARCHAR ( 50 ) NOT NULL,
	description VARCHAR (250),
	owner_id INT
);
```

## How to Use:
Run the program:
```bash
poetry run uvicorn main:app --port 8000 --reload
```

API documentation can be seen in FastAPI's built-in swagger documentation at:
```
localhost:8000/docs
```

Alternatively, you can import the postman collection from `postman_sample/rpg_postman_collection.json`
