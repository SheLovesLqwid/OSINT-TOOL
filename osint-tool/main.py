# Main CLI interface
import os
import sys
import time
import json
from modules import (
    ip_lookup, phone_lookup, email_lookup, username_lookup,
    dark_web_lookup, reverse_image, metadata_extractor, whois_dns
)
from modules.utils import save_results

# Load settings from config file
CONFIG_PATH = "config/settings.json"

def main_menu():
    while True:
        print("\n🔍 OPEN-SOURCE OSINT TOOL")
        print("1. IP Lookup")
        print("2. Phone Number Lookup")
        print("3. Email Lookup")
        print("4. Username Lookup")
        print("5. Dark Web Lookup")
        print("6. Reverse Image Search")
        print("7. Metadata Extraction")
        print("8. WHOIS & DNS Lookup")
        print("9. Exit")

        choice = input("\nSelect an option: ")

        if choice == "1":
            result = ip_lookup.start_lookup()
        elif choice == "2":
            result = phone_lookup.start_lookup()
        elif choice == "3":
            result = email_lookup.start_lookup()
        elif choice == "4":
            result = username_lookup.start_lookup()
        elif choice == "5":
            result = dark_web_lookup.start_lookup()
        elif choice == "6":
            result = reverse_image.start_lookup()
        elif choice == "7":
            result = metadata_extractor.start_lookup()
        elif choice == "8":
            result = whois_dns.start_lookup()
        elif choice == "9":
            print("Exiting... Stay stealthy! 🕵️‍♂️")
            sys.exit()
        else:
            print("❌ Invalid choice. Try again.")

        if result:
            save_results(result)

if __name__ == "__main__":
    main_menu()
