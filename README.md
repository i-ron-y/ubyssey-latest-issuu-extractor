# Ubyssey Latest ISSUU Extractor

Extracts the URL and cover image of the latest Ubyssey print issue from [The Ubyssey's ISSUU page](https://issuu.com/ubyssey).

Currently only prints the links to console.

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
````

Go to the directory where `ubyssey-latest-issuu-extractor-rss.py` is located.

Run:

````
python ubyssey-latest-issuu-extractor-rss.py
````
