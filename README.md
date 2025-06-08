# automobile-etl-project

This project performs ETL on car specification data using the API Ninjas car API. Data is cleaned and stored in PostgreSQL.

## Structure

- `etl/extract.py`: Extracts data from the API
- `etl/transform.py`: Cleans and filters the data
- `etl/load.py`: Loads data into PostgreSQL
- `main.py`: Orchestrates the full ETL pipeline
- `run_etl.bat`: Automates daily ETL execution via task scheduler (optional)

## Setup

1. Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set PostgreSQL credentials in environment variables or `.env`.

4. Run the ETL pipeline:
    ```bash
    python main.py
    ```
5. Automate the ETL pipeline (Optional):
   Schedule the run_etl.bat file using Windows Task Scheduler to run the ETL process daily.

## License
MIT
