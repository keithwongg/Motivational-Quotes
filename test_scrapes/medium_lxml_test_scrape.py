import requests
import lxml.html
import pprint

html = requests.get('https://timber.io/blog/an-intro-to-web-scraping-with-lxml-and-python/')
doc = lxml.html.fromstring(html.content)
header = doc.xpath('//div[@class="markdown sc-cMljjf geolAC"]')
paragraphs = [line.text_content() for line in header]
with open('medium_lxml_guide.txt', 'w') as f:
    for p in paragraphs:
        f.write(p)