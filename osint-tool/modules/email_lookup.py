# Email lookup module
import requests
from modules.utils import print_table

def start_lookup():
    email = input("Enter email: ")
    api_url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    
    headers = {"User-Agent": "OSINT-Tool"}
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        breaches = response.json()
        results = [[b["Name"], b["Domain"], b["BreachDate"]] for b in breaches]
        print_table(results, headers=["Breach Name", "Domain", "Date"])
        return results
    else:
        print("✅ No breaches found for this email.")
        return None
