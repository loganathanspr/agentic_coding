from fastapi import FastAPI, Query

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

# Hardcoded lunch menu data
lunch_menus = {
    "monday": ["Pizza", "Salad", "Fruit"],
    "tuesday": ["Burger", "Fries", "Apple"],
    "wednesday": ["Pasta", "Garlic Bread", "Banana"],
    "thursday": ["Chicken Rice", "Soup", "Orange"],
    "friday": ["Fish", "Chips", "Grapes"],
    "saturday": ["Sandwich", "Juice", "Cookie"],
    "sunday": ["Wrap", "Smoothie", "Brownie"]
}

# Lunch menu endpoint
@app.get("/lunch-menu")
async def get_lunch_menu(day: str = Query(..., description="Day of the week")):
    menu = lunch_menus.get(day.lower())
    if menu:
        return {"day": day.capitalize(), "menu": menu}
    return {"error": "Menu not found for the given day."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
