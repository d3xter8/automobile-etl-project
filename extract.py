import os
import requests
import pandas as pd

API_KEY = "Fdy6m8VVVMFzqlKGcLez7A==7TLolR00Z9LgIh2F"
HEADERS = {"X-Api-Key": API_KEY}
API_URL = "https://api.api-ninjas.com/v1/cars"

def fetch_car_data(
    models=["camry", "mustang", "3 series"],
    make=None,
    fuel_type=None,
    drive=None,
    cylinders=None,
    transmission=None
):
    all_data = []

    for model in models:
        params = {"model": model}
        if make:
            params["make"] = make
        if fuel_type:
            params["fuel_type"] = fuel_type
        if drive:
            params["drive"] = drive
        if cylinders:
            params["cylinders"] = cylinders
        if transmission:
            params["transmission"] = transmission

        try:
            response = requests.get(API_URL, headers=HEADERS, params=params)
            if response.status_code == 200:
                data = response.json()
                if data:
                    all_data.extend(data)
                    print(f"✅ Data fetched for model: {model}")
                else:
                    print(f"⚠️ No data found for model: {model}")
            else:
                print(f"❌ Error for {model}: {response.status_code} - {response.text}")

        except Exception as e:
            print(f"❌ Exception for {model}: {e}")

    os.makedirs("data/raw", exist_ok=True)
    pd.DataFrame(all_data).to_csv("data/raw/car_data_raw.csv", index=False)
    print("✅ All data fetched and saved to data/raw/car_data_raw.csv")
# This function fetches car data from the API for a list of specified models.
# It handles API responses, checks for errors, and saves the data to a CSV file.
# If no data is found for a model, it logs a warning instead of failing.
# The function ensures that the data is stored in a structured format for further processing.
# This script is part of the ETL process, specifically for the extraction phase.
