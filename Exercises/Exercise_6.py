import time
import requests

urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.stackoverflow.com",
    "https://www.realpython.com"
]

def fetch(url):
    print(f"Fetching {url}")
    resp = requests.get(url)
    print(f"Done {url}, length: {len(resp.text)}")
    return len(resp.text)

start = time.time()
results = []
for url in urls:
    results.append(fetch(url))
end = time.time()

print("Sequential results:", results)
print(f"Sequential time taken: {end-start:.2f} seconds")
