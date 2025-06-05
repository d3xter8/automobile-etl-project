import os
import pandas as pd
import psycopg2

def load_to_postgresql():
    PG_HOST = os.getenv("PG_HOST", "localhost")
    PG_NAME = os.getenv("PG_NAME", "postgres")
    PG_USER = os.getenv("PG_USER", "postgres")
    PG_PASSWORD = os.getenv("PG_PASSWORD", "FRIJO@2001")

    conn = psycopg2.connect(
        host=PG_HOST,
        dbname=PG_NAME,
        user=PG_USER,
        password=PG_PASSWORD
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS car_data (
            make TEXT,
            model TEXT,
            fuel_type TEXT,
            drive TEXT,
            transmission TEXT,
            cylinders INTEGER,
            displacement FLOAT,
            class TEXT
        )
    """)
    conn.commit()

    df = pd.read_csv("data/processed/car_data_clean.csv")
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO car_data (make, model, fuel_type, drive, transmission, cylinders, displacement, class)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row.get("make"),
            row.get("model"),
            row.get("fuel_type"),
            row.get("drive"),
            row.get("transmission"),
            row.get("cylinders"),
            row.get("displacement"),
            row.get("class")
        ))
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Data loaded into PostgreSQL.")
# This function connects to a PostgreSQL database and creates a table for car data if it doesn't exist.
# It reads cleaned car data from a CSV file and inserts it into the database.
# The function ensures that the data is structured correctly and handles any potential issues with missing columns.