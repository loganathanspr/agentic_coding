# Simple FastAPI App

This is a simple FastAPI application that serves a "Hello, World!" message via HTTP API.

## Features

- GET `/` - Returns a JSON response with "Hello, World!" message
- GET `/health` - Health check endpoint that returns status

## Requirements

- Python 3.x
- FastAPI
- Uvicorn

## Installation

1. Make sure you have Python installed (version 3.x).
2. Open a terminal in this directory.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## How to Run

### Option 1: Using Python directly
```bash
python app.py
```

### Option 2: Using uvicorn command
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The server will start on `http://localhost:8000`.

## Testing the API

You can test the API endpoints:

- Visit `http://localhost:8000/` in your browser or use curl:
  ```bash
  curl http://localhost:8000/
  ```
  Response: `{"message": "Hello, World!"}`

- Health check endpoint:
  ```bash
  curl http://localhost:8000/health
  ```
  Response: `{"status": "healthy"}`

- Interactive API documentation is available at `http://localhost:8000/docs`
