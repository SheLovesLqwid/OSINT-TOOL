# Utility functions
import csv
import json
import os
from tabulate import tabulate

DATA_PATH_CSV = "data/results.csv"
DATA_PATH_JSON = "data/results.json"

def print_table(data, headers=None):
    """Prints data in a table format."""
    print("\n" + tabulate(data, headers=headers, tablefmt="grid") + "\n")

def save_results(data):
    """Saves results to CSV & JSON files."""
    
    # Save to CSV
    with open(DATA_PATH_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)

    # Save to JSON
    try:
        if os.path.exists(DATA_PATH_JSON):
            with open(DATA_PATH_JSON, "r") as f:
                json_data = json.load(f)
        else:
            json_data = []

        json_data.append(data)

        with open(DATA_PATH_JSON, "w") as f:
            json.dump(json_data, f, indent=4)

    except Exception as e:
        print(f"❌ Error saving JSON: {e}")
