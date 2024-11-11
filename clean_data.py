import pandas as pd
import ast

def clean_data():
    # Read the data from CSV
    df = pd.read_csv('properties_listings.csv')

    # Clean the 'phoneNumber' column (convert string representation of dict into actual dict)
    df['phoneNumber'] = df['phoneNumber'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Extract relevant phone numbers
    df['mobile'] = df['phoneNumber'].apply(lambda x: x.get('mobile', '') if isinstance(x, dict) else '')
    df['phone'] = df['phoneNumber'].apply(lambda x: x.get('phone', '') if isinstance(x, dict) else '')

    # Clean the 'geography' column (convert string representation of dict into actual dict)
    df['geography'] = df['geography'].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else x)

    # Extract latitude and longitude
    df['latitude'] = df['geography'].apply(lambda x: x.get('lat', None) if isinstance(x, dict) else None)
    df['longitude'] = df['geography'].apply(lambda x: x.get('lng', None) if isinstance(x, dict) else None)

    # Remove unnecessary columns
    df.drop(columns=['phoneNumber', 'geography'], inplace=True)

    # Save cleaned data back to CSV
    df.to_csv('cleaned_properties_listings.csv', index=False)
    print("Cleaned data saved to cleaned_properties_listings.csv")

if __name__ == "__main__":
    clean_data()
