import re
import sys
from collections import Counter

import requests

if len(sys.argv) < 2:
    print(f"usage: python {sys.argv[0]} <url>")
    sys.exit(1)

url = sys.argv[1]
html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}).text

links = re.findall(r'href\s*=\s*["\']?([^"\'\s>]+)', html, re.IGNORECASE)

for link, n in Counter(links).most_common():
    print(f"{n:>3}  {link}")

print("----")
print(f"all links: {len(links)}, unique: {len(set(links))}")
