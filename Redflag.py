import sys
import requests
import re

def fetch_and_search(url, domain):
    response = requests.get(url)
    if response.status_code == 200:
        if re.search(r'\b' + re.escape(domain) + r'\b', response.text):
            return True
    return False

def check_domain(domain):
    urls = [
        "https://dl.red.flag.domains/red.flag.domains.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-NEW-today.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-ACTIVE.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-ACTIVE-today.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-ACTIVE-TODAY.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-links-ACTIVE-NOW.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-NEW-last-hour.txt",
        "https://raw.githubusercontent.com/mitchellkrogza/Phishing.Database/master/phishing-domains-ACTIVE.txt"
    ]

    found_urls = []
    for url in urls:
        if fetch_and_search(url, domain):
            found_urls.append(url)

    if found_urls:
        print(f"Domain '{domain}' was found in the following lists:")
        for url in found_urls:
            print(url)
    else:
        print(f"Domain '{domain}' was not found in any list.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <domain>")
    else:
        domain = sys.argv[1]
        check_domain(domain)
