# Metadata extractor module
from PIL import Image
from PIL.ExifTags import TAGS
import os
import json

def start_lookup():
    file_path = input("Enter file path: ")

    if not os.path.exists(file_path):
        print("❌ File not found.")
        return None

    print("🔍 Extracting metadata...")

    metadata = {}
    
    try:
        with Image.open(file_path) as img:
            exif_data = img._getexif()
            if exif_data:
                for tag, value in exif_data.items():
                    metadata[TAGS.get(tag, tag)] = value
    except:
        print("❌ Not an image file or no metadata found.")
        return None

    for key, value in metadata.items():
        print(f"{key}: {value}")

    return [["Metadata", json.dumps(metadata, indent=4)]]
