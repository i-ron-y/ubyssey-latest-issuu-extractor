from contextlib import closing
from selenium.webdriver import Firefox
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup

# Extracts latest Ubyssey issue's URL and cover image from the Ubyssey ISSUU page using Selenium WebDriver.

url = 'https://issuu.com/ubyssey/'

with closing(Firefox()) as browser:
	browser.get(url)
	WebDriverWait(browser, timeout=10).until(
		lambda x: x.find_elements_by_class_name('cover'))
	page_source = browser.page_source

soup = BeautifulSoup(page_source, 'html.parser')

latestIssue = soup.findAll('a', {'class': 'cover'})[0]

issueUrl = 'https://issuu.com' + latestIssue.get('href')
print(issueUrl)

coverImage = latestIssue.find('img').get('src')
print(coverImage)