"""
File: WeatherForecaster.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a Meteorological Forecasting service. It utilizes 
    remote sensing APIs to retrieve atmospheric parameters and performs 
    temporal analysis of climate conditions.

Complexity Analysis:
    - Time Complexity: O(1) for parameter retrieval.
    - Space Complexity: O(M) where M is the meteorological data structure size.

Logic:
    1. Geolocation Verification: Convert city/coordinate input into validated IDs.
    2. Atmospheric Retrieval: Fetch temperature, humidity, and barometric pressure.
    3. Condition Cataloging: Map weather codes to human-readable weather states.
    4. Unit Normalization: Standardize output between Metric (Celsius) and Imperial.
"""

import os
import requests
from typing import Dict, Any, Optional


class WeatherForecasterService:
    """
    A service class for atmospheric data retrieval and meteorological analysis.
    Uses Open-Meteo.com - a trusted open-source weather API.
    """

    def __init__(self):
        # Using Open-Meteo.com - trusted open-source weather API, no API key needed
        self.geocode_url = "https://geocoding-api.open-meteo.com/v1/search"
        self.weather_url = "https://api.open-meteo.com/v1/forecast"
        self.headers = {
            "User-Agent": "PythonShorts-Weather-Forensics/1.0"
        }

    def get_forecast(self, city: str) -> Dict[str, Any]:
        """
        Retrieves the meteorological state for a specified urban node.
        """
        try:
            # Step 1: Geocode the city to get coordinates
            geocode_params = {"name": city, "count": 1, "language": "en", "format": "json"}
            geo_response = requests.get(self.geocode_url, params=geocode_params, headers=self.headers, timeout=10)
            geo_response.raise_for_status()
            geo_data = geo_response.json()

            if not geo_data.get("results"):
                return {"success": False, "error": f"City '{city}' not found"}

            location = geo_data["results"][0]
            lat, lon = location["latitude"], location["longitude"]
            city_name = location["name"]

            # Step 2: Get current weather data
            weather_params = {
                "latitude": lat,
                "longitude": lon,
                "current": "temperature_2m,relative_humidity_2m,surface_pressure,weather_code,wind_speed_10m",
                "timezone": "auto"
            }
            weather_response = requests.get(self.weather_url, params=weather_params, headers=self.headers, timeout=10)
            weather_response.raise_for_status()
            weather_data = weather_response.json()

            current = weather_data["current"]

            # Map WMO weather codes to descriptions
            weather_codes = {
                0: "Clear sky", 1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
                45: "Foggy", 48: "Depositing rime fog",
                51: "Light drizzle", 53: "Moderate drizzle", 55: "Dense drizzle",
                61: "Slight rain", 63: "Moderate rain", 65: "Heavy rain",
                71: "Slight snow", 73: "Moderate snow", 75: "Heavy snow",
                80: "Slight rain showers", 81: "Moderate rain showers", 82: "Violent rain showers",
                95: "Thunderstorm", 96: "Thunderstorm with slight hail", 99: "Thunderstorm with heavy hail"
            }
            
            weather_code = current.get("weather_code", 0)
            condition = weather_codes.get(weather_code, "Unknown")

            return {
                "success": True,
                "city": city_name,
                "temperature": current["temperature_2m"],
                "condition": condition,
                "humidity": current["relative_humidity_2m"],
                "pressure": current["surface_pressure"],
                "wind_speed": current["wind_speed_10m"] / 3.6,  # Convert km/h to m/s
                "source": "Open-Meteo API"
            }

        except Exception as e:
            return {"success": False, "error": str(e)}


def main():
    """
    Demonstrates the Meteorological Forecasting service.
    """
    print("--- Atmospheric Science: Meteorological Forecasting Service ---")
    print(f"Service: WeatherForecaster.py | Authors: Amey Thakur & Mega Satish\n")

    try:
        service = WeatherForecasterService()
        
        target_nodes = ["New York", "London", "Tokyo"]

        print("[Meteorological Observation Log]")
        for city in target_nodes:
            report = service.get_forecast(city)
            if report["success"]:
                print(f"  [+] Node: {report['city']:<10} | Temp: {report['temperature']}°C")
                print(f"      State: {report['condition']} | Humidity: {report['humidity']}% | P: {report['pressure']} hPa")
            else:
                print(f"  [-] Failed retrieval for {city}: {report['error']}")

        print("\nScholarly Notice:")
        print("    Atmospheric Logic: Data retrieval follows the temporal resolution")
        print("    of remote sensing satellites and calibrated ground sensors.")

    except Exception as e:
        print(f"Error during service initialization: {e}")

    print("\n--- Observation Complete ---")


if __name__ == "__main__":
    main()
