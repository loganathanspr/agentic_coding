from fastapi import FastAPI, HTTPException, Query

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

<<<<<<< HEAD
@app.get("/lunch-menu")
async def get_lunch_menu(day: str = Query(..., description="Day of the week for which to get the lunch menu")):
    """Get lunch menu for a given day"""
    # Hardcoded lunch menu data for different days
    lunch_menus = {
        "monday": {
            "day": "Monday",
            "menu": ["Pizza", "Salad", "Fruit"]
        },
        "tuesday": {
            "day": "Tuesday", 
            "menu": ["Burger", "Soup", "Cookie"]
        },
        "wednesday": {
            "day": "Wednesday",
            "menu": ["Pasta", "Garlic Bread", "Apple"]
        },
        "thursday": {
            "day": "Thursday",
            "menu": ["Tacos", "Rice", "Orange"]
        },
        "friday": {
            "day": "Friday",
            "menu": ["Fish", "Chips", "Yogurt"]
        },
        "saturday": {
            "day": "Saturday",
            "menu": ["Sandwich", "Salad", "Banana"]
        },
        "sunday": {
            "day": "Sunday",
            "menu": ["Chicken", "Vegetables", "Ice Cream"]
        }
    }
    
    # Convert day to lowercase for case-insensitive matching
    day_lower = day.lower()
    
    if day_lower not in lunch_menus:
        raise HTTPException(
            status_code=404, 
            detail=f"No lunch menu found for '{day}'. Available days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday"
        )
    
    return lunch_menus[day_lower]
=======
@app.get("/translate")
async def translate(text: str, target_lang: str):
    """Translate text to a target language"""
    # Mock translation - in a real implementation, this would call a translation API
    return {
        "original_text": text,
        "target_language": target_lang,
        "translated_text": f"[{target_lang.upper()}] {text}"
    }
>>>>>>> origin/main

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
