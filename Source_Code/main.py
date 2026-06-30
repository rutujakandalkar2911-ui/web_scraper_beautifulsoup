import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "lxml")

    quotes = soup.find_all("span", class_="text")

    print("Quotes from Website:\n")

    for i, quote in enumerate(quotes, 1):
        print(f"{i}. {quote.text}")
else:
    print("Failed to fetch website.")