# FastAPI Simple Application

This is a simple FastAPI application that serves a "Hello, World!" message and health check via HTTP API. The application consists of a single `app.py` file with two main endpoints and uses FastAPI with Uvicorn as the ASGI server.

**ALWAYS reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Working Effectively

### Bootstrap and Setup
- **Environment**: Python 3.12+ is required and available
- **Dependencies**: Install with `pip install -r requirements.txt`
  - **Normal completion time**: ~10 seconds when network is available
  - **Known issue**: `pip install` may fail due to network timeouts with PyPI - retry with `pip install --timeout 120 -r requirements.txt` or install packages individually if this occurs
- **No build step required** - this is a pure Python application with no compilation needed

### Running the Application
Choose one of two methods (both work identically):

**Method 1: Direct Python execution**
```bash
python app.py
```

**Method 2: Uvicorn command**
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

Both methods start the server on `http://localhost:8000` within 2-3 seconds.

### Testing and Validation
**ALWAYS validate your changes by running the complete validation scenario below:**

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application** (using either method above)

3. **Test all endpoints:**
   ```bash
   # Root endpoint - should return {"message": "Hello, World!"}
   curl http://localhost:8000/
   
   # Health check - should return {"status": "healthy"}  
   curl http://localhost:8000/health
   
   # API documentation - should return HTML page
   curl http://localhost:8000/docs
   ```

4. **Verify responses:**
   - Root (`/`) must return: `{"message": "Hello, World!"}`
   - Health (`/health`) must return: `{"status": "healthy"}`
   - Docs (`/docs`) must return: HTML page with Swagger UI

**CRITICAL: Always run through this complete validation after making any changes to ensure the application still functions correctly.**

## Repository Structure

```
.
├── README.md              # User documentation
├── app.py                 # Main application file (298 bytes)
├── requirements.txt       # Python dependencies (fastapi==0.104.1, uvicorn==0.24.0)
├── .gitignore            # Git ignore rules for Python projects
└── .github/
    └── copilot-instructions.md  # This file
```

## Key Application Details

### Main Application File (`app.py`)
- **Size**: 298 bytes - very simple application
- **Framework**: FastAPI with two route handlers
- **Endpoints**:
  - `GET /` - Returns JSON greeting message
  - `GET /health` - Returns health status 
  - `GET /docs` - Auto-generated API documentation (FastAPI feature)
- **Server**: Uses Uvicorn ASGI server when run directly

### Dependencies (`requirements.txt`)
- `fastapi==0.104.1` - Web framework
- `uvicorn==0.24.0` - ASGI server
- **Install time**: ~10 seconds on standard systems

## Development Guidelines

### Making Changes
1. **Always install dependencies first** if working in a fresh environment
2. **Test changes immediately** using the validation scenario above
3. **Both startup methods must work** - test both `python app.py` and `uvicorn app:app --host 0.0.0.0 --port 8000`
4. **All three endpoints must respond correctly** - root, health, and docs

### Common Tasks
- **Add new endpoint**: Modify `app.py` and add a new `@app.get()` decorated function
- **Change response format**: Modify return values in existing functions
- **Add dependencies**: Update `requirements.txt` and run `pip install -r requirements.txt`
- **Update server config**: Modify the `uvicorn.run()` call in `app.py` line 15

### Validation Requirements
**NEVER SKIP VALIDATION** - Always run the complete test scenario when:
- Adding new endpoints
- Modifying existing endpoints  
- Changing dependencies
- Updating server configuration
- Making any code changes

### Timing Expectations
- **Dependency installation**: ~10 seconds
- **Application startup**: 2-3 seconds
- **Endpoint response**: Immediate (under 100ms)
- **No build/compilation time** - changes are immediately active

### Important Notes
- **No test framework configured** - manual validation is required
- **No linting/formatting tools** - code style is manual
- **No CI/CD pipelines** - all validation is local
- **No database or external dependencies** - self-contained application
- **Default port 8000** - ensure no conflicts with other services

## Quick Reference Commands

```bash
# Complete setup and validation workflow:
pip install -r requirements.txt  # May require --timeout 120 if network issues occur
python app.py &                  # Starts server in background
sleep 2                          # Allow server to start
curl http://localhost:8000/      # Should return: {"message": "Hello, World!"}
curl http://localhost:8000/health  # Should return: {"status": "healthy"}
curl http://localhost:8000/docs    # Should return: HTML page
kill %1                          # Stop background server

# Alternative startup method test:
uvicorn app:app --host 0.0.0.0 --port 8000 &
sleep 2
curl http://localhost:8000/
kill %1
```

**ALWAYS use this complete validation workflow to ensure your changes work correctly.**

## Network and Environment Notes
- **PyPI connectivity**: If `pip install` times out, try `pip install --timeout 120 -r requirements.txt`
- **Port conflicts**: Ensure port 8000 is available; if not, modify the port in `app.py` line 15
- **Firewall**: Application listens on 0.0.0.0:8000 - ensure firewall allows this if testing from remote machines