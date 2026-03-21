"""
exercise_01_dict_parsing.py

Simulates parsing a JSON response from a weather API.
Practices dictionary navigation, list indexing, and string formatting
in preparation for making real API calls.

Author: Hunter
Date: 2026-03-21
"""

# ── Constants ──────────────────────────────────────────────────────────────────

weather_data = {
    "city": "Jackson",
    "country": "US",
    "temperature": {
        "current": 87,
        "feels_like": 93,
        "unit": "Fahrenheit"
    },
    "conditions": ["humid", "partly cloudy", "chance of storms"],
    "wind": {
        "speed": 12,
        "direction": "SW"
    },
    "forecast": [
        {"day": "Tuesday", "high": 91, "low": 74},
        {"day": "Wednesday", "high": 88, "low": 72},
        {"day": "Thursday", "high": 85, "low": 70}
    ]
}


# ── Step 1: Current conditions ─────────────────────────────────────────────────
#f string{city}, city not standalone variable. 
#its a key inside weather_data
print(f"{weather_data['city']}, {weather_data['country']} | "
      f"{weather_data['temperature']['current']}°F (feels like {weather_data['temperature']['feels_like']}°F) | "
      f"{weather_data['conditions'][1]}")


# ── Step 2: Forecast(for loop loop through) ───────────────────────────────────────────────────────────
#already in weather_data so dont have to call it with day
for day in weather_data["forecast"]:
    print(f"{day['day']}: high {day['high']}°F / low {day['low']}°F")
    


# ── Step 3: Wind ───────────────────────────────────────────────────────────────

# Your code goes here