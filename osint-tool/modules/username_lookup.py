# Username lookup module
import requests
from modules.utils import print_table

SOCIAL_MEDIA = {
    "Facebook": "https://www.facebook.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "Snapchat": "https://www.snapchat.com/add/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "GitHub": "https://github.com/{}",
    "LinkedIn": "https://www.linkedin.com/in/{}"
}

def start_lookup():
    username = input("Enter username: ")
    results = []

    for platform, url in SOCIAL_MEDIA.items():
        profile_url = url.format(username)
        response = requests.get(profile_url)

        if response.status_code == 200:
            results.append([platform, "✅ Found", profile_url])
        else:
            results.append([platform, "❌ Not Found", "N/A"])

    print_table(results, headers=["Platform", "Status", "Profile Link"])
    return results
