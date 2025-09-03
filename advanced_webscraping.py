#!/usr/bin/env python3
"""
Advanced Web Scraping Examples
This script demonstrates various web scraping techniques including:
- Basic HTML parsing
- Form handling
- Data extraction from tables
- Image downloading
- JSON API scraping
"""

import bs4 as bs
import urllib.request
import urllib.error
import urllib.parse
import ssl
import json
import os
import sys
from datetime import datetime

def create_ssl_context():
    """Create SSL context for HTTPS requests."""
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    return ssl_context

def make_request(url, headers=None):
    """
    Make a web request with proper error handling.
    
    Args:
        url (str): The URL to request
        headers (dict): Optional headers to include
        
    Returns:
        bytes: The response content or None if failed
    """
    try:
        if headers is None:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        
        req = urllib.request.Request(url, headers=headers)
        ssl_context = create_ssl_context()
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            return response.read()
            
    except urllib.error.URLError as e:
        print(f"Error accessing URL {url}: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def scrape_quotes():
    """
    Scrape quotes from quotes.toscrape.com
    """
    print("Scraping quotes from quotes.toscrape.com...")
    print("-" * 50)
    
    url = "http://quotes.toscrape.com/"
    content = make_request(url)
    
    if not content:
        return
    
            # Parse HTML (try lxml first, fallback to html.parser)
        try:
            soup = bs.BeautifulSoup(content, 'lxml')
        except:
            soup = bs.BeautifulSoup(content, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    if quotes:
        print(f"Found {len(quotes)} quotes:")
        for i, quote in enumerate(quotes[:5], 1):  # Show first 5 quotes
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            print(f"{i}. \"{text}\" - {author}")
        
        if len(quotes) > 5:
            print(f"... and {len(quotes) - 5} more quotes")
    else:
        print("No quotes found")

def scrape_news_headlines():
    """
    Scrape news headlines from a news website
    """
    print("\nScraping news headlines...")
    print("-" * 50)
    
    # Using a simple news site
    url = "https://news.ycombinator.com/"
    content = make_request(url)
    
    if not content:
        return
    
            # Parse HTML (try lxml first, fallback to html.parser)
        try:
            soup = bs.BeautifulSoup(content, 'lxml')
        except:
            soup = bs.BeautifulSoup(content, 'html.parser')
    stories = soup.find_all('tr', class_='athing')
    
    if stories:
        print(f"Found {len(stories)} news stories:")
        for i, story in enumerate(stories[:10], 1):  # Show first 10 stories
            title_elem = story.find('span', class_='titleline')
            if title_elem:
                title = title_elem.get_text().strip()
                print(f"{i}. {title}")
        
        if len(stories) > 10:
            print(f"... and {len(stories) - 10} more stories")
    else:
        print("No news stories found")

def scrape_table_data():
    """
    Scrape data from HTML tables
    """
    print("\nScraping table data...")
    print("-" * 50)
    
    # Using a site with tables
    url = "https://en.wikipedia.org/wiki/List_of_countries_by_population"
    content = make_request(url)
    
    if not content:
        return
    
            # Parse HTML (try lxml first, fallback to html.parser)
        try:
            soup = bs.BeautifulSoup(content, 'lxml')
        except:
            soup = bs.BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table', class_='wikitable')
    
    if tables:
        table = tables[0]  # Get the first table
        rows = table.find_all('tr')
        
        print("Top 5 countries by population:")
        for i, row in enumerate(rows[1:6], 1):  # Skip header, get first 5 data rows
            cells = row.find_all(['td', 'th'])
            if len(cells) >= 2:
                country = cells[1].get_text().strip()
                population = cells[2].get_text().strip()
                print(f"{i}. {country}: {population}")
    else:
        print("No tables found")

def scrape_json_api():
    """
    Scrape data from a JSON API
    """
    print("\nScraping JSON API data...")
    print("-" * 50)
    
    # Using JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/posts"
    content = make_request(url)
    
    if not content:
        return
    
    try:
        data = json.loads(content.decode('utf-8'))
        print(f"Found {len(data)} posts from JSON API:")
        
        for i, post in enumerate(data[:5], 1):  # Show first 5 posts
            title = post.get('title', 'No title')
            print(f"{i}. {title}")
        
        if len(data) > 5:
            print(f"... and {len(data) - 5} more posts")
            
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

def extract_links_and_images(url):
    """
    Extract all links and images from a webpage
    """
    print(f"\nExtracting links and images from {url}...")
    print("-" * 50)
    
    content = make_request(url)
    if not content:
        return
    
            # Parse HTML (try lxml first, fallback to html.parser)
        try:
            soup = bs.BeautifulSoup(content, 'lxml')
        except:
            soup = bs.BeautifulSoup(content, 'html.parser')
    
    # Extract links
    links = soup.find_all('a', href=True)
    print(f"Found {len(links)} links:")
    for i, link in enumerate(links[:10], 1):  # Show first 10 links
        href = link['href']
        text = link.get_text().strip()
        if text:
            print(f"{i}. {text} -> {href}")
        else:
            print(f"{i}. {href}")
    
    if len(links) > 10:
        print(f"... and {len(links) - 10} more links")
    
    # Extract images
    images = soup.find_all('img', src=True)
    print(f"\nFound {len(images)} images:")
    for i, img in enumerate(images[:5], 1):  # Show first 5 images
        src = img['src']
        alt = img.get('alt', 'No alt text')
        print(f"{i}. {alt} -> {src}")
    
    if len(images) > 5:
        print(f"... and {len(images) - 5} more images")

def main():
    """Main function to run all scraping examples."""
    print("Advanced Web Scraping Examples")
    print("=" * 60)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Run different scraping examples
    scrape_quotes()
    scrape_news_headlines()
    scrape_table_data()
    scrape_json_api()
    extract_links_and_images("https://example.com")
    
    print("\n" + "=" * 60)
    print("Advanced web scraping demo completed!")
    print(f"Finished at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
