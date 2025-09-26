from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/weather/{city}")
async def get_weather(city: str):
    """Get weather information for a given city"""
    # Mock weather data - in a real implementation, this would call an external weather API
    weather_data = {
        "city": city.title(),
        "temperature": 22,
        "description": "Partly cloudy",
        "humidity": 65,
        "wind_speed": 10,
        "unit": "celsius"
    }
    return weather_data

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
