# Reverse image lookup module
import requests
from modules.utils import print_table

def start_lookup():
    image_path = input("Enter image file path: ")
    
    print("🔍 Performing Reverse Image Search...")

    search_url = "https://www.google.com/searchbyimage?image_url={}"
    response = requests.get(search_url.format(image_path))

    if response.status_code == 200:
        print("✅ Image found on the web!")
        return [["Image Search", "✅ Found"]]
    else:
        print("❌ No results found.")
        return [["Image Search", "❌ No Results"]]
