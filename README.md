# Web Scraping with Python

A comprehensive web scraping project that demonstrates various techniques for extracting data from websites using Python.

## 🚀 Features

- **Basic Web Scraping**: Extract links, titles, and text from web pages
- **Advanced Scraping**: Handle forms, tables, JSON APIs, and images
- **Error Handling**: Robust error handling for network requests
- **SSL Support**: Handles SSL certificate issues
- **Multiple Examples**: Various real-world scraping scenarios

## 📁 Project Structure

```
Web-Scraping-/
├── webscraping.py          # Basic web scraping script
├── advanced_webscraping.py # Advanced scraping examples
├── install_dependencies.py # Dependency installation script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Installation

### Option 1: Automatic Installation
```bash
python3 install_dependencies.py
```

### Option 2: Manual Installation
```bash
pip3 install -r requirements.txt
```

## 🎯 Usage

### Basic Web Scraping
```bash
python3 webscraping.py
```

This script demonstrates:
- Extracting navigation links
- Getting page titles
- Finding all links on a page
- Basic error handling

### Advanced Web Scraping
```bash
python3 advanced_webscraping.py
```

This script includes:
- Quote scraping from quotes.toscrape.com
- News headline extraction
- Table data scraping
- JSON API data extraction
- Link and image extraction

## 📚 What You'll Learn

- **Data Extraction**: Using Beautiful Soup to parse HTML
- **Network Requests**: Making HTTP requests with proper headers
- **Error Handling**: Handling network errors and SSL issues
- **Data Processing**: Extracting structured data from web pages
- **API Integration**: Working with JSON APIs
- **Best Practices**: Following ethical web scraping guidelines

## 🔧 Dependencies

- `beautifulsoup4==4.12.2` - HTML/XML parsing
- `lxml==4.9.3` - Fast XML and HTML parser
- `requests==2.31.0` - HTTP library (for future enhancements)

## ⚠️ Important Notes

- **Respect robots.txt**: Always check the website's robots.txt file
- **Rate Limiting**: Don't overwhelm servers with too many requests
- **Terms of Service**: Ensure you comply with website terms
- **Legal Compliance**: Be aware of legal implications in your jurisdiction

## 🌟 Example Output

```
Web Scraping Demo
==================================================
Scraping website: https://example.com
--------------------------------------------------
No navigation element found on the page
No links found in navigation

--------------------------------------------------
Page title: Example Domain

--------------------------------------------------
Found 1 total links on the page:
1. https://www.iana.org/domains/example

==================================================
Web scraping demo completed!
```

## 🚀 Getting Started

1. Clone or download this repository
2. Install dependencies using one of the methods above
3. Run the basic script: `python3 webscraping.py`
4. Try the advanced examples: `python3 advanced_webscraping.py`
5. Modify the scripts to scrape your target websites

## 📖 Learning Resources

- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Python urllib Documentation](https://docs.python.org/3/library/urllib.html)
- [Web Scraping Best Practices](https://blog.hartleybrody.com/web-scraping/)

## 🤝 Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project!

## 📄 License

This project is open source and available under the MIT License.
