#!/bin/bash

# Run the migrations
alembic upgrade head

# Start the FastAPI server
python -m uvicorn weather_api.app.main:app --reload --host 0.0.0.0 --port 8000
