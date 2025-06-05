import pandas as pd
import os

def clean_car_data():
    raw_path = "data/raw/car_data_raw.csv"
    processed_path = "data/processed/car_data_clean.csv"

    if not os.path.exists(raw_path):
        print("❌ Raw data file not found.")
        return

    df = pd.read_csv(raw_path)
    cleaned_df = df.dropna(subset=["make", "model", "fuel_type", "drive"])
    cleaned_df = cleaned_df.drop_duplicates()

    os.makedirs("data/processed", exist_ok=True)
    cleaned_df.to_csv(processed_path, index=False)
    print("✅ Cleaned data saved.")
# This function reads the raw car data, cleans it by removing rows with missing values in critical columns,
# and saves the cleaned data to a new CSV file. It ensures that the data is ready for loading into PostgreSQL.
# The cleaned data is stored in a structured format, making it suitable for further analysis or database insertion.
# This script is part of the ETL process, specifically for the transformation phase.