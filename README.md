# Simple FastAPI App

This is a simple FastAPI application that serves a "Hello, World!" message via HTTP API.

## Features

- GET `/` - Returns a JSON response with "Hello, World!" message
- GET `/health` - Health check endpoint that returns status
- GET `/lunch-menu?day=<day>` - Returns lunch menu for a specified day

## Requirements

- Python 3.12+ (managed via pyenv)
- uv (Python package manager)

## Installation

1. **Install pyenv** (if not already installed):
   ```bash
   # On macOS
   brew install pyenv
   
   # On Ubuntu/Debian
   curl https://pyenv.run | bash
   
   # Add to your shell profile (.bashrc, .zshrc, etc.)
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

2. **Install uv** (if not already installed):
   ```bash
   # On macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Or via pip
   pip install uv
   ```

3. **Setup Python version** using pyenv:
   ```bash
   # Install Python 3.12.3 (or use the version specified in .python-version)
   pyenv install 3.12.3
   pyenv local 3.12.3  # This sets the Python version for this project
   ```

4. **Install dependencies** using uv:
   ```bash
   uv sync
   ```

   > **Note**: This project has migrated from `pip` and `requirements.txt` to `uv` and `pyproject.toml`. Dependencies are now managed in `pyproject.toml` and the exact versions are locked in `uv.lock`.

## How to Run

### Option 1: Using uv to run Python directly
```bash
uv run python app.py
```

### Option 2: Using uv with uvicorn command
```bash
uv run uvicorn app:app --host 0.0.0.0 --port 8000
```

### Option 3: Activate the virtual environment (optional)
```bash
source .venv/bin/activate  # On Linux/macOS
# .venv\Scripts\activate   # On Windows
python app.py
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

- Lunch menu endpoint:
  ```bash
  curl http://localhost:8000/lunch-menu?day=Monday
  ```
  Response: `{"day": "Monday", "menu": ["Pizza", "Salad", "Fruit"]}`

- Interactive API documentation is available at `http://localhost:8000/docs`
