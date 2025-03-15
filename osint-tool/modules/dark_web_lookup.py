# Dark web lookup module
import requests
from modules.utils import print_table

def start_lookup():
    query = input("Enter search term for Dark Web: ")
    tor_proxy = "socks5h://127.0.0.1:9050"
    
    print("🔍 Searching Dark Web... (Ensure TOR is running)")

    dark_web_sources = [
        f"http://hss3uro2hsxfogfq.onion/search?q={query}",
        f"http://msydqstlz2kzerdg.onion/search?q={query}"
    ]

    results = []
    
    for url in dark_web_sources:
        try:
            response = requests.get(url, proxies={"http": tor_proxy, "https": tor_proxy}, timeout=15)
            if response.status_code == 200:
                results.append([url, "✅ Found"])
            else:
                results.append([url, "❌ No Data"])
        except:
            results.append([url, "❌ Connection Failed"])

    print_table(results, headers=["Dark Web Source", "Status"])
    return results
