import requests
import json

# API details
API_URL = "https://stocknewsapi.com/api/v1"
params = {
    "tickers": "MSFT",  # Ticker symbol for Microsoft
    "items": 860,       # Number of items to retrieve
    "page": 300,        # Page number
    "token": "mwbnbg1mjalat46lwc31kiu9sqt2rzyyqvnx9wcf",     # Replace with your actual API token
    "date": "01012023-12062024"  # Date range (MMDDYYYY-MMDDYYYY)
}

try:
    # Send GET request to the API
    response = requests.get(API_URL, params=params)
    response.raise_for_status()  # Raise an error for HTTP issues

    # Parse the JSON response
    data = response.json()
    
    # Save the data to a JSON file
    with open("stock_news_page_300.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Data fetched and saved to stock_news_page_300.json successfully!")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
