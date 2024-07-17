import requests
from bs4 import BeautifulSoup
import json

topics = []
page = requests.get('https://myislam.org/quran-verses/')  # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup

topicsDiv = soup.find_all("div", {"class": "quran-topic-card"})

for div in topicsDiv:
    children = div.findChildren()
    for child in children:
        for titlediv in child.findChildren():
            topics.append(
                {
                    'name': titlediv.text,
                    'url' : child['href']
                }
            )
with open('results/topics-link.json', 'w') as f:
    json.dump(topics, f)

