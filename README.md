# API Data Extraction and Cleaning with Airflow DAG

Overview
===========

This project provides a data pipeline that extracts property listings from the **Bayut API**, cleans the extracted data, and orchestrates the workflow using an **Airflow DAG**. The pipeline involves the following tasks:

- **Extract API Data**: Retrieves property listings from the Bayut API and saves them to a CSV file.
- **Clean Data**: Cleans the raw data by processing specific fields, then saves the cleaned data to a new CSV.
- **Airflow DAG**: Orchestrates the process of data extraction and cleaning through Apache Airflow.

Project Contents
================

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG.

-  **`extract_api_data.py`**: 
   - Connects to the **Bayut API**.
   - Retrieves property listings.
   - Saves the extracted data to `properties_listings.csv`.

- **`clean_data.py`**: 
   - Reads `properties_listings.csv`.
   - Cleans and processes the data.
   - Saves the cleaned data to `cleaned_properties_listings.csv`.

- **`dag_api_data.py`**: 
   - Defines an Airflow DAG to orchestrate the workflow.
   - Runs the **extract API data** task followed by the **clean data** task.


Prerequisites
==============

- **Python 3.x** (recommended version: 3.8 or higher)
- **Docker** (for running Airflow locally)
- **Astro CLI** (for managing Airflow environments)
- **Airflow** (installed via Astro CLI)


Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

2. Access the Airflow UI for local Airflow project. go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

Access your Postgres Database at 'localhost:5432/postgres'.


Acknowledgment
==================

Bayut API: Property data is fetched from the Bayut API via RapidAPI.


