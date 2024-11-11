from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import os

# Import the functions from the other files
from fetch_api_data import fetch_api_data
from clean_data import clean_data

# Define the DAG
with DAG(
    'api_data_pipeline',
    default_args={
        'owner': 'olathedataguy',
        'retries': 1,
    },
    description='Simple data pipeline to fetch and clean API data',
    schedule_interval=None,  # Set to None for manual execution
    start_date=datetime(2024, 11, 11),
    catchup=False,
) as dag:

    # Define the task for fetching data from API
    task_fetch_api_data = PythonOperator(
        task_id='fetch_api_data',
        python_callable=fetch_api_data,
    )

    # Define the task for cleaning the data
    task_clean_data = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data,
    )

    # Set the task dependencies
    task_fetch_api_data >> task_clean_data
