import re

import requests
from bs4 import BeautifulSoup
import json

ayah = []
pattern = r"Surah (.+) Ayat (\d+)(?:-(\d+))?"

with open('results/topics-link.json') as f:
    d = json.load(f)

for x in d['topics']:
    page = requests.get(x['url'])
    soup = BeautifulSoup(page.content, 'html.parser')  # Parsing content using beautifulsoup
    ll = soup.select('.chapter-title div:first-child')
    print(ll)
    for l in ll:
        dc = l.select('a:first-child')
        if len(dc) == 0:
            continue
        match = re.search(pattern, dc[0].text)
        if match:
            surah = match.group(1)
            start_ayat = match.group(2)
            end_ayat = match.group(3) if match.group(3) else start_ayat
            start_ayat = int(start_ayat)
            end_ayat = int(end_ayat)

            ayah.append({
                'surah' : surah,
                'ayat' : [a for a in range(start_ayat, end_ayat+1)],
                'topic': x['name']
            })
with open('results/v2-topics-quran.json', 'w') as f:
    json.dump(ayah, f)

