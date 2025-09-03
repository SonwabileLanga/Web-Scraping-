import bs4 as bs
import urllib.request
import urllib.error
import ssl
import sys

def scrape_website(url):
    """
    Scrape a website and extract links from navigation elements.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        list: List of href attributes from navigation links
    """
    try:
        # Create SSL context that doesn't verify certificates (for testing purposes)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        # Add headers to mimic a real browser request
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        
        # Open the URL and read the content
        with urllib.request.urlopen(req, context=ssl_context) as response:
            source = response.read()
        
        # Parse the HTML content (try lxml first, fallback to html.parser)
        try:
            soup = bs.BeautifulSoup(source, 'lxml')
        except:
            soup = bs.BeautifulSoup(source, 'html.parser')
        
        # Find navigation element
        nav = soup.nav
        
        if nav:
            links = []
            for url_element in nav.find_all('a'):
                href = url_element.get('href')
                if href:
                    links.append(href)
            return links
        else:
            print("No navigation element found on the page")
            return []
            
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e}")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def get_page_title(url):
    """
    Extract the title of a webpage.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        str: The page title or None if not found
    """
    try:
        # Create SSL context that doesn't verify certificates (for testing purposes)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            source = response.read()
        
        soup = bs.BeautifulSoup(source, 'lxml')
        title = soup.title
        
        if title:
            return title.string
        return None
        
    except Exception as e:
        print(f"Error getting page title: {e}")
        return None

def get_all_links(url):
    """
    Extract all links from a webpage.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        list: List of all href attributes found on the page
    """
    try:
        # Create SSL context that doesn't verify certificates (for testing purposes)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            source = response.read()
        
        soup = bs.BeautifulSoup(source, 'lxml')
        links = []
        
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                links.append(href)
        
        return links
        
    except Exception as e:
        print(f"Error getting links: {e}")
        return []

def get_page_text(url):
    """
    Extract all text content from a webpage.
    
    Args:
        url (str): The URL to scrape
        
    Returns:
        str: All text content from the page
    """
    try:
        # Create SSL context that doesn't verify certificates (for testing purposes)
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        
        with urllib.request.urlopen(req, context=ssl_context) as response:
            source = response.read()
        
        soup = bs.BeautifulSoup(source, 'lxml')
        return soup.get_text()
        
    except Exception as e:
        print(f"Error getting page text: {e}")
        return ""

def main():
    # Use a publicly accessible website for testing
    url = 'https://example.com'
    
    print(f"Web Scraping Demo")
    print("=" * 50)
    print(f"Scraping website: {url}")
    print("-" * 50)
    
    # Test navigation links scraping
    links = scrape_website(url)
    
    if links:
        print("Found links in navigation:")
        for i, link in enumerate(links, 1):
            print(f"{i}. {link}")
    else:
        print("No links found in navigation")
    
    print("\n" + "-" * 50)
    
    # Test page title extraction
    title = get_page_title(url)
    if title:
        print(f"Page title: {title}")
    else:
        print("Could not extract page title")
    
    print("\n" + "-" * 50)
    
    # Test all links extraction
    all_links = get_all_links(url)
    if all_links:
        print(f"Found {len(all_links)} total links on the page:")
        for i, link in enumerate(all_links[:10], 1):  # Show first 10 links
            print(f"{i}. {link}")
        if len(all_links) > 10:
            print(f"... and {len(all_links) - 10} more links")
    else:
        print("No links found on the page")
    
    print("\n" + "=" * 50)
    print("Web scraping demo completed!")

if __name__ == "__main__":
    main()