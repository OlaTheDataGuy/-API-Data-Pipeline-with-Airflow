import requests
import pandas as pd
import ast

# Define API request parameters
url = "https://bayut-com1.p.rapidapi.com/properties/list"
querystring = {
    "name": "Abu Dhabi",  # Change to "Dubai" for Dubai data
    "purpose": "for-rent",
    "hitsPerPage": "50",
    "page": "0",
    "sort": "city-level-score"
}

headers = {
    "x-rapidapi-key": "79cb86260amshab2c1d34d2dd2aep12be33jsna9986011b056",  # Replace with your API key
    "x-rapidapi-host": "bayut-com1.p.rapidapi.com"
}

def fetch_api_data():
    # Send GET request to the API
    response = requests.get(url, headers=headers, params=querystring)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()

        # Extract the relevant listings and convert to DataFrame
        listings = data.get("hits", [])
        df = pd.DataFrame(listings)[['contactName', 'phoneNumber', 'title', 'area', 'baths',
                                     'completionStatus', 'furnishingStatus', 'rooms', 'geography', 'price']]

        # Save the data to CSV
        df.to_csv('properties_listings.csv', index=False)
        print("Data saved to properties_listings.csv")
    else:
        print("Failed to fetch data:", response.status_code)

if __name__ == "__main__":
    fetch_api_data()
