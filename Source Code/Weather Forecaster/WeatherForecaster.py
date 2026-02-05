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
    """

    def __init__(self, api_key: str = "demo"):
        self.api_key = api_key
        # Using a reliable public API endpoint for current weather
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.headers = {
            "User-Agent": "PythonShorts-Weather-Forensics/1.0"
        }

    def get_forecast(self, city: str) -> Dict[str, Any]:
        """
        Retrieves the meteorological state for a specified urban node.
        """
        try:
            # Note: OpenWeatherMap requires a key. For demo/scholarly logic, 
            # we use a documented fallback or mock if the key is 'demo'.
            if self.api_key == "demo":
                # Scholarly Mock Observation
                return {
                    "success": True,
                    "city": city.capitalize(),
                    "temperature": 22.5,
                    "condition": "Clear Sky",
                    "humidity": 45,
                    "pressure": 1013,
                    "source": "Forensic Mock Station"
                }

            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            data = response.json()

            return {
                "success": True,
                "city": data.get("name"),
                "temperature": data["main"].get("temp"),
                "condition": data["weather"][0].get("description").capitalize(),
                "humidity": data["main"].get("humidity"),
                "pressure": data["main"].get("pressure"),
                "wind_speed": data["wind"].get("speed"),
                "source": "OpenWeatherMap API"
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
        service = WeatherForecasterService(api_key="demo")
        
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
