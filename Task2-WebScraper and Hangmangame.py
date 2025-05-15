import requests
from bs4 import BeautifulSoup

# Website to scrape
url = "http://quotes.toscrape.com"

# Define headers to mimic a real browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Send a request to the website
response = requests.get(url, headers=headers, timeout=10)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all quote blocks
    quotes = soup.find_all("div", class_="quote")

    # Print each quote and its author
    print("Quotes from the website:\n")
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        print(f"{text} — {author}")
else:
    print(f"Failed to retrieve content: {response.status_code}")






