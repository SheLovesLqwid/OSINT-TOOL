# Phone lookup module
import requests
from modules.utils import print_table

def start_lookup():
    phone = input("Enter phone number (+CountryCode): ")
    api_key = "YOUR_API_KEY"
    api_url = f"https://api.numlookupapi.com/{phone}?apiKey={api_key}"
    
    response = requests.get(api_url)
    data = response.json()
    
    results = [
        ["Phone Number", data.get("number", "N/A")],
        ["Country", data.get("country_name", "N/A")],
        ["Location", data.get("location", "N/A")],
        ["Carrier", data.get("carrier", "N/A")],
        ["Line Type", data.get("line_type", "N/A")]
    ]
    
    print_table(results)
    return results
