#!/bin/bash

echo "Running database initialization..."
python -m app.db

echo "Starting the FastAPI application..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
