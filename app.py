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

@app.get("/translate")
async def translate(text: str, target_lang: str):
    """Translate text to a target language"""
    # Mock translation - in a real implementation, this would call a translation API
    return {
        "original_text": text,
        "target_language": target_lang,
        "translated_text": f"[{target_lang.upper()}] {text}"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
