import argparse
import requests
from bs4 import BeautifulSoup


def fetch_url(url: str) -> str:
    """Fetch content from the given URL."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def parse_links(html: str) -> list[str]:
    """Extract href links from HTML content."""
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for anchor in soup.find_all('a', href=True):
        links.append(anchor['href'])
    return links


def main():
    parser = argparse.ArgumentParser(description="Simple OSINT automation tool")
    parser.add_argument("url", help="URL to fetch")
    args = parser.parse_args()

    html = fetch_url(args.url)
    links = parse_links(html)
    for link in links:
        print(link)


if __name__ == "__main__":
    main()
