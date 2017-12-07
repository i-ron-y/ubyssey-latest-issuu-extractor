# Ubyssey Latest ISSUU Extractor

Extracts the URL and cover image of the latest Ubyssey print issue from [The Ubyssey's ISSUU page](https://issuu.com/ubyssey).

Currently only prints the links to console.

Two versions:
- `ubyssey-latest-issuu-extractor-selenium.py` uses Selenium WebDriver to extract the latest Ubyssey issue's URL and cover image from the Ubyssey ISSUU page.
- `ubyssey-latest-issuu-extractor-rss.py` extracts the latest Ubyssey issue's URL and cover image from the Ubyssey ISSUU page's RSS feed without having to use Selenium WebDriver.

## Usage

Install Python.

**For ubyssey-latest-issuu-extractor-selenium.py:**

Install the required packages:

````
pip install selenium
pip install BeautifulSoup4
````

Download and unzip [geckodriver](https://github.com/mozilla/geckodriver/releases), and add it to PATH.

Go to the directory where `ubyssey-latest-issuu-extractor-selenium.py` is located.

Run:

````
python ubyssey-latest-issuu-extractor-selenium.py
````

**For ubyssey-latest-issuu-extractor-rss.py:**

Install the required packages:

````
pip install requests
pip install BeautifulSoup4
pip install lxml
````

Go to the directory where `ubyssey-latest-issuu-extractor-rss.py` is located.

Run:

````
python ubyssey-latest-issuu-extractor-rss.py
````
