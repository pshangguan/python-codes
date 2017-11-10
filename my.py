import urllib.request
f = open('tempfile', 'w')
response = urllib.request.urlopen('http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=kitchen+sink')
f.write(str(response.read()))
response.close()

import lxml
from lxml import html
import requests

page = requests.get('http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=kitchen+sink')
tree = html.fromstring(page.content)

elements = tree.get_element_by_id('price')

for ee in elements:
	print (ee.text_content())
