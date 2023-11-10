import sys
import requests
from datetime import date, timedelta

today = date.today()
one_day_ago = str(today - timedelta(days=1))

WEBSITE_URL = "https://red.flag.domains/posts/" + one_day_ago
print(WEBSITE_URL)

async def check_for_word(word):
    response = requests.get(WEBSITE_URL)
    if response.status_code == 200:
        if word in response.text:
            message = f"Warning: A potential domain similar to '{word}' was recently registered. Make sure you are not a victim of phishing attacks. Check the source here: {WEBSITE_URL}"
            print(message)
        else:
            print("No relevant word found.")
    else:
        print(f"Could not connect to the website {WEBSITE_URL}.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <word>")
    else:
        word = sys.argv[1]
        asyncio.run(check_for_word(word))
