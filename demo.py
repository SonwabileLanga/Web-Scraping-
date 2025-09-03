#!/usr/bin/env python3
"""
Demo script showing how to use the web scraping functions.
This script demonstrates basic usage of the web scraping utilities.
"""

from webscraping import scrape_website, get_page_title, get_all_links, get_page_text

def demo_basic_scraping():
    """Demonstrate basic web scraping functions."""
    print("Web Scraping Demo")
    print("=" * 50)
    
    # Example URLs to scrape
    urls = [
        "https://example.com",
        "https://httpbin.org/html"
    ]
    
    for url in urls:
        print(f"\nScraping: {url}")
        print("-" * 30)
        
        # Get page title
        title = get_page_title(url)
        print(f"Title: {title}")
        
        # Get navigation links
        nav_links = scrape_website(url)
        print(f"Navigation links: {len(nav_links)} found")
        for link in nav_links[:3]:  # Show first 3
            print(f"  - {link}")
        
        # Get all links
        all_links = get_all_links(url)
        print(f"All links: {len(all_links)} found")
        for link in all_links[:3]:  # Show first 3
            print(f"  - {link}")
        
        # Get page text (first 100 characters)
        text = get_page_text(url)
        if text:
            print(f"Page text preview: {text[:100]}...")
        
        print()

def demo_custom_url():
    """Allow user to input a custom URL to scrape."""
    print("\nCustom URL Demo")
    print("=" * 50)
    
    url = input("Enter a URL to scrape (or press Enter to skip): ").strip()
    
    if not url:
        print("Skipping custom URL demo.")
        return
    
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"\nScraping: {url}")
    print("-" * 30)
    
    try:
        # Get page title
        title = get_page_title(url)
        print(f"Title: {title}")
        
        # Get all links
        all_links = get_all_links(url)
        print(f"Found {len(all_links)} links:")
        for i, link in enumerate(all_links[:10], 1):
            print(f"  {i}. {link}")
        
        if len(all_links) > 10:
            print(f"  ... and {len(all_links) - 10} more links")
            
    except Exception as e:
        print(f"Error scraping {url}: {e}")

def main():
    """Main demo function."""
    demo_basic_scraping()
    demo_custom_url()
    
    print("\n" + "=" * 50)
    print("Demo completed!")
    print("\nTo run the full examples:")
    print("  python3 webscraping.py")
    print("  python3 advanced_webscraping.py")

if __name__ == "__main__":
    main()
