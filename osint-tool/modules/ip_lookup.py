# IP lookup module
import requests
from modules.utils import print_table

def start_lookup():
    ip = input("Enter IP address: ")
    api_url = f"https://ipinfo.io/{ip}/json"
    
    response = requests.get(api_url)
    data = response.json()
    
    results = [
        ["IP Address", data.get("ip", "N/A")],
        ["City", data.get("city", "N/A")],
        ["Region", data.get("region", "N/A")],
        ["Country", data.get("country", "N/A")],
        ["ISP", data.get("org", "N/A")],
        ["Location", data.get("loc", "N/A")]
    ]

    print_table(results)
    return results
