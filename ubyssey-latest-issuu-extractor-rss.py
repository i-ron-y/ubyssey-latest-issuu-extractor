import requests
from bs4 import BeautifulSoup

# Extracts latest Ubyssey issue's URL and cover image from the Ubyssey ISSUU page's RSS feed.

page = requests.get('http://search.issuu.com/ubyssey/docs/recent.rss')
soup = BeautifulSoup(page.content, 'xml')
latestIssue = soup.findAll('item')[0]

issueUrl = latestIssue.find('link').get_text()
print(issueUrl)

coverImage = latestIssue.find('media:content').get('url')
print(coverImage)