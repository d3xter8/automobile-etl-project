import schedule
import time
from etl.extract import fetch_car_data
from etl.transform import clean_car_data
from etl.load import load_to_postgresql

def run_etl():
    # Extract Phase: Fetch car data with optional filters
    fetch_car_data(models=["camry", "mustang", "3 series"])

    # Transform Phase: Clean and normalize the data
    clean_car_data()

    # Load Phase: Store the cleaned data into PostgreSQL
    load_to_postgresql()

if __name__ == "__main__":
    run_etl()
schedule.every().day.at("09:00").do(run_etl) # Schedule the ETL process to run daily at 9 AM
print("🔁 ETL scheduler started. Waiting for the next run...")

while True:
    schedule.run_pending() # Loop to keep the script running
    time.sleep(1)
# This script orchestrates the ETL process by calling the extract, transform, and load functions in sequence.
# It first fetches car data from the API, then cleans the data, and finally loads it into a PostgreSQL database.
## The ETL process is scheduled to run daily at 9 AM using the `schedule` library.
# The main function ensures that the entire ETL pipeline runs smoothly, handling any potential issues along the way.
